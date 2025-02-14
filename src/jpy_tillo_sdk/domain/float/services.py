import logging

from .endpoints import CheckFloatsEndpoint
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
    def request_payment_transfer():
        logger.debug("Method request_payment_transfer not implemented.")
        raise NotImplementedError("This method is not implemented.")

    @staticmethod
    async def request_payment_transfer_async():
        logger.debug("Method request_payment_transfer_async not implemented.")
        raise NotImplementedError("This method is not implemented.")
