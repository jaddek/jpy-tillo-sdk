from typing import Any

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
        query_params: Any | None = None,
        body: IssueDigitalCodeEndpoint.RequestBody | None = None,
    ) -> Response:
        endpoint = IssueDigitalCodeEndpoint(body=body, query=query_params)
        return await self.client.request(endpoint=endpoint)

    async def order_digital_code(
        self,
        query_params: Any | None = None,
        body: OrderDigitalCodeAsyncEndpoint.RequestBody | None = None,
    ) -> Response:
        endpoint = OrderDigitalCodeAsyncEndpoint(body=body, query=query_params)
        return await self.client.request(endpoint=endpoint)

    async def check_digital_order(
        self,
        query_params: Any | None = None,
    ) -> Response:
        endpoint = CheckDigitalOrderStatusAsyncEndpoint(query=query_params)
        return await self.client.request(endpoint=endpoint)

    async def top_up_digital_code(
        self,
        query_params: Any | None = None,
        body: TopUpDigitalCodeEndpoint.RequestBody | None = None,
    ) -> Response:
        endpoint = TopUpDigitalCodeEndpoint(body=body, query=query_params)
        return await self.client.request(endpoint=endpoint)

    async def cancel_digital_url(
        self,
        query_params: Any | None = None,
        body: CancelDigitalUrlEndpoint.RequestBody | None = None,
    ) -> Response:
        endpoint = CancelDigitalUrlEndpoint(body=body, query=query_params)
        return await self.client.request(endpoint=endpoint)

    async def cancel_digital_code(
        self,
        query_params: Any | None = None,
        body: CancelDigitalCodeEndpoint.RequestBody | None = None,
    ) -> Response:
        endpoint = CancelDigitalCodeEndpoint(body=body, query=query_params)
        return await self.client.request(endpoint=endpoint)

    async def check_balance(
        self,
        query_params: Any | None = None,
        body: CheckBalanceEndpoint.RequestBody | None = None,
    ) -> Response:
        endpoint = CheckBalanceEndpoint(body=body, query=query_params)
        return await self.client.request(endpoint=endpoint)

    async def check_stock(
        self,
        query_params: Any | None = None,
    ) -> Response:
        endpoint = CheckStockEndpoint(query=query_params)
        return await self.client.request(endpoint=endpoint)

    async def reverse_digital_code(
        self,
        query_params: Any | None = None,
        body: ReverseDigitalCodeEndpoint.RequestBody | None = None,
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
        query_params: dict | None = None,
        body: IssueDigitalCodeEndpoint.RequestBody | None = None,
    ) -> Response:
        endpoint = IssueDigitalCodeEndpoint(body=body, query=query_params)
        return self.client.request(endpoint=endpoint)

    def order_digital_code(
        self,
        query_params: dict | None = None,
        body: OrderDigitalCodeAsyncEndpoint.RequestBody | None = None,
    ) -> Response:
        endpoint = OrderDigitalCodeAsyncEndpoint(body=body, query=query_params)
        return self.client.request(endpoint=endpoint)

    def check_digital_order(
        self,
        query_params: dict | None = None,
    ) -> Response:
        endpoint = CheckDigitalOrderStatusAsyncEndpoint(query=query_params)
        return self.client.request(endpoint=endpoint)

    def top_up_digital_code(
        self,
        query_params: dict | None = None,
        body: TopUpDigitalCodeEndpoint.RequestBody | None = None,
    ) -> Response:
        endpoint = TopUpDigitalCodeEndpoint(body=body)
        return self.client.request(endpoint=endpoint)

    def cancel_digital_url(
        self,
        query_params: dict | None = None,
        body: CancelDigitalUrlEndpoint.RequestBody | None = None,
    ) -> Response:
        endpoint = CancelDigitalUrlEndpoint(body=body)
        return self.client.request(endpoint=endpoint)

    def cancel_digital_code(
        self,
        query_params: dict | None = None,
        body: CancelDigitalCodeEndpoint.RequestBody | None = None,
    ) -> Response:
        endpoint = CancelDigitalCodeEndpoint(body=body)
        return self.client.request(endpoint=endpoint)

    def reverse_digital_code(
        self,
        query_params: dict | None = None,
        body: ReverseDigitalCodeEndpoint.RequestBody | None = None,
    ) -> Response:
        endpoint = ReverseDigitalCodeEndpoint(body=body)
        return self.client.request(endpoint=endpoint)

    def check_stock(
        self,
        query_params: Any | None = None,
    ) -> Response:
        endpoint = CheckStockEndpoint(query=query_params)
        return self.client.request(endpoint=endpoint)

    def check_balance(
        self,
        query_params: Any | None = None,
        body: CheckBalanceEndpoint.RequestBody | None = None,
    ) -> Response:
        endpoint = CheckBalanceEndpoint(body=body)
        return self.client.request(endpoint=endpoint)
