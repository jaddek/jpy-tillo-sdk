import asyncio

from jpy_tillo_sdk import tillo as __tillo

TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {"base_url": "https://sandbox.tillo.dev", "http2": True}

tillo = __tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)


def reverse_digital_code(_tillo):
    response = _tillo.digital_card.reverse_digital_code()

    print(response.text)


reverse_digital_code(tillo)


async def reverse_digital_code_async(_tillo):
    response = await _tillo.digital_card_async.reverse_digital_code()

    print(response.text)


asyncio.run(reverse_digital_code_async(tillo))
