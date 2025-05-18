import asyncio

from jpy_tillo_sdk import tillo as __tillo
from jpy_tillo_sdk.domain.digital_card.endpoints import CancelDigitalCodeRequestBody
from jpy_tillo_sdk.domain.digital_card.shared import FaceValue
from jpy_tillo_sdk.enums import Currency, Sector

TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {"base_url": "https://sandbox.tillo.dev", "http2": True}


tillo = __tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)


def cancel_digital_code(_tillo):
    body = CancelDigitalCodeRequestBody(
        client_request_id="test",
        original_client_request_id="origin",
        brand="test",
        code="test",
        face_value=FaceValue(
            currency=Currency.EUR.value,
            amount="100",
        ),
        sector=Sector.GIFT_CARD_MALL.value,
    )

    response = _tillo.digital_card.cancel_digital_code(body=body)

    print(response.text)


cancel_digital_code(tillo)


async def cancel_digital_code_async(_tillo):
    body = CancelDigitalCodeRequestBody(
        client_request_id="test",
        original_client_request_id="origin",
        brand="test",
        code="test",
        face_value=FaceValue(
            currency=Currency.EUR.value,
            amount="100",
        ),
        sector=Sector.GIFT_CARD_MALL.value,
    )

    response = await _tillo.digital_card_async.cancel_digital_code(body=body)

    print(response.text)


asyncio.run(cancel_digital_code_async(tillo))
