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


class IssueDigitalCodeServiceAsync:
    def __init__(self, *, client: AsyncHttpClient):
        """Initialize the float service with an HTTP client.

        Args:
            client (HttpClient): The HTTP client instance for making requests
        """
        self.client = client

    async def issue_digital_code_async(
            self,
            query_params: Optional[dict] = None,
            body: Optional[IssueDigitalCodeEndpoint.RequestBody] = None,
    ):
        endpoint = IssueDigitalCodeEndpoint(body=body, query=query_params)
        return await self.client.request(endpoint=endpoint)

    async def order_digital_code_async(
            self,
            query_params: Optional[dict] = None,
            body: Optional[OrderDigitalCodeAsyncEndpoint.RequestBody] = None,
    ):
        endpoint = OrderDigitalCodeAsyncEndpoint(body=body, query=query_params)
        return await self.client.request(endpoint=endpoint)

    async def check_digital_order_async(
            self,
            query_params: Optional[dict] = None,
    ):
        endpoint = CheckDigitalOrderStatusAsyncEndpoint(query=query_params)
        return await self.client.request(endpoint=endpoint)

    async def top_up_digital_code_async(
            self,
            query_params: Optional[dict] = None,
            body: Optional[TopUpDigitalCodeEndpoint.RequestBody] = None,
    ):
        endpoint = TopUpDigitalCodeEndpoint(body=body, query=query_params)
        return await self.client.request(endpoint=endpoint)

    async def cancel_digital_url_async(
            self,
            query_params: Optional[dict] = None,
            body: Optional[CancelDigitalUrlEndpoint.RequestBody] = None,
    ):
        endpoint = CancelDigitalUrlEndpoint(body=body, query=query_params)
        return await self.client.request(endpoint=endpoint)

    async def cancel_digital_code_async(
            self,
            query_params: Optional[dict] = None,
            body: Optional[CancelDigitalCodeEndpoint.RequestBody] = None,
    ):
        endpoint = CancelDigitalCodeEndpoint(body=body, query=query_params)
        return await self.client.request(endpoint=endpoint)

    async def check_balance_async(
            self,
            query_params: Optional[dict] = None,
            body: Optional[CheckBalanceEndpoint.RequestBody] = None,
    ):
        endpoint = CheckBalanceEndpoint(body=body, query=query_params)
        return await self.client.request(endpoint=endpoint)

    async def check_stock_async(
            self,
            query_params: Optional[dict] = None,
    ):
        endpoint = CheckStockEndpoint(query=query_params)
        return await self.client.request(endpoint=endpoint)

    async def reverse_digital_code_async(
            self,
            query_params: Optional[dict] = None,
            body: Optional[ReverseDigitalCodeEndpoint.RequestBody] = None,
    ):
        endpoint = ReverseDigitalCodeEndpoint(body=body, query=query_params)
        return await self.client.request(endpoint=endpoint)


class IssueDigitalCodeService:
    def __init__(self, *, client: HttpClient):
        """Initialize the float service with an HTTP client.

        Args:
            client (HttpClient): The HTTP client instance for making requests
        """
        self.client = client

    def issue_digital_code(
            self,
            query_params: Optional[dict] = None,
            body: Optional[IssueDigitalCodeEndpoint.RequestBody] = None,
    ):
        endpoint = IssueDigitalCodeEndpoint(body=body, query=query_params)
        return self.client.request(endpoint=endpoint)

    def order_digital_code(
            self,
            query_params: Optional[dict] = None,
            body: Optional[OrderDigitalCodeAsyncEndpoint.RequestBody] = None,
    ):
        endpoint = OrderDigitalCodeAsyncEndpoint(body=body, query=query_params)
        return self.client.request(endpoint=endpoint)

    def check_digital_order(
            self,
            query_params: Optional[dict] = None,
    ):
        endpoint = CheckDigitalOrderStatusAsyncEndpoint(query=query_params)
        return self.client.request(endpoint=endpoint)

    def top_up_digital_code(
            self,
            query_params: Optional[dict] = None,
            body: Optional[TopUpDigitalCodeEndpoint.RequestBody] = None,
    ):
        endpoint = TopUpDigitalCodeEndpoint(body=body, query=query_params)
        return self.client.request(endpoint=endpoint)

    def cancel_digital_url(
            self,
            query_params: Optional[dict] = None,
            body: Optional[CancelDigitalUrlEndpoint.RequestBody] = None,
    ):
        endpoint = CancelDigitalUrlEndpoint(body=body, query=query_params)
        return self.client.request(endpoint=endpoint)

    def cancel_digital_code(
            self,
            query_params: Optional[dict] = None,
            body: Optional[CancelDigitalCodeEndpoint.RequestBody] = None,
    ):
        endpoint = CancelDigitalCodeEndpoint(body=body, query=query_params)
        return self.client.request(endpoint=endpoint)

    def reverse_digital_code(
            self,
            query_params: Optional[dict] = None,
            body: Optional[ReverseDigitalCodeEndpoint.RequestBody] = None,
    ):
        endpoint = ReverseDigitalCodeEndpoint(body=body, query=query_params)
        return self.client.request(endpoint=endpoint)

    def check_stock(
            self,
            query_params: Optional[dict] = None,
    ):
        endpoint = CheckStockEndpoint(query=query_params)
        return self.client.request(endpoint=endpoint)

    def check_balance(
            self,
            query_params: Optional[dict] = None,
            body: Optional[CheckBalanceEndpoint.RequestBody] = None,
    ):
        endpoint = CheckBalanceEndpoint(body=body, query=query_params)
        return self.client.request(endpoint=endpoint)
