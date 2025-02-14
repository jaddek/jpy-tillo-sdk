import logging
from abc import abstractmethod
from typing import Optional

from httpx import Client, AsyncClient, Response

from .endpoint import Endpoint
from .signature import SignatureBridge

logger = logging.getLogger(__name__)


class AbstractClient:
    _signer: SignatureBridge

    def __init__(
            self,
            tillo_client_options:
            dict, signer: SignatureBridge
    ):
        self.tillo_client_options = tillo_client_options
        self._signer = signer

    @abstractmethod
    def request(
            self,
            endpoint: Endpoint,
    ):
        pass

    def _get_request_headers(
            self,
            method: str,
            endpoint: str,
            sign_attrs: Optional[tuple] = None,
    ) -> dict:
        (request_api_key, request_signature, request_timestamp) = self._signer.sign(
            endpoint,
            method,
            sign_attrs,
        )

        return {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "API-Key": request_api_key,
            "Signature": request_signature,
            "Timestamp": request_timestamp,
            "User-Agent": "JpyTilloSDKClient/0.2",
        }


class AsyncHttpClient(AbstractClient):
    async def request(
            self,
            endpoint: Endpoint,
    ) -> Response:
        json: Optional[dict] = None

        logger.debug("Requesting endpoint %s", endpoint)

        # Probably the best option here is to check for POST or GET to identify which parameters should be signed
        if endpoint.is_body_not_empty():
            logger.debug("Requesting endpoint using body for signing: %s", endpoint.body)
            sign_attrs = endpoint.body.get_sign_attrs()
            json = endpoint.body.get_as_dict()
        else:
            logger.debug("Requesting endpoint using query for signing: %s", endpoint.query)
            sign_attrs = endpoint.query.get_sign_attrs()

        headers = self._get_request_headers(
            endpoint.method,
            endpoint.endpoint,
            sign_attrs,
        )

        logger.debug(
            "Headers formed using method <%s>, endpoint <%s>, attrs for signing <%s>",
            endpoint.method,
            endpoint.endpoint,
            sign_attrs if sign_attrs is not None else "No arguments",
        )

        async with AsyncClient(**self.tillo_client_options) as client:
            response = await client.request(
                url=endpoint.route,
                method=endpoint.method,
                params=endpoint.params,
                json=json,
                headers=headers,
            )

        return response


class HttpClient(AbstractClient):
    def request(
            self,
            endpoint: Endpoint,
    ) -> Response:
        json: Optional[dict] = None

        # Probably the best option here is to check for POST or GET to identify which parameters should be signed
        if endpoint.is_body_not_empty():
            logger.debug("Requesting endpoint using body for signing: %s", endpoint.body)
            sign_attrs = endpoint.body.get_sign_attrs()
            json = endpoint.body.get_as_dict()
        else:
            logger.debug("Requesting endpoint using query for signing: %s", endpoint.query)
            sign_attrs = endpoint.query.get_sign_attrs()

        headers = self._get_request_headers(
            endpoint.method,
            endpoint.endpoint,
            sign_attrs,
        )

        logger.debug(
            "Headers formed using method <%s>, endpoint <%s>, attrs for signing <%s>",
            endpoint.method,
            endpoint.endpoint,
            sign_attrs if sign_attrs is not None else "No arguments",
        )

        with Client(**self.tillo_client_options) as client:
            response = client.request(
                url=endpoint.route,
                method=endpoint.method,
                params=endpoint.params,
                json=json,
                headers=headers,
            )

        return response
