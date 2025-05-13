import string
from typing import Optional

from jpy_tillo_sdk.domain.float.endpoints import (
    CheckFloatsEndpoint,
    RequestPaymentTransferEndpoint,
)
from jpy_tillo_sdk.enums import Currency


def create_check_floats_query(currency: Currency):
    return CheckFloatsEndpoint.QueryParams(currency=currency.value)


def create_payment_transfer_request(
    transfer_float: str,
    currency: Currency,
    amount: string,
    finance_email: string,
    proforma_invoice: Optional[RequestPaymentTransferEndpoint.RequestBody.ProformaInvoiceParams] = None,
    payment_reference: string = "OUR_REF",
):
    return RequestPaymentTransferEndpoint.RequestBody(
        currency=currency,
        amount=amount,
        payment_reference=payment_reference,
        finance_email=finance_email,
        proforma_invoice=proforma_invoice,
        float=transfer_float,
    )
