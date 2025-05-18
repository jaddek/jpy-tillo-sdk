import asyncio

from jpy_tillo_sdk import tillo as __tillo
from jpy_tillo_sdk.domain.physical_card.endpoints import PhysicalCardOrderStatusRequestBody

TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {}

tillo = __tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)


def physical_card_order_status(_tillo) -> None:
    result = tillo.physical_card.order_status(PhysicalCardOrderStatusRequestBody(references=["some reference"]))

    print(result.json())


physical_card_order_status(_tillo=tillo)


async def physical_card_order_status_async(_tillo) -> None:
    result = await tillo.physical_card_async.order_status_async(
        PhysicalCardOrderStatusRequestBody(references=["some reference"])
    )

    print(result.json())


asyncio.run(physical_card_order_status_async(tillo))
