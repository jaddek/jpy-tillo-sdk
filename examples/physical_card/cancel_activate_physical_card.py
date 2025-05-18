import asyncio
import uuid

from jpy_tillo_sdk import tillo as __tillo
from jpy_tillo_sdk.domain.physical_card.endpoints import CancelActivateRequestBody
from jpy_tillo_sdk.domain.physical_card.shared import FaceValue
from jpy_tillo_sdk.enums import Currency, Sector

TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {}

tillo = __tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)


def cancel_activate_physical_card(_tillo) -> None:
    body = CancelActivateRequestBody(
        client_request_id=str(uuid.uuid4()),
        brand="costa",
        code="ABCD12324",
        pin="",
        face_value=FaceValue(
            currency=Currency.GBP.value,
            amount="10",
        ),
        sector=Sector.GIFT_CARD_MALL.value,
    )

    print(_tillo.physical_card.cancel_activate_physical_card(body=body))


cancel_activate_physical_card(tillo)


async def cancel_activate_physical_card_async(_tillo) -> None:
    body = CancelActivateRequestBody(
        client_request_id=str(uuid.uuid4()),
        brand="costa",
        code="ABCD12324",
        pin="",
        face_value=FaceValue(
            currency=Currency.GBP.value,
            amount="10",
        ),
        sector=Sector.GIFT_CARD_MALL.value,
    )

    print(await _tillo.physical_card_async.cancel_activate_physical_card(body=body))


asyncio.run(cancel_activate_physical_card_async(tillo))
