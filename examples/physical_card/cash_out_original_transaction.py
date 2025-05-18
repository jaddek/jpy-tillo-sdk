import asyncio
import uuid

from jpy_tillo_sdk import tillo as __tillo
from jpy_tillo_sdk.domain.physical_card.endpoints import CashOutOriginalTransactionRequestBody
from jpy_tillo_sdk.enums import Sector

TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {}

tillo = __tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)


def cancel_activate_physical_card(_tillo) -> None:
    body = CashOutOriginalTransactionRequestBody(
        client_request_id=str(uuid.uuid4()),
        original_client_request_id=str(uuid.uuid4()),
        brand="costa",
        code="ABCD12324",
        pin="1234",
        sector=Sector.GIFT_CARD_MALL.value,
    )

    result = tillo.physical_card.cash_out_original_transaction(body=body)

    print(result)


cancel_activate_physical_card(tillo)


async def cancel_activate_physical_card_async(_tillo) -> None:
    body = CashOutOriginalTransactionRequestBody(
        client_request_id=str(uuid.uuid4()),
        original_client_request_id=str(uuid.uuid4()),
        brand="costa",
        code="ABCD12324",
        pin="1234",
        sector=Sector.GIFT_CARD_MALL.value,
    )

    result = tillo.physical_card.cash_out_original_transaction(body=body)

    print(result)


asyncio.run(cancel_activate_physical_card_async(tillo))
