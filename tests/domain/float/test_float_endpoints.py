from jpy_tillo_sdk.domain.float.endpoints import CheckFloatsEndpoint, RequestPaymentTransferEndpoint
from jpy_tillo_sdk.enums import Domains
from jpy_tillo_sdk.http_methods import HttpMethods


def test_check_floats_endpoint():
    endpoint = CheckFloatsEndpoint()

    assert endpoint.method == HttpMethods.GET.value
    assert endpoint.endpoint == Domains.CHECK_FLOATS.value
    assert endpoint.route == "/api/v2/" + Domains.CHECK_FLOATS.value
    assert endpoint.body == {}
    assert endpoint.sign_attrs is None
    assert endpoint.is_body_not_empty() is False
    assert endpoint.params == {}


def test_request_payment_transfer_endpoint():
    endpoint = RequestPaymentTransferEndpoint()

    assert endpoint.method == HttpMethods.POST.value
    assert endpoint.endpoint == 'float-request-payment-transfer'
    assert endpoint.route == "/api/v2/float/request-payment-transfer"
    assert endpoint.body == {}
    assert endpoint.sign_attrs is None
    assert endpoint.is_body_not_empty() is False
    assert endpoint.params == {}
