import asyncio
import uuid

from jpy_tillo_sdk import tillo as __tillo
from jpy_tillo_sdk.domain.physical_card.endpoints import CancelTopUpRequestBody
from jpy_tillo_sdk.domain.physical_card.shared import FaceValue
from jpy_tillo_sdk.enums import Currency, Sector

TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {}

tillo = __tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)


def cancel_top_up_physical_card(_tillo) -> None:
    body = CancelTopUpRequestBody(
        client_request_id=str(uuid.uuid4()),
        original_client_request_id=str(uuid.uuid4()),
        brand="costa",
        face_value=FaceValue(
            currency=Currency.GBP.value,
            amount="10",
        ),
        code="ABCD12324",
        pin="pin",
        sector=Sector.GIFT_CARD_MALL,
    )

    result = _tillo.physical_card.cancel_top_up(body=body)

    print(result)


cancel_top_up_physical_card(tillo)


async def cancel_top_up_physical_card_async(_tillo) -> None:
    body = CancelTopUpRequestBody(
        client_request_id=str(uuid.uuid4()),
        original_client_request_id=str(uuid.uuid4()),
        brand="costa",
        face_value=FaceValue(
            currency=Currency.GBP.value,
            amount="10",
        ),
        code="ABCD12324",
        pin="pin",
        sector=Sector.GIFT_CARD_MALL,
    )

    result = await _tillo.physical_card_async.cancel_top_up(body=body)

    print(result)


asyncio.run(cancel_top_up_physical_card_async(tillo))
