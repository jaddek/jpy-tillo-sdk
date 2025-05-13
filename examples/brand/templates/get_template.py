import asyncio

from jpy_tillo_sdk import tillo
from jpy_tillo_sdk.domain.brand.factory import create_brand_template_query_params

TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {}


def get_brand_template():
    client = tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)
    params = create_brand_template_query_params()
    response = client.templates.download_brand_template(params)

    print(response.text)


get_brand_template()


async def get_brand_template_async():
    client = tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)
    params = create_brand_template_query_params()
    response = await client.templates_async.download_brand_template(params)

    print(response.text)


asyncio.run(get_brand_template_async())
