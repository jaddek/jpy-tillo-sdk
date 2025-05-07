import asyncio

from jpy_tillo_sdk import tillo
from jpy_tillo_sdk.domain.float.factory import create_payment_transfer_request
from jpy_tillo_sdk.enums import Currency

TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {}


async def request_payment_transfer_async():
    client = tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)

    response = await client.floats_async.request_payment_transfer_async(
        create_payment_transfer_request(
            currency=Currency.EUR,
            amount="100",
            payment_reference="ref",
            finance_email="email",
        )
    )

    print(response.text)


asyncio.run(request_payment_transfer_async())
