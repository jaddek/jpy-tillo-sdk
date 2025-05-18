import asyncio
import uuid

from jpy_tillo_sdk import tillo as __tillo
from jpy_tillo_sdk.domain.digital_card.endpoints import IssueDigitalCodeRequestBody, OrderDigitalCodeAsyncRequestBody
from jpy_tillo_sdk.domain.digital_card.shared import FaceValue
from jpy_tillo_sdk.enums import Currency, DeliveryMethod, FulfilmentType, Sector

TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {"base_url": "https://sandbox.tillo.dev", "http2": True}

tillo = __tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)


def order_digital_code(_tillo):
    body = OrderDigitalCodeAsyncRequestBody(
        client_request_id=str(uuid.uuid4()),
        brand="costa",
        face_value=FaceValue(
            currency=Currency.GBP.value,
            amount="100",
        ),
        sector=Sector.GIFT_CARD_MALL.value,
        delivery_method=DeliveryMethod.URL.value,
        fulfilment_by=FulfilmentType.PARTNER.value,
    )

    response = _tillo.digital_card.order_digital_code(body=body)

    print(response.text)


order_digital_code(tillo)


async def order_digital_code_async(_tillo):
    body = IssueDigitalCodeRequestBody(
        client_request_id=str(uuid.uuid4()),
        brand="costa",
        face_value=FaceValue(
            currency=Currency.GBP.value,
            amount="100",
        ),
        sector=Sector.GIFT_CARD_MALL.value,
        delivery_method=DeliveryMethod.URL.value,
        fulfilment_by=FulfilmentType.PARTNER.value,
    )

    response = await _tillo.digital_card_async.order_digital_code(body=body)

    print(response.text)


asyncio.run(order_digital_code_async(tillo))
