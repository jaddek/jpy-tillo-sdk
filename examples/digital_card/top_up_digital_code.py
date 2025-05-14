import asyncio

from jpy_tillo_sdk import tillo
from jpy_tillo_sdk.domain.physical_card.factory import (
    create_top_up_physical_card_request,
)
from jpy_tillo_sdk.enums import Currency, Sector

TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {"base_url": "https://sandbox.tillo.dev", "http2": True}


def topup_digital_code():
    client = tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)

    body = create_top_up_physical_card_request(
        client_request_id="req_id",
        brand="amazon",
        amount="100",
        code="100",
        pin="100",
        currency=Currency.EUR,
        sector=Sector.GIFT_CARD_MALL.value,
    )

    response = client.digital_card.top_up_digital_code(body=body)

    print(response.text)


topup_digital_code()


async def topup_digital_code_async():
    client = tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)

    body = create_top_up_physical_card_request(
        client_request_id="req_id",
        brand="amazon",
        amount="100",
        code="100",
        pin="100",
        currency=Currency.EUR,
        sector=Sector.GIFT_CARD_MALL.value,
    )

    response = await client.digital_card_async.top_up_digital_code(body=body)

    print(response.text)


asyncio.run(topup_digital_code_async())
