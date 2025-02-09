import asyncio
import uuid

from httpx import Response

from jaddek_tillo_sdk.domain.physical_card.factory import (
    create_order_new_card_request,
    create_order_status_request,
)
from jaddek_tillo_sdk.domain.physical_card.services import (
    PhysicalGiftCardsService,
)
from jaddek_tillo_sdk.http_client_factory import (
    create_client,
    create_client_async,
)

TILLO_HOST = ""
TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {}


def physical_card_order_status() -> Response:
    sync_client = create_client(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)

    body = create_order_new_card_request(
        client_request_id=str(uuid.uuid4()),
        brand="costa",
        amount="100",
    )

    return PhysicalGiftCardsService.physical_card_order_status(sync_client, body)


print(physical_card_order_status().json())


async def physical_card_order_status_async() -> Response:
    async_client = create_client_async(
        TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS
    )

    body = create_order_status_request(
        references=["some reference"],
    )

    return await PhysicalGiftCardsService.physical_card_order_status_async(
        client=async_client, body=body
    )


asyncio.run(physical_card_order_status_async())
