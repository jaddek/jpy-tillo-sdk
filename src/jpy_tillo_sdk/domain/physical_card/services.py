from typing import Optional

from httpx import Response

from .endpoints import (
    ActivatePhysicalCardEndpoint,
    CancelActivatePhysicalCardEndpoint,
    CashOutOriginalTransactionPhysicalCardEndpoint,
    TopUpPhysicalCardEndpoint,
    BalanceCheckPhysicalEndpoint,
    OrderPhysicalCardEndpoint,
    PhysicalCardOrderStatusEndpoint,
    FulfilPhysicalCardOrderEndpoint,
)
from ...http_client import HttpClient, AsyncHttpClient


class PhysicalGiftCardsService:
    @staticmethod
    def activate_physical_card(
        client: HttpClient,
        query_params: Optional[dict] = None,
        body: Optional[ActivatePhysicalCardEndpoint.RequestBody] = None,
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
        query_params: Optional[dict] = None,
        body: Optional[ActivatePhysicalCardEndpoint.RequestBody] = None,
    ) -> Response:
        endpoint = ActivatePhysicalCardEndpoint(body=body, query=query_params)

        response = await client.request(
            endpoint=endpoint,
        )

        return response

    @staticmethod
    def cancel_activate_physical_card(
        client: HttpClient,
        query_params: Optional[dict] = None,
        body: Optional[CancelActivatePhysicalCardEndpoint.RequestBody] = None,
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
        query_params: Optional[dict] = None,
        body: Optional[CancelActivatePhysicalCardEndpoint.RequestBody] = None,
    ) -> Response:
        endpoint = CancelActivatePhysicalCardEndpoint(body=body, query=query_params)

        response = await client.request(
            endpoint=endpoint,
        )

        return response

    @staticmethod
    def cash_out_original_transaction_physical_card(
        client: HttpClient,
        query_params: Optional[dict] = None,
        body: Optional[
            CashOutOriginalTransactionPhysicalCardEndpoint.RequestBody
        ] = None,
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
        query_params: Optional[dict] = None,
        body: Optional[
            CashOutOriginalTransactionPhysicalCardEndpoint.RequestBody
        ] = None,
    ) -> Response:
        endpoint = CashOutOriginalTransactionPhysicalCardEndpoint(
            body=body, query=query_params
        )

        response = await client.request(
            endpoint=endpoint,
        )

        return response

    @staticmethod
    def top_up_physical_card(
        client: HttpClient,
        query_params: Optional[dict] = None,
        body: Optional[TopUpPhysicalCardEndpoint.RequestBody] = None,
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
        query_params: Optional[dict] = None,
        body: Optional[TopUpPhysicalCardEndpoint.RequestBody] = None,
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
        query_params: Optional[dict] = None,
        body: Optional[CancelActivatePhysicalCardEndpoint.RequestBody] = None,
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
        query_params: Optional[dict] = None,
        body: Optional[CancelActivatePhysicalCardEndpoint.RequestBody] = None,
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
        query_params: Optional[dict] = None,
        body: Optional[OrderPhysicalCardEndpoint.RequestBody] = None,
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
        query_params: Optional[dict] = None,
        body: Optional[OrderPhysicalCardEndpoint.RequestBody] = None,
    ) -> Response:
        endpoint = OrderPhysicalCardEndpoint(
            body=body,
            query=query_params,
        )

        response = await client.request(endpoint=endpoint)

        return response

    @staticmethod
    def physical_card_order_status(
        client: HttpClient, body: PhysicalCardOrderStatusEndpoint.RequestBody
    ):
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
    def fulfil_physical_card_order(
        client: HttpClient, body: FulfilPhysicalCardOrderEndpoint.RequestBody
    ):
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
        query_params: Optional[dict] = None,
        body: Optional[BalanceCheckPhysicalEndpoint.RequestBody] = None,
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
        query_params: Optional[dict] = None,
        body: Optional[BalanceCheckPhysicalEndpoint.RequestBody] = None,
    ) -> Response:
        endpoint = BalanceCheckPhysicalEndpoint(
            body=body,
            query=query_params,
        )

        response = await client.request(endpoint=endpoint)

        return response
