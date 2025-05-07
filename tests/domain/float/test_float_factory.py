from jpy_tillo_sdk.domain.float.endpoints import (
    CheckFloatsEndpoint,
    RequestPaymentTransferEndpoint,
)
from jpy_tillo_sdk.enums import Currency
from jpy_tillo_sdk.domain.float.factory import (
    create_check_floats_query,
    create_payment_transfer_request,
)


def test_create_check_floats_query():
    request = create_check_floats_query(
        currency=Currency.EUR,
    )

    assert isinstance(request, CheckFloatsEndpoint.QueryParams)
    assert request.currency == Currency.EUR.value


def test_create_payment_transfer_request():
    request = create_payment_transfer_request(
        currency=Currency.EUR,
        amount="100",
        payment_reference="ref",
        finance_email="finance_email",
    )

    assert isinstance(request, RequestPaymentTransferEndpoint.RequestBody)
    assert request.currency == Currency.EUR
    assert request.amount == "100"
    assert request.payment_reference == "ref"
    assert request.finance_email == "finance_email"
    assert request.proforma_invoice is None
