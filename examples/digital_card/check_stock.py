import asyncio

from jpy_tillo_sdk import tillo

TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {"base_url": "https://sandbox.tillo.dev", "http2": True}


def check_stock():
    client = tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)

    response = client.digital_card.check_stock()

    print(response.text)


check_stock()


async def check_stock_async():
    client = tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)

    response = await client.digital_card_async.check_stock()

    print(response.text)


asyncio.run(check_stock_async())
