import logging

from httpx import Response

from ...contracts import PhysicalCardsAsyncServiceInterface, PhysicalCardsServiceInterface, SignatureAttributesInterface
from .endpoints import (
    ActivatePhysicalCardEndpoint,
    ActivatePhysicalCardERequestBody,
    BalanceCheckPhysicalEndpoint,
    BalanceCheckPhysicalRequestBody,
    CancelActivateEndpoint,
    CancelActivateRequestBody,
    CancelTopUpRequestBody,
    CashOutOriginalTransactionEndpoint,
    CashOutOriginalTransactionRequestBody,
    FulfilPhysicalCardOrderEndpoint,
    FulfilPhysicalCardOrderEndpointRequestBody,
    OrderPhysicalCardEndpoint,
    OrderPhysicalCardRequestBody,
    PhysicalCardOrderStatusEndpoint,
    PhysicalCardOrderStatusRequestBody,
    TopUpPhysicalCardEndpoint,
    TopUpPhysicalCardRequestBody,
)

logger = logging.getLogger("tillo.brand_physical_cards")


class PhysicalCardsAsyncService(PhysicalCardsAsyncServiceInterface):
    async def activate_physical_card_async(
        self,
        query: SignatureAttributesInterface | None = None,
        body: ActivatePhysicalCardERequestBody | None = None,
    ) -> Response:
        endpoint = ActivatePhysicalCardEndpoint(body=body, query=query)

        response = await self._client.request(
            endpoint=endpoint,
        )

        return response

    async def cancel_activate_physical_card_async(
        self,
        query: SignatureAttributesInterface | None = None,
        body: CancelActivateRequestBody | None = None,
    ) -> Response:
        endpoint = CancelActivateEndpoint(body=body, query=query)

        response = await self._client.request(
            endpoint=endpoint,
        )

        return response

    async def order_status_async(self, body: PhysicalCardOrderStatusRequestBody) -> Response:
        endpoint = PhysicalCardOrderStatusEndpoint(
            body=body,
        )

        response = await self._client.request(endpoint=endpoint)

        return response

    async def cash_out_original_transaction_physical_card_async(
        self,
        query: SignatureAttributesInterface | None = None,
        body: CashOutOriginalTransactionRequestBody | None = None,
    ) -> Response:
        endpoint = CashOutOriginalTransactionEndpoint(body=body, query=query)

        response = await self._client.request(
            endpoint=endpoint,
        )

        return response

    async def balance_check_physical_async(
        self,
        query: SignatureAttributesInterface | None = None,
        body: BalanceCheckPhysicalRequestBody | None = None,
    ) -> Response:
        endpoint = BalanceCheckPhysicalEndpoint(
            body=body,
            query=query,
        )

        response = await self._client.request(endpoint=endpoint)

        return response

    async def order_physical_card_async(
        self,
        query: SignatureAttributesInterface | None = None,
        body: OrderPhysicalCardRequestBody | None = None,
    ) -> Response:
        endpoint = OrderPhysicalCardEndpoint(
            body=body,
            query=query,
        )

        response = await self._client.request(endpoint=endpoint)

        return response

    async def cancel_top_up_on_physical_card_async(
        self,
        query: SignatureAttributesInterface | None = None,
        body: CancelTopUpRequestBody | None = None,
    ) -> Response:
        endpoint = CancelActivateEndpoint(
            body=body,
            query=query,
        )

        response = await self._client.request(endpoint=endpoint)

        return response

    async def top_up_physical_card_async(
        self,
        query: SignatureAttributesInterface | None = None,
        body: TopUpPhysicalCardRequestBody | None = None,
    ) -> Response:
        endpoint = TopUpPhysicalCardEndpoint(
            body=body,
            query=query,
        )

        response = await self._client.request(endpoint=endpoint)

        return response

    async def fulfil_physical_card_order_async(
        self, body: FulfilPhysicalCardOrderEndpointRequestBody | None = None
    ) -> Response:
        endpoint = FulfilPhysicalCardOrderEndpoint(
            body=body,
        )

        response = await self._client.request(endpoint=endpoint)

        return response


class PhysicalCardsService(PhysicalCardsServiceInterface):
    def activate_physical_card(
        self,
        query: SignatureAttributesInterface | None = None,
        body: ActivatePhysicalCardERequestBody | None = None,
    ) -> Response:
        endpoint = ActivatePhysicalCardEndpoint(
            body=body,
            query=query,
        )

        response = self._client.request(endpoint=endpoint)

        return response

    def cancel_activate_physical_card(
        self,
        query: SignatureAttributesInterface | None = None,
        body: CancelActivateRequestBody | None = None,
    ) -> Response:
        endpoint = CancelActivateEndpoint(
            body=body,
            query=query,
        )

        response = self._client.request(endpoint=endpoint)

        return response

    def cash_out_original_transaction(
        self,
        query: SignatureAttributesInterface | None = None,
        body: CashOutOriginalTransactionRequestBody | None = None,
    ) -> Response:
        endpoint = ActivatePhysicalCardEndpoint(
            body=body,
            query=query,
        )

        response = self._client.request(endpoint=endpoint)

        return response

    def top_up_physical_card(
        self,
        body: TopUpPhysicalCardRequestBody | None = None,
    ) -> Response:
        endpoint = TopUpPhysicalCardEndpoint(
            body=body,
        )

        response = self._client.request(endpoint=endpoint)

        return response

    def cancel_top_up(
        self,
        body: CancelTopUpRequestBody | None = None,
    ) -> Response:
        endpoint = CancelActivateEndpoint(
            body=body,
        )

        response = self._client.request(endpoint=endpoint)

        return response

    def order_physical_card(
        self,
        query: SignatureAttributesInterface | None = None,
        body: OrderPhysicalCardRequestBody | None = None,
    ) -> Response:
        endpoint = OrderPhysicalCardEndpoint(
            body=body,
            query=query,
        )

        response = self._client.request(endpoint=endpoint)

        return response

    def order_status(
        self,
        body: PhysicalCardOrderStatusRequestBody | None = None,
    ) -> Response:
        endpoint = PhysicalCardOrderStatusEndpoint(
            body=body,
        )

        response = self._client.request(endpoint=endpoint)

        return response

    def fulfil_order(
        self,
        body: FulfilPhysicalCardOrderEndpointRequestBody | None = None,
    ) -> Response:
        endpoint = FulfilPhysicalCardOrderEndpoint(
            body=body,
        )

        response = self._client.request(endpoint=endpoint)

        return response

    def balance_check_physical(
        self,
        query: SignatureAttributesInterface | None = None,
        body: BalanceCheckPhysicalRequestBody | None = None,
    ) -> Response:
        endpoint = BalanceCheckPhysicalEndpoint(
            body=body,
            query=query,
        )

        response = self._client.request(endpoint=endpoint)

        return response
