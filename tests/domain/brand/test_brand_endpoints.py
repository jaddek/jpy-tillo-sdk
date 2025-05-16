import pytest

from jpy_tillo_sdk.domain.brand.endpoints import (
    BrandEndpoint,
    BrandEndpointRequestQuery,
    DownloadBrandTemplateEndpoint,
    DownloadBrandTemplateEndpointRequestQuery,
    TemplatesListEndpoint,
    TemplatesListEndpointRequestQuery,
)
from jpy_tillo_sdk.enums import Domains
from jpy_tillo_sdk.http_methods import HttpMethods


def test_brand_endpoint():
    endpoint = BrandEndpoint()

    assert endpoint.method == HttpMethods.GET.value
    assert endpoint.endpoint == Domains.BRANDS.value
    assert endpoint.route == "/api/v2/" + Domains.BRANDS.value
    assert endpoint.query is None
    assert endpoint.body is None
    assert endpoint.sign_attrs == ()
    assert endpoint.query is None


@pytest.mark.parametrize(
    "query",
    [
        (
            {
                "brand": "brand",
                "category": "category",
                "country": "country",
                "currency": "currency",
                "detail": True,
            }
        ),
        (
            {
                "brand": "brand",
                "category": "category",
                "country": "country",
                "currency": "currency",
                "detail": False,
            }
        ),
        ({}),
    ],
)
def test_brand_endpoint_query(query):
    endpoint_class = BrandEndpoint(query=BrandEndpointRequestQuery(**query))

    if query is None:
        assert endpoint_class.query is None
    else:
        assert endpoint_class.query.brand == query.get("brand")
        assert endpoint_class.query.category == query.get("category")
        assert endpoint_class.query.country == query.get("country")
        assert endpoint_class.query.currency == query.get("currency")
        assert endpoint_class.query.detail == query.get("detail")


def test_template_list_endpoint():
    endpoint = TemplatesListEndpoint()

    assert endpoint.method == HttpMethods.GET.value
    assert endpoint.endpoint == Domains.TEMPLATES.value
    assert endpoint.route == "/api/v2/" + Domains.TEMPLATES.value
    assert endpoint.query is None
    assert endpoint.body is None
    assert endpoint.sign_attrs == ()
    assert endpoint.query is None


@pytest.mark.parametrize(
    "query",
    [
        (
            {
                "brand": "brand",
            }
        ),
        (
            {
                "brand": "brand",
            }
        ),
        ({}),
    ],
)
def test_template_list_endpoint_query(query):
    endpoint_class = TemplatesListEndpoint(query=TemplatesListEndpointRequestQuery(**query))

    assert isinstance(endpoint_class.query, TemplatesListEndpointRequestQuery)

    if query is None:
        assert endpoint_class.query.brand is None
    else:
        assert endpoint_class.query.brand == query.get("brand")


def test_endpoint():
    endpoint = DownloadBrandTemplateEndpoint()

    assert endpoint.method == HttpMethods.GET.value
    assert endpoint.endpoint == Domains.TEMPLATE.value
    assert endpoint.route == "/api/v2/" + Domains.TEMPLATE.value
    assert endpoint.query is None
    assert endpoint.body is None
    assert endpoint.sign_attrs == ()
    assert endpoint.query is None


@pytest.mark.parametrize(
    "query",
    [
        (
            {
                "brand": "brand",
                "template": "template",
            }
        ),
        (
            {
                "brand": "brand",
                "template": "template",
            }
        ),
        ({}),
    ],
)
def test_endpoint_query(query):
    endpoint_class = DownloadBrandTemplateEndpoint(query=DownloadBrandTemplateEndpointRequestQuery(**query))

    assert isinstance(endpoint_class.query, DownloadBrandTemplateEndpointRequestQuery)

    if query is None:
        assert endpoint_class.query.brand is None
        assert endpoint_class.query.template is None
    else:
        assert endpoint_class.query.brand == query.get("brand")
        assert endpoint_class.query.template == query.get("template")
