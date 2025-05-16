import asyncio

from jpy_tillo_sdk import tillo as __tillo
from jpy_tillo_sdk.domain.brand.endpoints import (
    DownloadBrandTemplateEndpointRequestQuery,
)

TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {"base_url": "https://sandbox.tillo.dev", "http2": True}

tillo = __tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)


def get_brand_template(tillo):
    tillo.templates.download_brand_template(
        DownloadBrandTemplateEndpointRequestQuery(brand="amazon-de", template="default")
    )

    print("Template comes here as a zip file")


get_brand_template(tillo)


async def get_brand_template_async(tillo):
    await tillo.templates_async.download_brand_template(
        DownloadBrandTemplateEndpointRequestQuery(brand="amazon-de", template="default")
    )

    print("Template comes here as a zip file")


asyncio.run(get_brand_template_async(tillo))
