import asyncio

from jaddek_tillo_sdk.domain.brand.services import BrandService
from jaddek_tillo_sdk.http_client_factory import (
    create_client_async,
    create_client,
)

TILLO_HOST = ""
TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {}


def get_brand_templates():
    sync_client = create_client(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)

    response = BrandService.get_brand_templates(sync_client)

    print(response.text)


get_brand_templates()


async def get_brand_templates_async():
    async_client = create_client_async(
        TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS
    )

    response = await BrandService.get_brand_templates_async(async_client)

    print(response.text)


asyncio.run(get_brand_templates_async())
