from typing import Any, final

from httpx import Response

from ...contracts import DigitalCardServiceAsyncInterface, DigitalCardServiceInterface, SignatureAttributesInterface
from .endpoints import (
    CancelDigitalCodeEndpoint,
    CancelDigitalCodeRequestBody,
    CancelDigitalUrlEndpoint,
    CancelDigitalUrlRequestBody,
    CheckBalanceEndpoint,
    CheckBalanceRequestBody,
    CheckDigitalOrderStatusAsyncEndpoint,
    CheckStockEndpoint,
    IssueDigitalCodeEndpoint,
    IssueDigitalCodeRequestBody,
    OrderDigitalCodeAsyncEndpoint,
    OrderDigitalCodeAsyncRequestBody,
    ReverseDigitalCodeEndpoint,
    ReverseDigitalCodeRequestBody,
    TopUpDigitalCodeEndpoint,
    TopUpDigitalCodeRequestBody,
)


@final
class DigitalCardServiceAsync(DigitalCardServiceAsyncInterface):
    async def issue_digital_code(
        self,
        query: SignatureAttributesInterface | None = None,
        body: IssueDigitalCodeRequestBody | None = None,
    ) -> Response:
        endpoint = IssueDigitalCodeEndpoint(body=body, query=query)
        return await self.client.request(endpoint=endpoint)

    async def order_digital_code(
        self,
        query: SignatureAttributesInterface | None = None,
        body: OrderDigitalCodeAsyncRequestBody | None = None,
    ) -> Response:
        endpoint = OrderDigitalCodeAsyncEndpoint(body=body, query=query)
        return await self.client.request(endpoint=endpoint)

    async def check_digital_order(
        self,
        query: SignatureAttributesInterface | None = None,
    ) -> Response:
        endpoint = CheckDigitalOrderStatusAsyncEndpoint(query=query)
        return await self.client.request(endpoint=endpoint)

    async def top_up_digital_code(
        self,
        query: SignatureAttributesInterface | None = None,
        body: TopUpDigitalCodeRequestBody | None = None,
    ) -> Response:
        endpoint = TopUpDigitalCodeEndpoint(body=body, query=query)
        return await self.client.request(endpoint=endpoint)

    async def cancel_digital_url(
        self,
        query: SignatureAttributesInterface | None = None,
        body: CancelDigitalUrlRequestBody | None = None,
    ) -> Response:
        endpoint = CancelDigitalUrlEndpoint(body=body, query=query)
        return await self.client.request(endpoint=endpoint)

    async def cancel_digital_code(
        self,
        query: SignatureAttributesInterface | None = None,
        body: CancelDigitalCodeRequestBody | None = None,
    ) -> Response:
        endpoint = CancelDigitalCodeEndpoint(body=body, query=query)
        return await self.client.request(endpoint=endpoint)

    async def check_balance(
        self,
        query: Any | None = None,
        body: CheckBalanceRequestBody | None = None,
    ) -> Response:
        endpoint = CheckBalanceEndpoint(body=body, query=query)
        return await self.client.request(endpoint=endpoint)

    async def check_stock(
        self,
        query: Any | None = None,
    ) -> Response:
        endpoint = CheckStockEndpoint(query=query)
        return await self.client.request(endpoint=endpoint)

    async def reverse_digital_code(
        self,
        query: SignatureAttributesInterface | None = None,
        body: ReverseDigitalCodeRequestBody | None = None,
    ) -> Response:
        endpoint = ReverseDigitalCodeEndpoint(body=body, query=query)
        return await self.client.request(endpoint=endpoint)


@final
class DigitalCardService(DigitalCardServiceInterface):
    def issue_digital_code(
        self,
        query: SignatureAttributesInterface | None = None,
        body: IssueDigitalCodeRequestBody | None = None,
    ) -> Response:
        endpoint = IssueDigitalCodeEndpoint(body=body, query=query)
        return self.client.request(endpoint=endpoint)

    def order_digital_code(
        self,
        query: SignatureAttributesInterface | None = None,
        body: OrderDigitalCodeAsyncRequestBody | None = None,
    ) -> Response:
        endpoint = OrderDigitalCodeAsyncEndpoint(body=body, query=query)
        return self.client.request(endpoint=endpoint)

    def check_digital_order(
        self,
        query: SignatureAttributesInterface | None = None,
    ) -> Response:
        endpoint = CheckDigitalOrderStatusAsyncEndpoint(query=query)
        return self.client.request(endpoint=endpoint)

    def top_up_digital_code(
        self,
        query: SignatureAttributesInterface | None = None,
        body: TopUpDigitalCodeRequestBody | None = None,
    ) -> Response:
        endpoint = TopUpDigitalCodeEndpoint(body=body)
        return self.client.request(endpoint=endpoint)

    def cancel_digital_url(
        self,
        query: SignatureAttributesInterface | None = None,
        body: CancelDigitalUrlRequestBody | None = None,
    ) -> Response:
        endpoint = CancelDigitalUrlEndpoint(body=body)
        return self.client.request(endpoint=endpoint)

    def cancel_digital_code(
        self,
        query: SignatureAttributesInterface | None = None,
        body: CancelDigitalCodeRequestBody | None = None,
    ) -> Response:
        endpoint = CancelDigitalCodeEndpoint(body=body)
        return self.client.request(endpoint=endpoint)

    def reverse_digital_code(
        self,
        query: SignatureAttributesInterface | None = None,
        body: ReverseDigitalCodeRequestBody | None = None,
    ) -> Response:
        endpoint = ReverseDigitalCodeEndpoint(body=body)
        return self.client.request(endpoint=endpoint)

    def check_stock(
        self,
        query: SignatureAttributesInterface | None = None,
    ) -> Response:
        endpoint = CheckStockEndpoint(query=query)
        return self.client.request(endpoint=endpoint)

    def check_balance(
        self,
        query: SignatureAttributesInterface | None = None,
        body: CheckBalanceRequestBody | None = None,
    ) -> Response:
        endpoint = CheckBalanceEndpoint(body=body)
        return self.client.request(endpoint=endpoint)
