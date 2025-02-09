import asyncio

from jaddek_tillo_sdk.domain.float.services import FloatService
from jaddek_tillo_sdk.http_client_factory import (
    create_client,
    create_client_async,
)

TILLO_HOST = ""
TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {}


def check_floats():
    sync_client = create_client(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)

    response = FloatService.check_floats(sync_client)

    print(response.text)


check_floats()


async def check_floats_async():
    async_client = create_client_async(
        TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS
    )

    response = await FloatService.check_floats_async(async_client)

    print(response.text)


asyncio.run(check_floats_async())
