import asyncio
import uuid

from jpy_tillo_sdk import tillo as __tillo
from jpy_tillo_sdk.domain.digital_card.shared import FaceValue
from jpy_tillo_sdk.domain.physical_card.endpoints import ActivatePhysicalCardERequestBody
from jpy_tillo_sdk.enums import Currency, Sector

TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {"base_url": "https://sandbox.tillo.dev", "http2": True}

tillo = __tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)


def activate_physical_card(_tillo) -> None:
    body = ActivatePhysicalCardERequestBody(
        face_value=FaceValue(
            currency=Currency.GBP.value,
            amount="10",
        ),
        sector=Sector.GIFT_CARD_MALL,
        client_request_id=str(uuid.uuid4()),
        brand="costa",
        code="ABCD12324",
        pin="",
    )

    print(_tillo.physical_card.activate_physical_card(body=body))


activate_physical_card(tillo)


async def activate_physical_card_async(_tillo):
    body = ActivatePhysicalCardERequestBody(
        face_value=FaceValue(
            currency=Currency.GBP.value,
            amount="10",
        ),
        sector=Sector.GIFT_CARD_MALL,
        client_request_id=str(uuid.uuid4()),
        brand="costa",
        code="ABCD12324",
        pin="",
    )

    print(_tillo.physical_card_async.activate_physical_card(body=body))


asyncio.run(activate_physical_card_async(tillo))
