import string
from typing import Optional

from jpy_tillo_sdk.domain.float.endpoints import CheckFloatsEndpoint, RequestPaymentTransferEndpoint
from jpy_tillo_sdk.enums import Currency


def create_check_floats_query(currency: Currency):
    return CheckFloatsEndpoint.QueryParams(currency=currency.value)


def create_payment_transfer_request(
        currency: Currency,
        amount: string,
        payment_reference: string,
        finance_email: string,
        proforma_invoice: Optional[RequestPaymentTransferEndpoint.RequestBody.ProformaInvoiceParams] = None
):
    return RequestPaymentTransferEndpoint.RequestBody(
        currency=Currency.EUR,
        amount="100",
        payment_reference="PAY_REF",
        finance_email="<EMAIL>",
        proforma_invoice=proforma_invoice,
    )
