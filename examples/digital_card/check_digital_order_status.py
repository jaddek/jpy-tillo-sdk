import asyncio

from jpy_tillo_sdk import tillo

TILLO_HOST = ""
TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {}


def check_digital_order_status():
    client = tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)

    response = client.digital_card.check_digital_order(query_params={"reference": "ref"})

    print(response.text)


check_digital_order_status()


async def check_digital_order_status_async():
    client = tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)

    response = await client.digital_card_async.check_digital_order(query_params={"reference": "ref"})

    print(response.text)


asyncio.run(check_digital_order_status_async())
