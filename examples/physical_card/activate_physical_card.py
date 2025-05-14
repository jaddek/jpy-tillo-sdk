import asyncio
import uuid

from jpy_tillo_sdk.domain.physical_card.factory import (
    create_activate_physical_card_request,
)
from jpy_tillo_sdk.domain.physical_card.services import (
    PhysicalGiftCardsService,
)
from jpy_tillo_sdk.enums import Currency
from jpy_tillo_sdk.http_client_factory import (
    create_client,
    create_client_async,
)

TILLO_API_KEY = "531f9263eede2f86a944aea966b71624c6abaa5f8b6d292f082146eb2e1e48bd"
TILLO_SECRET = "18420be9a3eeca4012229277cb60b3c9afbaa0190e0d72ee1c9046fa88086d0e"
TILLO_HTTP_CLIENT_OPTIONS = {"base_url": "https://sandbox.tillo.dev", "http2": True}


def activate_physical_card():
    sync_client = create_client(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)

    body = create_activate_physical_card_request(
        client_request_id=str(uuid.uuid4()),
        brand="costa",
        currency=Currency.GBP,
        amount="10",
        code="ABCD12324",
        pin="",
    )

    return PhysicalGiftCardsService.activate_physical_card(client=sync_client, body=body)


print(activate_physical_card().json())


async def activate_physical_card_async():
    async_client = create_client_async(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)

    body = create_activate_physical_card_request(
        client_request_id=str(uuid.uuid4()),
        brand="costa",
        currency=Currency.GBP,
        amount="10",
        code="ABCD12324",
        pin="",
    )

    return await PhysicalGiftCardsService.activate_physical_card_async(client=async_client, body=body)


asyncio.run(activate_physical_card_async())
