import asyncio
import uuid

from jpy_tillo_sdk import tillo
from jpy_tillo_sdk.domain.digital_card.factory import (
    create_standard_issue_request,
)
from jpy_tillo_sdk.enums import Currency

TILLO_HOST = ""
TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {}


def issue_digital_code():
    client = tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)

    body = create_standard_issue_request(
        client_request_id=str(uuid.uuid4()),
        brand="costa",
        currency=Currency.GBP,
        amount="10",
    )

    response = client.digital_card.issue_digital_code(body=body)

    print(response.text)


issue_digital_code()


async def issue_digital_code_async():
    client = tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)

    body = create_standard_issue_request(
        client_request_id=str(uuid.uuid4()),
        brand="costa",
        currency=Currency.GBP,
        amount="10",
    )

    response = await client.digital_card_async.order_digital_code(body=body)

    print(response.text)


asyncio.run(issue_digital_code_async())
