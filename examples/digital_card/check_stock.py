import asyncio

from jpy_tillo_sdk import tillo
from jpy_tillo_sdk.domain.digital_card.endpoints import CheckStockEndpoint

TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {"base_url": "https://sandbox.tillo.dev", "http2": True}


def check_stock():
    client = tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)

    qp = CheckStockEndpoint.QueryParams(brand="hello-fresh")

    response = client.digital_card.check_stock(query_params=qp)

    print(response.text)


check_stock()


async def check_stock_async():
    client = tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)

    qp = CheckStockEndpoint.QueryParams(brand="hello-fresh")

    response = client.digital_card.check_stock(query_params=qp)

    print(response.text)


asyncio.run(check_stock_async())
