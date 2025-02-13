import asyncio
import uuid

from httpx import Response

from jpy_tillo_sdk.domain.physical_card.factory import (
    create_cancel_top_up_physical_card_request,
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


def cancel_top_up_physical_card() -> Response:
    sync_client = create_client(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)

    body = create_cancel_top_up_physical_card_request(
        client_request_id=str(uuid.uuid4()),
        original_client_request_id=str(uuid.uuid4()),
        brand="costa",
        code="ABCD12324",
        pin="",
        currency=Currency.GBP,
        amount="10",
    )

    return PhysicalGiftCardsService.cancel_top_up_on_physical_card(
        client=sync_client, body=body
    )


print(cancel_top_up_physical_card().json())


async def cancel_top_up_physical_card_async() -> Response:
    async_client = create_client_async(
        TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS
    )

    body = create_cancel_top_up_physical_card_request(
        client_request_id=str(uuid.uuid4()),
        original_client_request_id=str(uuid.uuid4()),
        brand="costa",
        code="ABCD12324",
        currency=Currency.GBP,
        amount="10",
        pin="",
    )

    return await PhysicalGiftCardsService.cancel_top_up_on_physical_card_async(
        client=async_client, body=body
    )


asyncio.run(cancel_top_up_physical_card_async())
