import asyncio
import uuid

from httpx import Response

from jpy_tillo_sdk.domain.physical_card.factory import (
    create_order_new_card_request,
)
from jpy_tillo_sdk.domain.physical_card.services import (
    PhysicalGiftCardsService,
)
from jpy_tillo_sdk.http_client_factory import (
    create_client,
    create_client_async,
)

TILLO_HOST = ""
TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {}

TILLO_API_KEY = "531f9263eede2f86a944aea966b71624c6abaa5f8b6d292f082146eb2e1e48bd"
TILLO_SECRET = "18420be9a3eeca4012229277cb60b3c9afbaa0190e0d72ee1c9046fa88086d0e"
TILLO_HTTP_CLIENT_OPTIONS = {"base_url": "https://sandbox.tillo.dev", "http2": True}


def order_physical_card() -> Response:
    sync_client = create_client(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)

    body = create_order_new_card_request(client_request_id=str(uuid.uuid4()), brand="amazon-de", amount="100", tags=[])

    return PhysicalGiftCardsService.cash_out_original_transaction_physical_card(client=sync_client, body=body)


print(order_physical_card().json())


async def order_physical_card_async() -> Response:
    async_client = create_client_async(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)

    body = create_order_new_card_request(
        client_request_id=str(uuid.uuid4()),
        brand="costa",
        amount="100",
    )

    return await PhysicalGiftCardsService.cash_out_original_transaction_physical_card_async(
        client=async_client, body=body
    )


asyncio.run(order_physical_card_async())
