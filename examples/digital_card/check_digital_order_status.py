import asyncio

from jpy_tillo_sdk import tillo
from jpy_tillo_sdk.domain.digital_card.endpoints import CheckDigitalOrderStatusAsyncEndpoint

TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {"base_url": "https://sandbox.tillo.dev", "http2": True}


def check_digital_order_status():
    client = tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)

    qp = CheckDigitalOrderStatusAsyncEndpoint.QueryParams(reference="a6404b20-30a5-11f0-80b5-035a01d8c540")

    response = client.digital_card.check_digital_order(query_params=qp)

    print(response.text)


check_digital_order_status()


async def check_digital_order_status_async():
    client = tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)

    qp = CheckDigitalOrderStatusAsyncEndpoint.QueryParams(reference="a6404b20-30a5-11f0-80b5-035a01d8c540")

    response = await client.digital_card_async.check_digital_order(query_params=qp)

    print(response.text)


asyncio.run(check_digital_order_status_async())
