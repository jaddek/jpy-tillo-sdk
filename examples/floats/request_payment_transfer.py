import asyncio
import logging

from jpy_tillo_sdk import tillo as __tillo
from jpy_tillo_sdk.domain.float.endpoints import RequestPaymentTransferEndpointRequestBody
from jpy_tillo_sdk.enums import Currency

TILLO_API_KEY = ""
TILLO_SECRET = ""
TILLO_HTTP_CLIENT_OPTIONS = {}

logging.basicConfig(level=logging.DEBUG)

tillo = __tillo.Tillo(TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS)


def request_payment_transfer(_tillo):
    response = _tillo.floats.request_payment_transfer(
        RequestPaymentTransferEndpointRequestBody(
            float=Currency.UNIVERSAL_FLOAT.value,
            currency=Currency.GBP.value,
            amount="100",
            payment_reference="OUR_REF",
            finance_email="test@payment.com",
        )
    )

    print(response.text)


request_payment_transfer(tillo)


async def request_payment_transfer_async(_tillo):
    response = await _tillo.floats_async.request_payment_transfer(
        RequestPaymentTransferEndpointRequestBody(
            float=Currency.UNIVERSAL_FLOAT.value,
            currency=Currency.GBP.value,
            amount="100",
            payment_reference="OUR_REF",
            finance_email="test@payment.com",
        )
    )

    print(response.text)


asyncio.run(request_payment_transfer_async(tillo))

tillo.close_sync()
asyncio.run(tillo.close_async())
