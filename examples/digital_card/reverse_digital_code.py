import asyncio

from jpy_tillo_sdk import tillo

TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {"base_url": "https://sandbox.tillo.dev", "http2": True}


def reverse_digital_code():
    client = tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)

    response = client.digital_card.reverse_digital_code()

    print(response.text)


reverse_digital_code()


async def reverse_digital_code_async():
    client = tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)

    response = await client.digital_card_async.reverse_digital_code()

    print(response.text)


asyncio.run(reverse_digital_code_async())
