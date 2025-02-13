import asyncio
import uuid

from jaddek_tillo_sdk.domain.digital_card.factory import (
    create_standard_issue_request,
)
from jaddek_tillo_sdk.domain.digital_card.services import (
    IssueDigitalCodeService,
)
from jaddek_tillo_sdk import Currency
from jaddek_tillo_sdk.http_client_factory import (
    create_client,
    create_client_async,
)

TILLO_HOST = ""
TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {}


def issue_digital_code():
    sync_client = create_client(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)

    body = create_standard_issue_request(
        client_request_id=str(uuid.uuid4()),
        brand="costa",
        currency=Currency.GBP,
        amount="10",
    )

    response = IssueDigitalCodeService.issue_digital_code(sync_client, body=body)

    print(response.text)


issue_digital_code()


async def issue_digital_code_async():
    async_client = create_client_async(
        TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS
    )

    body = create_standard_issue_request(
        client_request_id=str(uuid.uuid4()),
        brand="costa",
        currency=Currency.GBP,
        amount="10",
    )

    response = await IssueDigitalCodeService.issue_digital_code_async(
        async_client, body=body
    )

    print(response.text)


asyncio.run(issue_digital_code_async())
