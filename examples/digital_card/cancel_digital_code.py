import asyncio

from jpy_tillo_sdk import tillo
from jpy_tillo_sdk.domain.physical_card.factory import (
    create_cancel_top_up_physical_card_request,
)
from jpy_tillo_sdk.enums import Currency, Sector

TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {"base_url": "https://sandbox.tillo.dev", "http2": True}


def cancel_digital_code():
    client = tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)

    body = create_cancel_top_up_physical_card_request(
        client_request_id="test",
        original_client_request_id="origin",
        brand="test",
        code="test",
        pin="100",
        currency=Currency.EUR,
        sector=Sector.GIFT_CARD_MALL,
        amount="100",
    )

    response = client.digital_card.cancel_digital_code(body=body)

    print(response.text)


cancel_digital_code()


async def cancel_digital_code_async():
    client = tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)

    body = create_cancel_top_up_physical_card_request(
        client_request_id="test",
        original_client_request_id="origin",
        brand="test",
        code="test",
        pin="100",
        currency=Currency.EUR,
        sector=Sector.GIFT_CARD_MALL,
        amount="100",
    )

    response = await client.digital_card_async.cancel_digital_code(body=body)

    print(response.text)


asyncio.run(cancel_digital_code_async())
