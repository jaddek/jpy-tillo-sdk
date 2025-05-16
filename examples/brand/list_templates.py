import asyncio

from jpy_tillo_sdk import tillo
from jpy_tillo_sdk.domain.brand.endpoints import TemplatesListEndpointRequestQuery

TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {"base_url": "https://sandbox.tillo.dev", "http2": True}


def get_brand_templates():
    client = tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)
    response = client.templates.get_templates_list(
        TemplatesListEndpointRequestQuery(
            brand="amazon-de",
        )
    )

    print(response.text)


get_brand_templates()


async def get_brand_templates_async():
    client = tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)
    response = await client.templates_async.get_brand_templates(TemplatesListEndpointRequestQuery(brand="amazon-de"))

    print(response.text)


asyncio.run(get_brand_templates_async())
