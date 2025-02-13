import asyncio
import uuid

from jpy_tillo_sdk.domain.physical_card.factory import (
    create_activate_physical_card_request,
)
from jpy_tillo_sdk.domain.physical_card.services import (
    PhysicalGiftCardsService,
)
from jpy_tillo_sdk import Currency
from jpy_tillo_sdk.http_client_factory import (
    create_client,
    create_client_async,
)

TILLO_HOST = ""
TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {}


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

    return PhysicalGiftCardsService.activate_physical_card(
        client=sync_client, body=body
    )


print(activate_physical_card().json())


async def activate_physical_card_async():
    async_client = create_client_async(
        TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS
    )

    body = create_activate_physical_card_request(
        client_request_id=str(uuid.uuid4()),
        brand="costa",
        currency=Currency.GBP,
        amount="10",
        code="ABCD12324",
        pin="",
    )

    return await PhysicalGiftCardsService.activate_physical_card_async(
        client=async_client, body=body
    )


asyncio.run(activate_physical_card_async())
