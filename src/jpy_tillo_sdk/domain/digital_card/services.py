from typing import Any, Optional

from httpx import Response

from ...contracts import IssueDigitalCodeServiceAsyncInterface, IssueDigitalCodeServiceInterface
from ...http_client import AsyncHttpClient, HttpClient
from .endpoints import (
    CancelDigitalCodeEndpoint,
    CancelDigitalUrlEndpoint,
    CheckBalanceEndpoint,
    CheckDigitalOrderStatusAsyncEndpoint,
    CheckStockEndpoint,
    IssueDigitalCodeEndpoint,
    OrderDigitalCodeAsyncEndpoint,
    ReverseDigitalCodeEndpoint,
    TopUpDigitalCodeEndpoint,
)


class IssueDigitalCodeServiceAsync(IssueDigitalCodeServiceAsyncInterface):
    def __init__(self, *, client: AsyncHttpClient):
        """Initialize the float service with an HTTP client.

        Args:
            client (HttpClient): The HTTP client instance for making requests
        """
        self.client = client

    async def issue_digital_code(
        self,
        query_params: Optional[dict] = None,
        body: Optional[IssueDigitalCodeEndpoint.RequestBody] = None,
    ) -> Response:
        endpoint = IssueDigitalCodeEndpoint(body=body, query=query_params)
        return await self.client.request(endpoint=endpoint)

    async def order_digital_code(
        self,
        query_params: Optional[dict] = None,
        body: Optional[OrderDigitalCodeAsyncEndpoint.RequestBody] = None,
    ) -> Response:
        endpoint = OrderDigitalCodeAsyncEndpoint(body=body, query=query_params)
        return await self.client.request(endpoint=endpoint)

    async def check_digital_order(
        self,
        query_params: Optional[dict] = None,
    ) -> Response:
        endpoint = CheckDigitalOrderStatusAsyncEndpoint(query=query_params)
        return await self.client.request(endpoint=endpoint)

    async def top_up_digital_code(
        self,
        query_params: Optional[dict] = None,
        body: Optional[TopUpDigitalCodeEndpoint.RequestBody] = None,
    ) -> Response:
        endpoint = TopUpDigitalCodeEndpoint(body=body, query=query_params)
        return await self.client.request(endpoint=endpoint)

    async def cancel_digital_url(
        self,
        query_params: Optional[dict] = None,
        body: Optional[CancelDigitalUrlEndpoint.RequestBody] = None,
    ) -> Response:
        endpoint = CancelDigitalUrlEndpoint(body=body, query=query_params)
        return await self.client.request(endpoint=endpoint)

    async def cancel_digital_code(
        self,
        query_params: Optional[dict] = None,
        body: Optional[CancelDigitalCodeEndpoint.RequestBody] = None,
    ) -> Response:
        endpoint = CancelDigitalCodeEndpoint(body=body, query=query_params)
        return await self.client.request(endpoint=endpoint)

    async def check_balance(
        self,
        query_params: Optional[dict] = None,
        body: Optional[CheckBalanceEndpoint.RequestBody] = None,
    ) -> Response:
        endpoint = CheckBalanceEndpoint(body=body, query=query_params)
        return await self.client.request(endpoint=endpoint)

    async def check_stock(
        self,
        query_params: Optional[dict] = None,
    ) -> Response:
        endpoint = CheckStockEndpoint(query=query_params)
        return await self.client.request(endpoint=endpoint)

    async def reverse_digital_code(
        self,
        query_params: Optional[dict] = None,
        body: Optional[ReverseDigitalCodeEndpoint.RequestBody] = None,
    ) -> Response:
        endpoint = ReverseDigitalCodeEndpoint(body=body, query=query_params)
        return await self.client.request(endpoint=endpoint)


class IssueDigitalCodeService(IssueDigitalCodeServiceInterface):
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
    ) -> Response:
        endpoint = IssueDigitalCodeEndpoint(body=body, query=query_params)
        return self.client.request(endpoint=endpoint)

    def order_digital_code(
        self,
        query_params: Optional[dict] = None,
        body: Optional[OrderDigitalCodeAsyncEndpoint.RequestBody] = None,
    ) -> Response:
        endpoint = OrderDigitalCodeAsyncEndpoint(body=body, query=query_params)
        return self.client.request(endpoint=endpoint)

    def check_digital_order(
        self,
        query_params: Optional[dict] = None,
    ) -> Response:
        endpoint = CheckDigitalOrderStatusAsyncEndpoint(query=query_params)
        return self.client.request(endpoint=endpoint)

    def top_up_digital_code(
        self,
        query_params: Optional[dict] = None,
        body: Optional[TopUpDigitalCodeEndpoint.RequestBody] = None,
    ) -> Response:
        endpoint = TopUpDigitalCodeEndpoint(body=body)
        return self.client.request(endpoint=endpoint)

    def cancel_digital_url(
        self,
        query_params: Optional[dict] = None,
        body: Optional[CancelDigitalUrlEndpoint.RequestBody] = None,
    ) -> Response:
        endpoint = CancelDigitalUrlEndpoint(body=body)
        return self.client.request(endpoint=endpoint)

    def cancel_digital_code(
        self,
        query_params: Optional[dict] = None,
        body: Optional[CancelDigitalCodeEndpoint.RequestBody] = None,
    ) -> Response:
        endpoint = CancelDigitalCodeEndpoint(body=body)
        return self.client.request(endpoint=endpoint)

    def reverse_digital_code(
        self,
        query_params: Optional[dict] = None,
        body: Optional[ReverseDigitalCodeEndpoint.RequestBody] = None,
    ) -> Response:
        endpoint = ReverseDigitalCodeEndpoint(body=body)
        return self.client.request(endpoint=endpoint)

    def check_stock(
        self,
        query_params: Optional[Any] = None,
    ) -> Response:
        endpoint = CheckStockEndpoint(query=query_params)
        return self.client.request(endpoint=endpoint)

    def check_balance(
        self,
        query_params: Optional[Any] = None,
        body: Optional[CheckBalanceEndpoint.RequestBody] = None,
    ) -> Response:
        endpoint = CheckBalanceEndpoint(body=body)
        return self.client.request(endpoint=endpoint)
