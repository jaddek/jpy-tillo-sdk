import asyncio

from jpy_tillo_sdk import tillo as __tillo
from jpy_tillo_sdk.domain.brand.endpoints import TemplatesListEndpointRequestQuery

TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {"base_url": "https://sandbox.tillo.dev", "http2": True}

tillo = __tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)


def get_brand_templates(tillo):
    response = tillo.templates.get_templates_list(
        TemplatesListEndpointRequestQuery(
            brand="amazon-de",
        )
    )

    print(response.text)


get_brand_templates(tillo)


async def get_brand_templates_async(tillo):
    response = await tillo.templates_async.get_brand_templates(TemplatesListEndpointRequestQuery(brand="amazon-de"))

    print(response.text)


asyncio.run(get_brand_templates_async())
