import asyncio

from jpy_tillo_sdk import tillo as __tillo
from jpy_tillo_sdk.domain.float.endpoints import CheckFloatsEndpointRequestQuery

TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {}


tillo = __tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)


def check_floats(_tillo):
    response = _tillo.floats.check_floats(CheckFloatsEndpointRequestQuery())

    print(response.text)


check_floats(tillo)


async def check_floats_async(_tillo):
    response = await _tillo.floats_async.check_floats(CheckFloatsEndpointRequestQuery())

    print(response.text)


asyncio.run(check_floats_async(tillo))

tillo.close_sync()
asyncio.run(tillo.close_async())
