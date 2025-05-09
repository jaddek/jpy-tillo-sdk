import asyncio
import logging

from jpy_tillo_sdk import tillo
from jpy_tillo_sdk.domain.float.factory import create_payment_transfer_request
from jpy_tillo_sdk.enums import Currency

TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {}

logging.basicConfig(level=logging.DEBUG)


def request_payment_transfer():
    client = tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)

    response = client.floats.request_payment_transfer(
        create_payment_transfer_request(
            transfer_float=Currency.UNIVERSAL_FLOAT.value,
            currency=Currency.GBP.value,
            amount=100.00,
            payment_reference="OUR_REF",
            finance_email="test@payment.com",
        )
    )

    print(response.text)


async def request_payment_transfer_async():
    client = tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)

    response = await client.floats_async.request_payment_transfer_async(
        create_payment_transfer_request(
            transfer_float=Currency.UNIVERSAL_FLOAT.value,
            currency=Currency.GBP.value,
            amount=100.00,
            payment_reference="OUR_REF",
            finance_email="test@payment.com",
        )
    )

    print(response.text)


asyncio.run(request_payment_transfer_async())
