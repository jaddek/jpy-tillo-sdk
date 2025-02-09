import asyncio
import uuid

from httpx import Response

from jaddek_tillo_sdk.domain.physical_card.factory import (
    create_fulfil_physical_card_order_request,
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


def physical_card_fulfil_order() -> Response:
    sync_client = create_client(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)

    body = create_fulfil_physical_card_order_request(
        client_request_id=str(uuid.uuid4()),
        brand="costa",
        code="1234",
        amount="100",
        reference="some reference",
    )

    return PhysicalGiftCardsService.fulfil_physical_card_order(sync_client, body)


print(physical_card_fulfil_order().json())


async def physical_card_fulfil_order_async() -> Response:
    async_client = create_client_async(
        TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS
    )

    body = create_fulfil_physical_card_order_request(
        client_request_id=str(uuid.uuid4()),
        brand="costa",
        code="1234",
        amount="100",
        reference="some reference",
    )

    return await PhysicalGiftCardsService.fulfil_physical_card_order_async(
        client=async_client, body=body
    )


asyncio.run(physical_card_fulfil_order_async())
