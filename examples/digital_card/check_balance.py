import asyncio

from jpy_tillo_sdk import tillo
from jpy_tillo_sdk.domain.physical_card.factory import create_balance_check_request
from jpy_tillo_sdk.enums import Currency, Sector

TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {"base_url": "https://sandbox.tillo.dev", "http2": True}


def check_balance():
    client = tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)

    body = create_balance_check_request(
        client_request_id="5434",
        brand="amazon-de",
        code="test",
        pin="100",
        currency=Currency.EUR,
        sector=Sector.GIFT_CARD_MALL,
    )

    response = client.digital_card.check_balance(body=body)

    print(response.text)


check_balance()


async def check_balance_async():
    client = tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)

    body = create_balance_check_request(
        client_request_id="test",
        brand="test",
        code="test",
        pin="100",
        currency=Currency.EUR,
        sector=Sector.GIFT_CARD_MALL,
    )

    response = await client.digital_card_async.check_balance(body=body)

    print(response.text)


asyncio.run(check_balance_async())
