import logging

from .endpoints import CheckFloatsEndpoint, RequestPaymentTransferEndpoint
from ...http_client import HttpClient, AsyncHttpClient
from typing import Optional

logger = logging.getLogger(__name__)


class FloatService:
    @staticmethod
    def check_floats(
            client: HttpClient,
            query_params: Optional[CheckFloatsEndpoint.QueryParams] = None,
    ):
        logger.debug("Checking floats: sync HTTP client with query_params: %s", query_params)

        endpoint = CheckFloatsEndpoint(query=query_params)

        response = client.request(
            endpoint=endpoint,
        )

        return response

    @staticmethod
    async def check_floats_async(
            client: AsyncHttpClient,
            query_params: Optional[CheckFloatsEndpoint.QueryParams] = None,
    ):
        logger.debug("Checking floats: sync HTTP client with query_params: %s", query_params)

        endpoint = CheckFloatsEndpoint(query=query_params)

        response = await client.request(
            endpoint=endpoint,
        )

        return response

    @staticmethod
    def request_payment_transfer(
            client: HttpClient,
            body: RequestPaymentTransferEndpoint.RequestBody
    ):
        logger.debug("Checking floats: sync HTTP client with body: %s", body)

        endpoint = RequestPaymentTransferEndpoint(body=body)

        response = client.request(
            endpoint=endpoint,
        )

        return response

    @staticmethod
    async def request_payment_transfer_async(
            client: AsyncHttpClient,
            body: RequestPaymentTransferEndpoint.RequestBody
    ):
        logger.debug("Checking floats: sync HTTP client with body: %s", body)

        endpoint = RequestPaymentTransferEndpoint(body=body)

        response = await client.request(
            endpoint=endpoint,
        )

        return response
