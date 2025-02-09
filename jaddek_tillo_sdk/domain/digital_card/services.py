from typing import Optional
from .endpoints import (
    IssueDigitalCodeEndpoint,
    OrderDigitalCodeAsyncEndpoint,
    CheckDigitalOrderStatusAsyncEndpoint,
    TopUpDigitalCodeEndpoint,
    CancelDigitalUrlEndpoint,
    CancelDigitalCodeEndpoint,
    ReverseDigitalCodeEndpoint,
    CheckStockEndpoint,
    CheckBalanceEndpoint,
)
from ...http_client import HttpClient, AsyncHttpClient


class IssueDigitalCodeService:
    @staticmethod
    def issue_digital_code(
        client: HttpClient,
        query_params: Optional[dict] = None,
        body: Optional[IssueDigitalCodeEndpoint.RequestBody] = None,
    ):
        endpoint = IssueDigitalCodeEndpoint(body=body, query=query_params)
        return client.request(endpoint=endpoint)

    @staticmethod
    async def issue_digital_code_async(
        client: AsyncHttpClient,
        query_params: Optional[dict] = None,
        body: Optional[IssueDigitalCodeEndpoint.RequestBody] = None,
    ):
        endpoint = IssueDigitalCodeEndpoint(body=body, query=query_params)
        return await client.request(endpoint=endpoint)

    @staticmethod
    def order_digital_code(
        client: HttpClient,
        query_params: Optional[dict] = None,
        body: Optional[OrderDigitalCodeAsyncEndpoint.RequestBody] = None,
    ):
        endpoint = OrderDigitalCodeAsyncEndpoint(body=body, query=query_params)
        return client.request(endpoint=endpoint)

    @staticmethod
    async def order_digital_code_async(
        client: AsyncHttpClient,
        query_params: Optional[dict] = None,
        body: Optional[OrderDigitalCodeAsyncEndpoint.RequestBody] = None,
    ):
        endpoint = OrderDigitalCodeAsyncEndpoint(body=body, query=query_params)
        return await client.request(endpoint=endpoint)

    @staticmethod
    def check_digital_order(
        client: HttpClient,
        query_params: Optional[dict] = None,
    ):
        endpoint = CheckDigitalOrderStatusAsyncEndpoint(query=query_params)
        return client.request(endpoint=endpoint)

    @staticmethod
    async def check_digital_order_async(
        client: AsyncHttpClient,
        query_params: Optional[dict] = None,
    ):
        endpoint = CheckDigitalOrderStatusAsyncEndpoint(query=query_params)
        return await client.request(endpoint=endpoint)

    @staticmethod
    def top_up_digital_code(
        client: HttpClient,
        query_params: Optional[dict] = None,
        body: Optional[TopUpDigitalCodeEndpoint.RequestBody] = None,
    ):
        endpoint = TopUpDigitalCodeEndpoint(body=body, query=query_params)
        return client.request(endpoint=endpoint)

    @staticmethod
    async def top_up_digital_code_async(
        client: AsyncHttpClient,
        query_params: Optional[dict] = None,
        body: Optional[TopUpDigitalCodeEndpoint.RequestBody] = None,
    ):
        endpoint = TopUpDigitalCodeEndpoint(body=body, query=query_params)
        return await client.request(endpoint=endpoint)

    @staticmethod
    def cancel_digital_url(
        client: HttpClient,
        query_params: Optional[dict] = None,
        body: Optional[CancelDigitalUrlEndpoint.RequestBody] = None,
    ):
        endpoint = CancelDigitalUrlEndpoint(body=body, query=query_params)
        return client.request(endpoint=endpoint)

    @staticmethod
    async def cancel_digital_url_async(
        client: AsyncHttpClient,
        query_params: Optional[dict] = None,
        body: Optional[CancelDigitalUrlEndpoint.RequestBody] = None,
    ):
        endpoint = CancelDigitalUrlEndpoint(body=body, query=query_params)
        return await client.request(endpoint=endpoint)

    @staticmethod
    def cancel_digital_code(
        client: HttpClient,
        query_params: Optional[dict] = None,
        body: Optional[CancelDigitalCodeEndpoint.RequestBody] = None,
    ):
        endpoint = CancelDigitalCodeEndpoint(body=body, query=query_params)
        return client.request(endpoint=endpoint)

    @staticmethod
    async def cancel_digital_code_async(
        client: AsyncHttpClient,
        query_params: Optional[dict] = None,
        body: Optional[CancelDigitalCodeEndpoint.RequestBody] = None,
    ):
        endpoint = CancelDigitalCodeEndpoint(body=body, query=query_params)
        return await client.request(endpoint=endpoint)

    @staticmethod
    def reverse_digital_code(
        client: HttpClient,
        query_params: Optional[dict] = None,
        body: Optional[ReverseDigitalCodeEndpoint.RequestBody] = None,
    ):
        endpoint = ReverseDigitalCodeEndpoint(body=body, query=query_params)
        return client.request(endpoint=endpoint)

    @staticmethod
    async def reverse_digital_code_async(
        client: AsyncHttpClient,
        query_params: Optional[dict] = None,
        body: Optional[ReverseDigitalCodeEndpoint.RequestBody] = None,
    ):
        endpoint = ReverseDigitalCodeEndpoint(body=body, query=query_params)
        return await client.request(endpoint=endpoint)

    @staticmethod
    def check_stock(
        client: HttpClient,  # Fixed type hint from AsyncHttpClient to HttpClient
        query_params: Optional[dict] = None,
    ):
        endpoint = CheckStockEndpoint(query=query_params)
        return client.request(endpoint=endpoint)

    @staticmethod
    async def check_stock_async(
        client: AsyncHttpClient,
        query_params: Optional[dict] = None,
    ):
        endpoint = CheckStockEndpoint(query=query_params)
        return await client.request(endpoint=endpoint)

    @staticmethod
    def check_balance(
        client: HttpClient,
        query_params: Optional[dict] = None,
        body: Optional[CheckBalanceEndpoint.RequestBody] = None,
    ):
        endpoint = CheckBalanceEndpoint(body=body, query=query_params)
        return client.request(endpoint=endpoint)

    @staticmethod
    async def check_balance_async(
        client: AsyncHttpClient,
        query_params: Optional[dict] = None,
        body: Optional[CheckBalanceEndpoint.RequestBody] = None,
    ):
        endpoint = CheckBalanceEndpoint(body=body, query=query_params)
        return await client.request(endpoint=endpoint)
