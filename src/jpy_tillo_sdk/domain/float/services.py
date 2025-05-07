import logging

from httpx import Response

from .endpoints import CheckFloatsEndpoint, RequestPaymentTransferEndpoint
from ...http_client import HttpClient, AsyncHttpClient
from typing import Optional

logger = logging.getLogger(__name__)


class FloatService:
    @staticmethod
    def check_floats(
        client: HttpClient,
        query_params: Optional[CheckFloatsEndpoint.QueryParams] = None,
    ) -> Response:
        logger.debug(
            "Checking floats: sync HTTP client with query_params: %s", query_params
        )

        endpoint = CheckFloatsEndpoint(query=query_params)

        response = client.request(
            endpoint=endpoint,
        )

        return response

    @staticmethod
    async def check_floats_async(
        client: AsyncHttpClient,
        query_params: Optional[CheckFloatsEndpoint.QueryParams] = None,
    ) -> Response:
        logger.debug(
            "Checking floats: sync HTTP client with query_params: %s", query_params
        )

        endpoint = CheckFloatsEndpoint(query=query_params)

        response = await client.request(
            endpoint=endpoint,
        )

        return response

    @staticmethod
    def request_payment_transfer(
        client: HttpClient, body: RequestPaymentTransferEndpoint.RequestBody
    ) -> Response:
        logger.debug("Checking floats: sync HTTP client with body: %s", body)

        endpoint = RequestPaymentTransferEndpoint(body=body)

        response = client.request(
            endpoint=endpoint,
        )

        return response

    @staticmethod
    async def request_payment_transfer_async(
        client: AsyncHttpClient, body: RequestPaymentTransferEndpoint.RequestBody
    ) -> Response:
        logger.debug("Checking floats: sync HTTP client with body: %s", body)

        endpoint = RequestPaymentTransferEndpoint(body=body)

        response = await client.request(
            endpoint=endpoint,
        )

        return response


class FloatServiceAsyncInstance:
    def __init__(self, *, client: AsyncHttpClient):
        self.client = client

    async def check_floats_async(
        self,
        query_params: Optional[CheckFloatsEndpoint.QueryParams] = None,
    ) -> Response:
        response = await FloatService.check_floats_async(
            self.client, query_params=query_params
        )

        return response

    async def request_payment_transfer_async(
        self, body: RequestPaymentTransferEndpoint.RequestBody
    ) -> Response:
        response = await FloatService.request_payment_transfer_async(
            self.client, body=body
        )

        return response
