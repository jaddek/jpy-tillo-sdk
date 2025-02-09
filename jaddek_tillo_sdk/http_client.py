from abc import abstractmethod
from typing import Optional

from httpx import Client, AsyncClient, Response

from .endpoint import Endpoint
from .signature import SignatureBridge


class AbstractClient:
    _signer: SignatureBridge

    def __init__(self, tillo_client_options: dict, signer: SignatureBridge):
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
            "User-Agent": "TilloSDKPython/0.1",
        }


class AsyncHttpClient(AbstractClient):
    async def request(
        self,
        endpoint: Endpoint,
    ) -> Response:
        json: Optional[dict] = None

        if endpoint.is_body_not_empty():
            sign_attrs = endpoint.body.get_sign_attrs()
            json = endpoint.body.get_as_dict()
        else:
            sign_attrs = endpoint.query.get_sign_attrs()

        headers = self._get_request_headers(
            endpoint.method,
            endpoint.endpoint,
            sign_attrs,
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

        if endpoint.is_body_not_empty():
            sign_attrs = endpoint.body.get_sign_attrs()
            json = endpoint.body.get_as_dict()
        else:
            sign_attrs = endpoint.query.get_sign_attrs()

        headers = self._get_request_headers(
            endpoint.method,
            endpoint.endpoint,
            sign_attrs,
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
