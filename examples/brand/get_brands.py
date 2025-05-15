import asyncio

from jpy_tillo_sdk import tillo

TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {}


def get_available_brands():
    client = tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)
    response = client.brands.get_available_brands(client.brands_async.get_available_brands_query())

    print(response.text)


get_available_brands()


async def get_available_brands_async():
    client = tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)
    response = await client.brands_async.get_available_brands_async(client.brands_async.get_available_brands_query())

    print(response.text)


asyncio.run(get_available_brands_async())
