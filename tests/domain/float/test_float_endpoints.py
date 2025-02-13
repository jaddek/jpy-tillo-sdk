from jpy_tillo_sdk.domain.float.endpoints import CheckFloatsEndpoint
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
