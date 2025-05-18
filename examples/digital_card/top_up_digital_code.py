import asyncio

from jpy_tillo_sdk import tillo as __tillo
from jpy_tillo_sdk.domain.digital_card.endpoints import TopUpDigitalCodeRequestBody
from jpy_tillo_sdk.domain.digital_card.shared import FaceValue
from jpy_tillo_sdk.enums import Currency, Sector

TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {"base_url": "https://sandbox.tillo.dev", "http2": True}

tillo = __tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)


def top_up_digital_code(_tillo):
    body = TopUpDigitalCodeRequestBody(
        face_value=FaceValue(
            currency=Currency.EUR.value,
            amount="10",
        ),
        client_request_id="req_id",
        brand="amazon",
        code="100",
        pin="100",
        sector=Sector.GIFT_CARD_MALL.value,
    )

    response = tillo.digital_card.top_up_digital_code(body=body)

    print(response.text)


top_up_digital_code(tillo)


async def top_up_digital_code_async(_tillo):
    body = TopUpDigitalCodeRequestBody(
        face_value=FaceValue(
            currency=Currency.EUR.value,
            amount="10",
        ),
        client_request_id="req_id",
        brand="amazon",
        code="100",
        pin="100",
        sector=Sector.GIFT_CARD_MALL.value,
    )

    response = await tillo.digital_card_async.top_up_digital_code(body=body)

    print(response.text)


asyncio.run(top_up_digital_code_async(tillo))
