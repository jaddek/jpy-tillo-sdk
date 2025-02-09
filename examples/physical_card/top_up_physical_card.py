import asyncio
import uuid

from httpx import Response

from jaddek_tillo_sdk.domain.physical_card.factory import (
    create_top_up_physical_card_request,
)
from jaddek_tillo_sdk.domain.physical_card.services import (
    PhysicalGiftCardsService,
)
from jaddek_tillo_sdk.enums import Currency
from jaddek_tillo_sdk.http_client_factory import (
    create_client,
    create_client_async,
)

TILLO_HOST = ""
TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {}


def top_up_physical_card() -> Response:
    sync_client = create_client(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)

    body = create_top_up_physical_card_request(
        client_request_id=str(uuid.uuid4()),
        brand="costa",
        currency=Currency.GBP,
        amount="10",
        code="ABCD12324",
        pin="",
    )

    return PhysicalGiftCardsService.top_up_physical_card(client=sync_client, body=body)


print(top_up_physical_card().json())


async def top_up_physical_card_async() -> Response:
    async_client = create_client_async(
        TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS
    )

    body = create_top_up_physical_card_request(
        client_request_id=str(uuid.uuid4()),
        brand="costa",
        currency=Currency.GBP,
        amount="10",
        code="ABCD12324",
        pin="",
    )

    return await PhysicalGiftCardsService.top_up_physical_card_async(
        client=async_client, body=body
    )


asyncio.run(top_up_physical_card_async())
