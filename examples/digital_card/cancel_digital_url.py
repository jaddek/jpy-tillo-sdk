import asyncio

from jpy_tillo_sdk import tillo as __tillo
from jpy_tillo_sdk.domain.digital_card.endpoints import CancelDigitalUrlRequestBody
from jpy_tillo_sdk.domain.digital_card.shared import FaceValue
from jpy_tillo_sdk.enums import Currency, Sector

TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {"base_url": "https://sandbox.tillo.dev", "http2": True}

tillo = __tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)


def cancel_digital_url(_tillo) -> None:
    body = CancelDigitalUrlRequestBody(
        client_request_id="test",
        original_client_request_id="origin",
        brand="test",
        sector=Sector.GIFT_CARD_MALL.value,
        face_value=FaceValue(
            currency=Currency.EUR.value,
            amount="100",
        ),
    )

    response = _tillo.digital_card.cancel_digital_url(body=body)

    print(response.text)


cancel_digital_url(tillo)


async def cancel_digital_url_async(_tillo) -> None:
    body = CancelDigitalUrlRequestBody(
        client_request_id="test",
        original_client_request_id="origin",
        brand="test",
        sector=Sector.GIFT_CARD_MALL.value,
        face_value=FaceValue(
            currency=Currency.EUR.value,
            amount="100",
        ),
    )

    response = await _tillo.digital_card_async.cancel_digital_url(body=body)

    print(response.text)


asyncio.run(cancel_digital_url_async(tillo))
