import asyncio
import uuid

from httpx import Response

from jpy_tillo_sdk import tillo as __tillo
from jpy_tillo_sdk.domain.physical_card.endpoints import TopUpPhysicalCardRequestBody
from jpy_tillo_sdk.domain.physical_card.shared import FaceValue
from jpy_tillo_sdk.enums import Currency, Sector

TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {}

tillo = __tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)


def top_up_physical_card(_tillo) -> Response:
    body = TopUpPhysicalCardRequestBody(
        client_request_id=(uuid.uuid4()),
        brand="h-and-m",
        face_value=FaceValue(
            currency=Currency.GBP,
            amount="100",
        ),
        code="1234",
        pin="1234",
        sector=Sector.GIFT_CARD_MALL,
    )

    return _tillo.physical_card.top_up_physical_card(body=body)


top_up_physical_card(tillo)


async def top_up_physical_card_async(_tillo) -> Response:
    body = TopUpPhysicalCardRequestBody(
        client_request_id=str(uuid.uuid4()),
        brand="h-and-m",
        face_value=FaceValue(
            currency=Currency.GBP,
            amount="100",
        ),
        code="1234",
        pin="1234",
        sector=Sector.GIFT_CARD_MALL,
    )

    return await _tillo.physical_card_async.top_up_physical_card_async(body=body)


asyncio.run(top_up_physical_card_async(tillo))
