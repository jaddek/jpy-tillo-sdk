import asyncio

from jpy_tillo_sdk import tillo

TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {}


async def check_floats_async():
    client = tillo.TilloClient(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)

    response = await client.floats_async.check_floats_async()

    print(response.text)


asyncio.run(check_floats_async())
