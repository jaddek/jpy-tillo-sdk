import asyncio
import uuid

from jpy_tillo_sdk import tillo as __tillo
from jpy_tillo_sdk.domain.physical_card.endpoints import FulfilPhysicalCardOrderEndpointRequestBody
from jpy_tillo_sdk.domain.physical_card.shared import FaceValue
from jpy_tillo_sdk.enums import Currency

TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {}

tillo = __tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)


def physical_card_fulfil_order(_tillo) -> None:
    body = FulfilPhysicalCardOrderEndpointRequestBody(
        client_request_id=str(uuid.uuid4()),
        brand="costa",
        code="1234",
        face_value=FaceValue(
            currency=Currency.EUR.value,
            amount="100",
        ),
        reference="some reference",
    )

    result = _tillo.physical_card.fulfil_order(body)

    print(result)


physical_card_fulfil_order(tillo)


async def physical_card_fulfil_order_async(_tillo) -> None:
    body = FulfilPhysicalCardOrderEndpointRequestBody(
        client_request_id=str(uuid.uuid4()),
        brand="costa",
        code="1234",
        face_value=FaceValue(
            currency=Currency.EUR.value,
            amount="100",
        ),
        reference="some reference",
    )

    result = await _tillo.physical_card_async.fulfil_order(body)

    print(result)


asyncio.run(physical_card_fulfil_order_async(tillo))
