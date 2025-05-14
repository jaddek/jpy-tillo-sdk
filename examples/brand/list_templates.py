import asyncio

from jpy_tillo_sdk import tillo
from jpy_tillo_sdk.domain.brand.factory import create_brand_template_list_query_params

TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {"base_url": "https://sandbox.tillo.dev", "http2": True}


def get_brand_templates():
    client = tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)
    params = create_brand_template_list_query_params()
    response = client.templates.get_brand_templates(params)

    print(response.text)


get_brand_templates()


async def get_brand_templates_async():
    client = tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)
    params = create_brand_template_list_query_params()
    response = await client.templates_async.get_brand_templates(params)

    print(response.text)


asyncio.run(get_brand_templates_async())
