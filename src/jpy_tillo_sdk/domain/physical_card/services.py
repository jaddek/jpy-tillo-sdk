from httpx import Response

from ...http_client import AsyncHttpClient, HttpClient
from .endpoints import (
    ActivatePhysicalCardEndpoint,
    BalanceCheckPhysicalEndpoint,
    CancelActivatePhysicalCardEndpoint,
    CashOutOriginalTransactionPhysicalCardEndpoint,
    FulfilPhysicalCardOrderEndpoint,
    OrderPhysicalCardEndpoint,
    PhysicalCardOrderStatusEndpoint,
    TopUpPhysicalCardEndpoint,
)


class PhysicalGiftCardsService:
    @staticmethod
    def activate_physical_card(
        client: HttpClient,
        query_params: dict | None = None,
        body: ActivatePhysicalCardEndpoint.RequestBody | None = None,
    ) -> Response:
        endpoint = ActivatePhysicalCardEndpoint(
            body=body,
            query=query_params,
        )

        response = client.request(endpoint=endpoint)

        return response

    @staticmethod
    async def activate_physical_card_async(
        client: AsyncHttpClient,
        query_params: dict | None = None,
        body: ActivatePhysicalCardEndpoint.RequestBody | None = None,
    ) -> Response:
        endpoint = ActivatePhysicalCardEndpoint(body=body, query=query_params)

        response = await client.request(
            endpoint=endpoint,
        )

        return response

    @staticmethod
    def cancel_activate_physical_card(
        client: HttpClient,
        query_params: dict | None = None,
        body: CancelActivatePhysicalCardEndpoint.RequestBody | None = None,
    ) -> Response:
        endpoint = CancelActivatePhysicalCardEndpoint(
            body=body,
            query=query_params,
        )

        response = client.request(endpoint=endpoint)

        return response

    @staticmethod
    async def cancel_activate_physical_card_async(
        client: AsyncHttpClient,
        query_params: dict | None = None,
        body: CancelActivatePhysicalCardEndpoint.RequestBody | None = None,
    ) -> Response:
        endpoint = CancelActivatePhysicalCardEndpoint(body=body, query=query_params)

        response = await client.request(
            endpoint=endpoint,
        )

        return response

    @staticmethod
    def cash_out_original_transaction_physical_card(
        client: HttpClient,
        query_params: dict | None = None,
        body: CashOutOriginalTransactionPhysicalCardEndpoint.RequestBody | None = None,
    ) -> Response:
        endpoint = ActivatePhysicalCardEndpoint(
            body=body,
            query=query_params,
        )

        response = client.request(endpoint=endpoint)

        return response

    @staticmethod
    async def cash_out_original_transaction_physical_card_async(
        client: AsyncHttpClient,
        query_params: dict | None = None,
        body: CashOutOriginalTransactionPhysicalCardEndpoint.RequestBody | None = None,
    ) -> Response:
        endpoint = CashOutOriginalTransactionPhysicalCardEndpoint(body=body, query=query_params)

        response = await client.request(
            endpoint=endpoint,
        )

        return response

    @staticmethod
    def top_up_physical_card(
        client: HttpClient,
        query_params: dict | None = None,
        body: TopUpPhysicalCardEndpoint.RequestBody | None = None,
    ) -> Response:
        endpoint = TopUpPhysicalCardEndpoint(
            body=body,
            query=query_params,
        )

        response = client.request(endpoint=endpoint)

        return response

    @staticmethod
    async def top_up_physical_card_async(
        client: AsyncHttpClient,
        query_params: dict | None = None,
        body: TopUpPhysicalCardEndpoint.RequestBody | None = None,
    ) -> Response:
        endpoint = TopUpPhysicalCardEndpoint(
            body=body,
            query=query_params,
        )

        response = await client.request(endpoint=endpoint)

        return response

    @staticmethod
    def cancel_top_up_on_physical_card(
        client: HttpClient,
        query_params: dict | None = None,
        body: CancelActivatePhysicalCardEndpoint.RequestBody | None = None,
    ) -> Response:
        endpoint = CancelActivatePhysicalCardEndpoint(
            body=body,
            query=query_params,
        )

        response = client.request(endpoint=endpoint)

        return response

    @staticmethod
    async def cancel_top_up_on_physical_card_async(
        client: AsyncHttpClient,
        query_params: dict | None = None,
        body: CancelActivatePhysicalCardEndpoint.RequestBody | None = None,
    ) -> Response:
        endpoint = CancelActivatePhysicalCardEndpoint(
            body=body,
            query=query_params,
        )

        response = await client.request(endpoint=endpoint)

        return response

    @staticmethod
    def order_physical_card(
        client: HttpClient,
        query_params: dict | None = None,
        body: OrderPhysicalCardEndpoint.RequestBody | None = None,
    ) -> Response:
        endpoint = OrderPhysicalCardEndpoint(
            body=body,
            query=query_params,
        )

        response = client.request(endpoint=endpoint)

        return response

    @staticmethod
    async def order_physical_card_async(
        client: AsyncHttpClient,
        query_params: dict | None = None,
        body: OrderPhysicalCardEndpoint.RequestBody | None = None,
    ) -> Response:
        endpoint = OrderPhysicalCardEndpoint(
            body=body,
            query=query_params,
        )

        response = await client.request(endpoint=endpoint)

        return response

    @staticmethod
    def physical_card_order_status(client: HttpClient, body: PhysicalCardOrderStatusEndpoint.RequestBody):
        endpoint = PhysicalCardOrderStatusEndpoint(
            body=body,
        )

        response = client.request(endpoint=endpoint)

        return response

    @staticmethod
    async def physical_card_order_status_async(
        client: AsyncHttpClient, body: PhysicalCardOrderStatusEndpoint.RequestBody
    ):
        endpoint = PhysicalCardOrderStatusEndpoint(
            body=body,
        )

        response = await client.request(endpoint=endpoint)

        return response

    @staticmethod
    def fulfil_physical_card_order(client: HttpClient, body: FulfilPhysicalCardOrderEndpoint.RequestBody):
        endpoint = FulfilPhysicalCardOrderEndpoint(
            body=body,
        )

        response = client.request(endpoint=endpoint)

        return response

    @staticmethod
    async def fulfil_physical_card_order_async(
        client: AsyncHttpClient, body: FulfilPhysicalCardOrderEndpoint.RequestBody
    ):
        endpoint = FulfilPhysicalCardOrderEndpoint(
            body=body,
        )

        response = await client.request(endpoint=endpoint)

        return response

    @staticmethod
    def balance_check_physical(
        client: HttpClient,
        query_params: dict | None = None,
        body: BalanceCheckPhysicalEndpoint.RequestBody | None = None,
    ) -> Response:
        endpoint = BalanceCheckPhysicalEndpoint(
            body=body,
            query=query_params,
        )

        response = client.request(endpoint=endpoint)

        return response

    @staticmethod
    async def balance_check_physical_async(
        client: AsyncHttpClient,
        query_params: dict | None = None,
        body: BalanceCheckPhysicalEndpoint.RequestBody | None = None,
    ) -> Response:
        endpoint = BalanceCheckPhysicalEndpoint(
            body=body,
            query=query_params,
        )

        response = await client.request(endpoint=endpoint)

        return response
