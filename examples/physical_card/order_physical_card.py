import asyncio
import uuid

from jpy_tillo_sdk import tillo as __tillo
from jpy_tillo_sdk.domain.physical_card.endpoints import OrderPhysicalCardRequestBody
from jpy_tillo_sdk.domain.physical_card.shared import FaceValue
from jpy_tillo_sdk.enums import Currency

TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {}

tillo = __tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)


def order_physical_card(_tillo) -> None:
    result = _tillo.physical_card.order_physical_card(
        body=OrderPhysicalCardRequestBody(
            client_request_id=str(uuid.uuid4()),
            brand="amazon-de",
            face_value=FaceValue(currency=Currency.EUR, amount="100"),
        )
    )

    print(result)


order_physical_card(tillo)


async def order_physical_card_async(_tillo) -> None:
    result = await _tillo.physical_card_async.order_physical_card(
        body=OrderPhysicalCardRequestBody(
            client_request_id=str(uuid.uuid4()),
            brand="amazon-de",
            face_value=FaceValue(currency=Currency.EUR, amount="100"),
        )
    )

    print(result)


asyncio.run(order_physical_card_async(tillo))
