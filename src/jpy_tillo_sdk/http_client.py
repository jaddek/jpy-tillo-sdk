import logging
from abc import ABC
from dataclasses import asdict
from typing import Any

from httpx import AsyncClient, Client, Response

from .contracts import ClientInterface, EndpointInterface, RequestBodyAbstract, RequestQueryAbstract
from .endpoint import Endpoint
from .errors import AuthenticationFailed, InvalidIpAddress, UnprocessableContent, ValidationError
from .signature import SignatureBridge

logger = logging.getLogger("tillo.http_client")


class AbstractClient(ClientInterface, ABC):
    _signer: SignatureBridge

    def __init__(self, tillo_client_options: dict[str, Any] | None, signer: SignatureBridge):
        self.tillo_client_options = tillo_client_options or {}
        self._signer = signer
        logger.debug("Initialized HTTP client with options: %s", tillo_client_options)

    def _get_request_headers(self, method: str, endpoint: str, sign_attrs: tuple[str, ...]) -> dict[str, Any]:
        logger.debug("Generating headers for %s %s", method, endpoint)

        (request_api_key, request_signature, request_timestamp) = self._signer.sign(
            endpoint,
            method,
            sign_attrs,
        )

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "API-Key": request_api_key,
            "Signature": request_signature,
            "Timestamp": request_timestamp,
            "User-Agent": "JpyTilloSDKClient/0.2",
        }

        logger.debug(
            "Generated headers: %s",
            {k: v for k, v in headers.items() if k not in ["Signature", "API-Key"]},
        )
        return headers

    def _catch_non_200_response(
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


class AsyncHttpClient(AbstractClient):
    async def request(self, endpoint: Endpoint) -> Response:  # type: ignore
        json: dict[str, Any] | None = None
        params: dict[str, Any] | None = None

        if isinstance(endpoint.body, RequestBodyAbstract):
            json = asdict(endpoint.body)

        if isinstance(endpoint.query, RequestQueryAbstract):
            params = asdict(endpoint.query)

        logger.info("Making async request to %s %s", endpoint.method, endpoint.endpoint)
        logger.debug(
            "Request details: %s",
            {
                "method": endpoint.method,
                "endpoint": endpoint.endpoint,
                "route": endpoint.route,
                "body": endpoint.body,
            },
        )

        headers = self._get_request_headers(
            endpoint.method,
            endpoint.endpoint,
            endpoint.sign_attrs,
        )

        try:
            async with AsyncClient(**self.tillo_client_options) as client:
                logger.debug(
                    "Sending async request to %s with method %s",
                    endpoint.route,
                    endpoint.method,
                )
                response = await client.request(
                    url=endpoint.route,
                    method=endpoint.method,
                    params=params,
                    json=json,
                    headers=headers,
                )
                logger.debug("Received response with status code: %d", response.status_code)

                if response.status_code != 200:
                    self._catch_non_200_response(response)
                return response
        except Exception as e:
            logger.error("Error making async request to %s: %s", endpoint.route, str(e))
            raise


class HttpClient(AbstractClient):
    def request(
        self,
        endpoint: Endpoint | EndpointInterface,
    ) -> Response:
        json: dict[str, Any] | None = None
        params: dict[str, Any] | None = None

        if isinstance(endpoint.body, RequestBodyAbstract):
            json = asdict(endpoint.body)

        if isinstance(endpoint.query, RequestQueryAbstract):
            params = asdict(endpoint.query)

        logger.info("Making sync request to %s %s", endpoint.method, endpoint.endpoint)
        logger.debug(
            "Request details: %s",
            {
                "method": endpoint.method,
                "endpoint": endpoint.endpoint,
                "route": endpoint.route,
            },
        )

        headers = self._get_request_headers(
            endpoint.method,
            endpoint.endpoint,
            endpoint.sign_attrs,
        )

        try:
            with Client(**self.tillo_client_options) as client:
                logger.debug(
                    "Sending sync request to %s with method %s",
                    endpoint.route,
                    endpoint.method,
                )
                response = client.request(
                    url=endpoint.route,
                    method=endpoint.method,
                    params=params,
                    json=json,
                    headers=headers,
                )
                logger.debug("Received response with status code: %d", response.status_code)

                if response.status_code != 200:
                    self._catch_non_200_response(response)

                return response
        except Exception as e:
            logger.error("Error making sync request to %s: %s", endpoint.route, str(e))
            raise
