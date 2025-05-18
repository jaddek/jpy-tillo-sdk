import logging
from abc import ABC
from dataclasses import asdict
from typing import Any, Generic, TypeAlias, TypeVar, cast, final

from httpx import AsyncBaseTransport, AsyncClient, BaseTransport, Client, Response
from httpx._client import BaseClient

from .contracts import ClientInterface, EndpointInterface, SignatureAttributesInterface
from .endpoint import Endpoint
from .errors import AuthenticationFailed, InvalidIpAddress, UnprocessableContent, ValidationError
from .signature import SignatureBridge

logger = logging.getLogger("tillo.http_client")


class ErrorHandler:
    def handle(
        self,
        response: Response,
    ) -> None:
        status_code = response.status_code
        content_code = response.json().get("code")

        logger.debug(
            "Checking response code and content code: %d - %s",
            status_code,
            content_code,
        )

        if status_code == 201:
            logger.error("Received 201 response code, raising InvalidIpAddress")
            raise InvalidIpAddress(response)
        elif status_code == 422:
            if content_code == UnprocessableContent.TILLO_ERROR_CODE:
                logger.error("Received 422 response code, invalid data")
                raise UnprocessableContent(response)
            elif content_code == UnprocessableContent.TILLO_ERROR_CODE:
                logger.error("Received 401 response code, unauthorized")
                raise ValidationError(response)
        elif status_code == 401:
            if content_code == AuthenticationFailed.TILLO_ERROR_CODE:
                logger.error("Received 401 response code, unauthorized")
                raise AuthenticationFailed(response)


class RequestDataExtractor:
    _signer: SignatureBridge

    def __init__(self, signer: SignatureBridge) -> None:
        self._signer = signer

    def extract_request_headers(self, endpoint: EndpointInterface) -> dict[str, Any]:
        logger.debug("Generating headers for %s %s", endpoint.method, endpoint.endpoint)

        request_api_key, request_signature, request_timestamp = self._signer.sign(
            endpoint.endpoint,
            endpoint.method,
            endpoint.sign_attrs,
        )

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "API-Key": request_api_key,
            "Signature": request_signature,
            "Timestamp": request_timestamp,
            "User-Agent": "JpyTilloSDKClient/0.3",
        }

        logger.debug(
            "Generated headers: %s",
            {k: v for k, v in headers.items() if k not in ["Signature", "API-Key"]},
        )

        return headers

    def extract_request_params(self, endpoint: EndpointInterface) -> tuple[dict[str, Any] | None, ...]:
        json: dict[str, Any] | None = (
            asdict(endpoint.body) if isinstance(endpoint.body, SignatureAttributesInterface) else None
        )
        params: dict[str, Any] | None = (
            asdict(endpoint.query) if isinstance(endpoint.query, SignatureAttributesInterface) else None
        )

        return params, json

    def extract_all(self, endpoint: EndpointInterface) -> tuple[dict[str, Any] | None, ...]:
        params, json = self.extract_request_params(endpoint)

        return (
            self.extract_request_headers(endpoint),
            params,
            json,
        )


TClient = TypeVar("TClient", bound=BaseClient)
UTransport: TypeAlias = BaseTransport | AsyncBaseTransport | None


class AbstractClient(ClientInterface, ABC, Generic[TClient]):
    _extractor: RequestDataExtractor
    _error_handler: ErrorHandler
    _client: TClient | None = None
    _transport: UTransport = None

    def __init__(
        self,
        tillo_client_options: dict[str, Any] | None,
        *,
        extractor: RequestDataExtractor,
        error_handler: ErrorHandler,
        transport: UTransport = None,
        client: TClient | None = None,
    ):
        self.tillo_client_options = tillo_client_options or {}
        self._extractor = extractor
        self._error_handler = error_handler
        self._client = client
        self._transport = transport


@final
class AsyncHttpClient(AbstractClient["AsyncClient"]):
    async def request(self, endpoint: Endpoint) -> Response:  # type: ignore
        headers, params, json = self._extractor.extract_all(endpoint)

        if self._client is None:
            self._client = AsyncClient(
                transport=cast(AsyncBaseTransport, self._transport),
                **self.tillo_client_options,
            )

        try:
            logger.debug(
                "Sending async request to %s with method %s",
                endpoint.route,
                endpoint.method,
            )

            response = await self._client.request(
                url=endpoint.route,
                method=endpoint.method,
                params=params,
                json=json,
                headers=headers,
            )
            logger.debug("Received response with status code: %d", response.status_code)

            if response.status_code != 200:
                self._error_handler.handle(response)
            return response
        except Exception as e:
            logger.error("Error making async request to %s: %s", endpoint.route, str(e))
            raise e

    async def close_connection(self) -> None:
        if isinstance(self._client, AsyncClient):
            await self._client.aclose()


@final
class HttpClient(AbstractClient[Client]):
    def request(
        self,
        endpoint: Endpoint | EndpointInterface,
    ) -> Response:
        headers, params, json = self._extractor.extract_all(endpoint)

        if self._client is None:
            self._client = Client(transport=cast(BaseTransport, self._transport), **self.tillo_client_options)

        try:
            logger.debug(
                "Sending sync request to %s with method %s",
                endpoint.route,
                endpoint.method,
            )

            response = self._client.request(
                url=endpoint.route,
                method=endpoint.method,
                params=params,
                json=json,
                headers=headers,
            )
            logger.debug("Received response with status code: %d", response.status_code)

            if response.status_code != 200:
                self._error_handler.handle(response)

            return response
        except Exception as e:
            logger.error("Error making sync request to %s: %s", endpoint.route, str(e))
            raise

    def close_connection(self) -> None:
        if self._client is not None:
            self._client.close()
