from .endpoints import CheckFloatsEndpoint
from ...http_client import HttpClient, AsyncHttpClient
from typing import Optional


class FloatService:
    @staticmethod
    def check_floats(
        client: HttpClient,
        query_params: Optional[dict] = None,
    ):
        endpoint = CheckFloatsEndpoint(query=query_params)

        response = client.request(
            endpoint=endpoint,
        )

        return response

    @staticmethod
    async def check_floats_async(
        client: AsyncHttpClient,
        query_params: Optional[dict] = None,
    ):
        endpoint = CheckFloatsEndpoint(query=query_params)

        response = await client.request(
            endpoint=endpoint,
        )

        return response

    @staticmethod
    def request_payment_transfer():
        raise NotImplementedError("This method is not implemented.")

    @staticmethod
    async def request_payment_transfer_async():
        raise NotImplementedError("This method is not implemented.")
