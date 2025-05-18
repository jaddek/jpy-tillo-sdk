import asyncio

from jpy_tillo_sdk import tillo as __tillo
from jpy_tillo_sdk.domain.digital_card.endpoints import CheckStockRequestQuery

TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {"base_url": "https://sandbox.tillo.dev", "http2": True}

tillo = __tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)


def check_stock(_tillo):
    qp = CheckStockRequestQuery(brand="hello-fresh")

    response = _tillo.digital_card.check_stock(query=qp)

    print(response.text)


check_stock(tillo)


async def check_stock_async(_tillo):
    qp = CheckStockRequestQuery(brand="hello-fresh")

    response = _tillo.digital_card.check_stock(query=qp)

    print(response.text)


asyncio.run(check_stock_async(tillo))
