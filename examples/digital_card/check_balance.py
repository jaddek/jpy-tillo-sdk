import asyncio

from jpy_tillo_sdk import tillo as __tillo
from jpy_tillo_sdk.domain.digital_card.shared import FaceValue
from jpy_tillo_sdk.domain.physical_card.endpoints import BalanceCheckPhysicalRequestBody
from jpy_tillo_sdk.enums import Currency, Sector

TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {"base_url": "https://sandbox.tillo.dev", "http2": True}

tillo = __tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)


def check_balance(_tillo):
    body = BalanceCheckPhysicalRequestBody(
        client_request_id="5434",
        brand="amazon-de",
        code="test",
        pin="100",
        sector=Sector.GIFT_CARD_MALL,
        face_value=FaceValue(
            currency=Currency.EUR.value,
        ),
    )

    response = _tillo.digital_card.check_balance(body=body)

    print(response.text)


check_balance(tillo)


async def check_balance_async(_tillo):
    body = BalanceCheckPhysicalRequestBody(
        client_request_id="5434",
        brand="amazon-de",
        code="test",
        pin="100",
        sector=Sector.GIFT_CARD_MALL,
        face_value=FaceValue(
            currency=Currency.EUR.value,
        ),
    )

    response = await _tillo.digital_card_async.check_balance(body=body)

    print(response.text)


asyncio.run(check_balance_async(tillo))
