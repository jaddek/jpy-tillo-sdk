import asyncio
import uuid

from jpy_tillo_sdk import tillo as __tillo
from jpy_tillo_sdk.domain.physical_card.endpoints import BalanceCheckPhysicalRequestBody
from jpy_tillo_sdk.domain.physical_card.shared import FaceValue
from jpy_tillo_sdk.enums import Currency

TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {}

tillo = __tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)


def balance_check_physical(_tillo) -> None:
    body = BalanceCheckPhysicalRequestBody(
        client_request_id=str(uuid.uuid4()),
        brand="costa",
        face_value=FaceValue(
            currency=Currency.GBP,
        ),
        code="ABCD12324",
        pin="",
    )

    print(_tillo.physical_card.balance_check_physical(body=body))


balance_check_physical(tillo)


async def balance_check_physical_async(_tillo) -> None:
    body = BalanceCheckPhysicalRequestBody(
        client_request_id=str(uuid.uuid4()),
        brand="costa",
        face_value=FaceValue(
            currency=Currency.GBP,
        ),
        code="ABCD12324",
        pin="",
    )

    print(await _tillo.physical_card_async.balance_check_physical_async(body=body))


asyncio.run(balance_check_physical_async())
