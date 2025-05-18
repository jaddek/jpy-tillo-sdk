import asyncio

from jpy_tillo_sdk import tillo as __tillo
from jpy_tillo_sdk.domain.brand.endpoints import BrandEndpointRequestQuery

TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {}

tillo = __tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)


def get_available_brands(_tillo):
    response = _tillo.brands.get_available_brands(BrandEndpointRequestQuery(brand="amazon-de"))

    print(response.text)


get_available_brands(tillo)


async def get_available_brands_async(_tillo):
    response = await _tillo.brands_async.get_available_brands(BrandEndpointRequestQuery(brand="amazon-de"))

    print(response.text)

    await _tillo.close_async()


asyncio.run(get_available_brands_async(tillo))
