import asyncio

from jpy_tillo_sdk import tillo
from jpy_tillo_sdk.domain.brand.factory import create_brands_query_params

TILLO_HOST = ""
TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {}


def get_available_brands():
    client = tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)
    params = create_brands_query_params()
    response = client.brands.get_available_brands(params)

    print(response.text)


get_available_brands()


async def get_available_brands_async():
    client = tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)
    params = create_brands_query_params()
    response = await client.brands_async.get_available_brands(params)

    print(response.text)


asyncio.run(get_available_brands_async())
