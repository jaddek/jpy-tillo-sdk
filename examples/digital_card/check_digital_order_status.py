import asyncio

from jpy_tillo_sdk import tillo as __tillo
from jpy_tillo_sdk.domain.digital_card.endpoints import (
    CheckDigitalOrderStatusAsyncRequestQuery,
)

TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {"base_url": "https://sandbox.tillo.dev", "http2": True}

tillo = __tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)


def check_digital_order_status(_tillo):
    qp = CheckDigitalOrderStatusAsyncRequestQuery(reference="a6404b20-30a5-11f0-80b5-035a01d8c540")

    response = _tillo.digital_card.check_digital_order(query=qp)

    print(response.text)


check_digital_order_status(tillo)


async def check_digital_order_status_async(_tillo):
    qp = CheckDigitalOrderStatusAsyncRequestQuery(reference="a6404b20-30a5-11f0-80b5-035a01d8c540")

    response = await _tillo.digital_card_async.check_digital_order(query=qp)

    print(response.text)


asyncio.run(check_digital_order_status_async(tillo))
