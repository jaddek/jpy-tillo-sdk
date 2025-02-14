from jpy_tillo_sdk.domain.float.endpoints import CheckFloatsEndpoint
from jpy_tillo_sdk.enums import Currency
from jpy_tillo_sdk.domain.float.factory import create_check_floats_query

def test_create_check_floats_query():
    request = create_check_floats_query(
        currency=Currency.EUR,
    )

    assert isinstance(request, CheckFloatsEndpoint.QueryParams)
    assert request.currency == Currency.EUR.value
