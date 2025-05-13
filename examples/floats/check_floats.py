import asyncio

from jpy_tillo_sdk import tillo
from jpy_tillo_sdk.domain.float.endpoints import CheckFloatsEndpoint

TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {}


def check_floats():
    client = tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)
    params = CheckFloatsEndpoint.QueryParams()
    response = client.floats.check_floats(params)

    print(response.text)


async def check_floats_async():
    client = tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)
    params = CheckFloatsEndpoint.QueryParams()
    response = await client.floats_async.check_floats(params)

    print(response.text)


asyncio.run(check_floats_async())
