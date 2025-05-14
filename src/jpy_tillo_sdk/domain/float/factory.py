from jpy_tillo_sdk.domain.float.endpoints import (
    CheckFloatsEndpoint,
    RequestPaymentTransferEndpoint,
)
from jpy_tillo_sdk.enums import Currency


def create_check_floats_query(currency: Currency) -> CheckFloatsEndpoint.QueryParams:
    return CheckFloatsEndpoint.QueryParams(currency=currency)


def create_payment_transfer_request(
    transfer_float: str,
    currency: Currency,
    amount: str,
    finance_email: str,
    proforma_invoice: RequestPaymentTransferEndpoint.RequestBody.ProformaInvoiceParams | None = None,
    payment_reference: str = "OUR_REF",
) -> RequestPaymentTransferEndpoint.RequestBody:
    return RequestPaymentTransferEndpoint.RequestBody(
        currency=currency,
        amount=amount,
        payment_reference=payment_reference,
        finance_email=finance_email,
        proforma_invoice=proforma_invoice,
        float=transfer_float,
    )
