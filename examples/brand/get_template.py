import asyncio

from jpy_tillo_sdk import tillo
from jpy_tillo_sdk.domain.brand.endpoints import (
    DownloadBrandTemplateEndpointRequestQuery,
)

TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {"base_url": "https://sandbox.tillo.dev", "http2": True}


def get_brand_template():
    client = tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)
    client.templates.download_brand_template(
        DownloadBrandTemplateEndpointRequestQuery(brand="amazon-de", template="default")
    )

    print("Template comes here as a zip file")


get_brand_template()


async def get_brand_template_async():
    client = tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)
    await client.templates_async.download_brand_template(
        DownloadBrandTemplateEndpointRequestQuery(brand="amazon-de", template="default")
    )

    print("Template comes here as a zip file")


asyncio.run(get_brand_template_async())
