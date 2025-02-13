import pytest

from jpy_tillo_sdk.domain.digital_card.endpoints import IssueDigitalCodeEndpoint, TopUpDigitalCodeEndpoint, \
    CheckStockEndpoint, CancelDigitalCodeEndpoint, CancelDigitalUrlEndpoint, ReverseDigitalCodeEndpoint, \
    CheckBalanceEndpoint, OrderDigitalCodeAsyncEndpoint, CheckDigitalOrderStatusAsyncEndpoint
from jpy_tillo_sdk.domain.digital_card.models import FaceValue
from jpy_tillo_sdk.enums import Domains
from jpy_tillo_sdk.http_methods import HttpMethods


def test_issue_digital_code_endpoint():
    issue_digital_code_endpoint = IssueDigitalCodeEndpoint()

    assert issue_digital_code_endpoint.method == HttpMethods.POST.value
    assert issue_digital_code_endpoint.endpoint == Domains.DIGITAL_CARD.value + "-issue"
    assert issue_digital_code_endpoint.route == "/api/v2/digital/issue"
    assert issue_digital_code_endpoint.body == {}
    assert issue_digital_code_endpoint.sign_attrs is None
    assert issue_digital_code_endpoint.is_body_not_empty() is False
    assert issue_digital_code_endpoint.params == {}


@pytest.mark.parametrize(
    "body,signed_attrs",
    [
        ({}, ())
    ],
)
def test_issue_digital_code_endpoint_request_sign_attrs_if_body_is_empty(
        body,
        signed_attrs
):
    request_body = IssueDigitalCodeEndpoint.RequestBody(**body)

    assert request_body.client_request_id is None
    assert request_body.brand is None
    assert request_body.face_value is None
    assert request_body.delivery_method is None
    assert request_body.fulfilment_by is None
    assert request_body.sector is None
    assert request_body.personalisation is None

    assert (request_body.get_sign_attrs() == signed_attrs)


@pytest.mark.parametrize(
    "body,signed_attrs",
    [
        ({
             "client_request_id": "cl_req_id",
             "brand": "brand",
             "face_value": FaceValue(**{
                 "currency": "EUR",
                 "amount": "100",
             }),
             "delivery_method": "method",
             "fulfilment_by": "by",
             "sector": "test",
             "personalisation": None
         },
         ('cl_req_id', 'brand', "EUR", "100")
        ),
    ],
)
def test_issue_digital_code_endpoint_request_sign_attrs(body, signed_attrs):
    request_body = IssueDigitalCodeEndpoint.RequestBody(**body)

    assert request_body.client_request_id == body.get("client_request_id")
    assert request_body.brand == body.get("brand")
    assert request_body.face_value == body.get("face_value")
    assert request_body.delivery_method == body.get("delivery_method")
    assert request_body.fulfilment_by == body.get("fulfilment_by")
    assert request_body.sector == body.get("sector")
    assert request_body.personalisation == body.get("personalisation")

    assert (request_body.get_sign_attrs() == signed_attrs)


def test_top_up_digital_code_endpoint():
    endpoint = TopUpDigitalCodeEndpoint()

    assert endpoint.method == HttpMethods.POST.value
    assert endpoint.endpoint == Domains.DIGITAL_CARD.value + "-top-up"
    assert endpoint.route == "/api/v2/digital/top-up"
    assert endpoint.body == {}
    assert endpoint.sign_attrs is None
    assert endpoint.is_body_not_empty() is False
    assert endpoint.params == {}


@pytest.mark.parametrize(
    "body,signed_attrs",
    [
        ({
             "client_request_id": "cl_req_id",
             "brand": "brand",
             "face_value": FaceValue(**{
                 "currency": "EUR",
                 "amount": "100",
             }),
             "code": "method",
             "pin": "by",
             "sector": "test",
         },
         ('cl_req_id', 'brand', "EUR", "100")
        ),
    ],
)
def test_top_up_digital_code_endpoint_request_sign_attrs(body, signed_attrs):
    request_body = TopUpDigitalCodeEndpoint.RequestBody(**body)

    assert request_body.client_request_id == body.get("client_request_id")
    assert request_body.brand == body.get("brand")
    assert request_body.face_value == body.get("face_value")
    assert request_body.code == body.get("code")
    assert request_body.pin == body.get("pin")
    assert request_body.sector == body.get("sector")

    assert (request_body.get_sign_attrs() == signed_attrs)


#

def test_check_stock_endpoint():
    endpoint = CheckStockEndpoint()

    assert endpoint.method == HttpMethods.GET.value
    assert endpoint.endpoint == Domains.CHECK_STOCK.value
    assert endpoint.route == "/api/v2/" + Domains.CHECK_STOCK.value
    assert endpoint.body == {}
    assert endpoint.sign_attrs is None
    assert endpoint.is_body_not_empty() is False
    assert endpoint.params == {}


@pytest.mark.parametrize(
    "query,signed_attrs",
    [
        ({
             "brand": "brand",
         },
         ('brand',)
        ),
    ],
)
def test_check_stock_endpoint_query_sign_attrs(query, signed_attrs):
    request_query = CheckStockEndpoint.QueryParams(**query)

    assert request_query.brand == query.get("brand")

    assert (request_query.get_sign_attrs() == signed_attrs)


#

def test_cancel_digital_code_endpoint():
    endpoint = CancelDigitalCodeEndpoint()

    assert endpoint.method == HttpMethods.DELETE.value
    assert endpoint.endpoint == Domains.DIGITAL_CARD.value + "-issue"
    assert endpoint.route == "/api/v2/" + Domains.DIGITAL_CARD.value + "/issue"
    assert endpoint.body == {}
    assert endpoint.sign_attrs is None
    assert endpoint.is_body_not_empty() is False
    assert endpoint.params == {}


@pytest.mark.parametrize(
    "body,signed_attrs",
    [
        ({
             "client_request_id": "cl_req_id",
             "original_client_request_id": "or_req_id",
             "brand": "brand",
             "face_value": FaceValue(**{
                 "currency": "EUR",
                 "amount": "100",
             }),
             "code": "method",
             "sector": "test",
         },
         ('cl_req_id', 'brand', "EUR", "100")
        ),
    ],
)
def test_cancel_digital_code_endpoint_request_sign_attrs(body, signed_attrs):
    request_body = CancelDigitalCodeEndpoint.RequestBody(**body)

    assert request_body.client_request_id == body.get("client_request_id")
    assert request_body.original_client_request_id == body.get("original_client_request_id")
    assert request_body.face_value == body.get("face_value")
    assert request_body.code == body.get("code")
    assert request_body.sector == body.get("sector")

    assert (request_body.get_sign_attrs() == signed_attrs)


#

def test_cancel_digital_url_endpoint():
    endpoint = CancelDigitalCodeEndpoint()

    assert endpoint.method == HttpMethods.DELETE.value
    assert endpoint.endpoint == Domains.DIGITAL_CARD.value + "-issue"
    assert endpoint.route == "/api/v2/" + Domains.DIGITAL_CARD.value + "/issue"
    assert endpoint.body == {}
    assert endpoint.sign_attrs is None
    assert endpoint.is_body_not_empty() is False
    assert endpoint.params == {}


@pytest.mark.parametrize(
    "body,signed_attrs",
    [
        ({
             "client_request_id": "cl_req_id",
             "original_client_request_id": "or_req_id",
             "brand": "brand",
             "face_value": FaceValue(**{
                 "currency": "EUR",
                 "amount": "100",
             }),
             "url": "some url",
             "sector": "test",
         },
         ('cl_req_id', 'brand', "EUR", "100")
        ),
    ],
)
def test_cancel_digital_url_endpoint_request_sign_attrs(body, signed_attrs):
    request_body = CancelDigitalUrlEndpoint.RequestBody(**body)

    assert request_body.client_request_id == body.get("client_request_id")
    assert request_body.original_client_request_id == body.get("original_client_request_id")
    assert request_body.face_value == body.get("face_value")
    assert request_body.url == body.get("url")
    assert request_body.sector == body.get("sector")

    assert (request_body.get_sign_attrs() == signed_attrs)


#

def test_reverse_digital_code_endpoint():
    endpoint = ReverseDigitalCodeEndpoint()

    assert endpoint.method == HttpMethods.POST.value
    assert endpoint.endpoint == Domains.DIGITAL_CARD.value + "-reverse"
    assert endpoint.route == "/api/v2/" + Domains.DIGITAL_CARD.value + "/reverse"
    assert endpoint.body == {}
    assert endpoint.sign_attrs is None
    assert endpoint.is_body_not_empty() is False
    assert endpoint.params == {}


@pytest.mark.parametrize(
    "body,signed_attrs",
    [
        ({
             "client_request_id": "cl_req_id",
             "original_client_request_id": "or_req_id",
             "brand": "brand",
             "face_value": FaceValue(**{
                 "currency": "EUR",
                 "amount": "100",
             }),
             "sector": "test",
         },
         ('cl_req_id', 'brand', "EUR", "100")
        ),
    ],
)
def test_reverse_digital_code_endpoint_request_sign_attrs(body, signed_attrs):
    request_body = ReverseDigitalCodeEndpoint.RequestBody(**body)

    assert request_body.client_request_id == body.get("client_request_id")
    assert request_body.original_client_request_id == body.get("original_client_request_id")
    assert request_body.face_value == body.get("face_value")
    assert request_body.brand == body.get("brand")
    assert request_body.sector == body.get("sector")

    assert (request_body.get_sign_attrs() == signed_attrs)


#

def test_check_balance_endpoint():
    endpoint = CheckBalanceEndpoint()

    assert endpoint.method == HttpMethods.POST.value
    assert endpoint.endpoint == Domains.DIGITAL_CARD.value + "-check-balance"
    assert endpoint.route == "/api/v2/" + Domains.DIGITAL_CARD.value + "/check-balance"
    assert endpoint.body == {}
    assert endpoint.sign_attrs is None
    assert endpoint.is_body_not_empty() is False
    assert endpoint.params == {}


@pytest.mark.parametrize(
    "body,signed_attrs",
    [
        ({
             "client_request_id": "cl_req_id",
             "brand": "brand",
             "face_value": FaceValue(**{
                 "currency": "EUR",
             }),
             "reference": "test",
         },
         ('cl_req_id', 'brand', "EUR")
        ),
    ],
)
def test_check_balance_endpoint_request_sign_attrs(body, signed_attrs):
    request_body = CheckBalanceEndpoint.RequestBody(**body)

    assert request_body.client_request_id == body.get("client_request_id")
    assert request_body.face_value == body.get("face_value")
    assert request_body.brand == body.get("brand")
    assert request_body.reference == body.get("reference")

    assert (request_body.get_sign_attrs() == signed_attrs)


#

def test_order_digital_code_async_endpoint():
    endpoint = OrderDigitalCodeAsyncEndpoint()

    assert endpoint.method == HttpMethods.POST.value
    assert endpoint.endpoint == Domains.DIGITAL_CARD.value + "-order-card"
    assert endpoint.route == "/api/v2/" + Domains.DIGITAL_CARD.value + "/order-card"
    assert endpoint.body == {}
    assert endpoint.sign_attrs is None
    assert endpoint.is_body_not_empty() is False
    assert endpoint.params == {}


@pytest.mark.parametrize(
    "body,signed_attrs",
    [
        ({
             "client_request_id": "cl_req_id",
             "brand": "brand",
             "face_value": FaceValue(**{
                 "currency": "EUR",
                 "amount": "100",
             }),
             "delivery_method": "delivery_method",
             "fulfilment_by": "operator",
             "fulfilment_parameters": None,
             "sector": "test",
             "personalisation": None,
         },
         ('cl_req_id', 'brand', "EUR", "100")
        ),
    ],
)
def test_order_digital_code_async_endpoint_request_sign_attrs(body, signed_attrs):
    request_body = OrderDigitalCodeAsyncEndpoint.RequestBody(**body)

    assert request_body.client_request_id == body.get("client_request_id")
    assert request_body.brand == body.get("brand")
    assert request_body.face_value == body.get("face_value")
    assert request_body.delivery_method == body.get("delivery_method")
    assert request_body.fulfilment_by == body.get("fulfilment_by")
    assert request_body.fulfilment_parameters == body.get("fulfilment_parameters")
    assert request_body.sector == body.get("sector")
    assert request_body.personalisation == body.get("personalisation")

    assert (request_body.get_sign_attrs() == signed_attrs)


#

def test_check_digital_order_status_async_endpoint():
    endpoint = CheckDigitalOrderStatusAsyncEndpoint()

    assert endpoint.method == HttpMethods.GET.value
    assert endpoint.endpoint == Domains.DIGITAL_CARD.value + "-order-status"
    assert endpoint.route == "/api/v2/" + Domains.DIGITAL_CARD.value + "/order-status"
    assert endpoint.body == {}
    assert endpoint.sign_attrs is None
    assert endpoint.is_body_not_empty() is False
    assert endpoint.params == {}


@pytest.mark.parametrize(
    "query,signed_attrs",
    [
        ({
             "reference": "test",
         },
         ()
        ),
    ],
)
def test_check_digital_order_status_async_endpoint_request_sign_attrs(query, signed_attrs):
    request_query = CheckDigitalOrderStatusAsyncEndpoint.QueryParams(**query)

    assert request_query.reference == query.get("reference")

    assert (request_query.get_sign_attrs() == signed_attrs)
