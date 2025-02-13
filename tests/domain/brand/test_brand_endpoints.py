import pytest

from jpy_tillo_sdk.domain.brand.endpoints import (
    BrandEndpoint,
    TemplateListEndpoint,
    TemplateEndpoint,
)
from jpy_tillo_sdk.endpoint import QP
from jpy_tillo_sdk.enums import Domains
from jpy_tillo_sdk.http_methods import HttpMethods


@pytest.fixture
def brand_endpoint():
    return BrandEndpoint()


@pytest.fixture
def brand_endpoint_query_params():
    return BrandEndpoint.QueryParams()


@pytest.fixture
def template_list_endpoint():
    return TemplateListEndpoint()


@pytest.fixture
def template_endpoint():
    return TemplateEndpoint()


def test_brand_endpoint(brand_endpoint):
    assert brand_endpoint.method == HttpMethods.GET.value
    assert brand_endpoint.endpoint == Domains.BRANDS.value
    assert brand_endpoint.route == "/api/v2/" + Domains.BRANDS.value
    assert isinstance(brand_endpoint.query, QP)
    assert brand_endpoint.body == {}
    assert brand_endpoint.sign_attrs is None
    assert brand_endpoint.is_body_not_empty() is False
    assert brand_endpoint.params == {}


@pytest.mark.parametrize(
    "query",
    [
        ({
            "brand": "brand",
            "category": "category",
            "country": "country",
            "currency": "currency",
            "detail": True
        }),
        ({
            "brand": "brand",
            "category": "category",
            "country": "country",
            "currency": "currency",
            "detail": False
        }),
        ({}),
        (None),
    ],
)
def test_brand_endpoint_query(query):
    endpoint_class = BrandEndpoint(query=query)

    assert isinstance(endpoint_class.query, BrandEndpoint.QueryParams)

    if query is None:
        assert endpoint_class.query.brand is None
        assert endpoint_class.query.category is None
        assert endpoint_class.query.country is None
        assert endpoint_class.query.currency is None
        assert endpoint_class.query.detail is None
    else:
        assert endpoint_class.query.brand == query.get("brand")
        assert endpoint_class.query.category == query.get("category")
        assert endpoint_class.query.country == query.get("country")
        assert endpoint_class.query.currency == query.get("currency")
        assert endpoint_class.query.detail == query.get("detail")


@pytest.mark.parametrize(
    "query,not_empty_values,sign_attrs",
    [
        (
                {
                    "brand": "brand",
                    "category": "category",
                    "country": "country",
                    "currency": "currency",
                    "detail": True
                }, {
                    "brand": "brand",
                    "category": "category",
                    "country": "country",
                    "currency": "currency",
                    "detail": True
                },
                None
        ),
        (
                {
                    "brand": "brand",
                    "category": "category",
                    "country": "country",
                    "currency": "currency",
                    "detail": False
                }, {
                    "brand": "brand",
                    "category": "category",
                    "country": "country",
                    "currency": "currency",
                    "detail": False
                },
                None
        ),
        (
                {
                    "brand": "brand",
                    "category": "category",
                    "country": None,
                    "currency": None,
                    "detail": True
                }, {
                    "brand": "brand",
                    "category": "category",
                    "detail": True
                },
                None
        ),
        (
                {},
                {},
                None
        ),
        (None, {}, None),
    ],
)
def test_brand_endpoint_query_params(query, not_empty_values, sign_attrs):
    qp = BrandEndpoint.QueryParams(
        detail=query.get("detail") if query is not None else None,
        currency=query.get("currency") if query is not None else None,
        country=query.get("country") if query is not None else None,
        brand=query.get("brand") if query is not None else None,
        category=query.get("category") if query is not None else None,
    )

    assert qp.get_not_empty_values() == not_empty_values
    assert qp.get_sign_attrs() is None


def test_template_list_endpoint(template_list_endpoint):
    assert template_list_endpoint.method == HttpMethods.GET.value
    assert template_list_endpoint.endpoint == Domains.TEMPLATES.value
    assert template_list_endpoint.route == "/api/v2/" + Domains.TEMPLATES.value
    assert isinstance(template_list_endpoint.query, QP)
    assert template_list_endpoint.body == {}
    assert template_list_endpoint.sign_attrs is None
    assert template_list_endpoint.is_body_not_empty() is False
    assert template_list_endpoint.params == {}


@pytest.mark.parametrize(
    "query,not_empty_values,sign_attrs",
    [
        (
                {
                    "brand": "brand",
                }, {
                    "brand": "brand",
                },
                None
        ),
        (
                {
                    "brand": None,
                },
                {},
                None
        ),
        (
                {},
                {},
                None
        ),
        (
                None,
                {},
                None
        ),
    ],
)
def test_template_list_endpoint_query_params(query, not_empty_values, sign_attrs):
    brand_value = query.get("brand") if query is not None else None

    qp = TemplateListEndpoint.QueryParams(
        brand=brand_value,
    )

    assert qp.get_not_empty_values() == not_empty_values

    if brand_value is None:
        assert qp.get_sign_attrs() == ()
    else:
        assert qp.get_sign_attrs() == (brand_value,)


@pytest.mark.parametrize(
    "query",
    [
        ({
            "brand": "brand",
        }),
        ({
            "brand": "brand",
        }),
        ({}),
        (None),
    ],
)
def test_template_list_endpoint_query(query):
    endpoint_class = TemplateListEndpoint(query=query)

    assert isinstance(endpoint_class.query, TemplateListEndpoint.QueryParams)

    if query is None:
        assert endpoint_class.query.brand is None
    else:
        assert endpoint_class.query.brand == query.get("brand")


def test_template_endpoint(template_endpoint):
    assert template_endpoint.method == HttpMethods.GET.value
    assert template_endpoint.endpoint == Domains.TEMPLATE.value
    assert template_endpoint.route == "/api/v2/" + Domains.TEMPLATE.value
    assert isinstance(template_endpoint.query, QP)
    assert template_endpoint.body == {}
    assert template_endpoint.sign_attrs is None
    assert template_endpoint.is_body_not_empty() is False
    assert template_endpoint.params == {}


@pytest.mark.parametrize(
    "query",
    [
        ({
            "brand": "brand",
            "template": "template",
        }),
        ({
            "brand": "brand",
            "template": "template",
        }),
        ({}),
        (None),
    ],
)
def test_template_endpoint_query(query):
    endpoint_class = TemplateEndpoint(query=query)

    assert isinstance(endpoint_class.query, TemplateEndpoint.QueryParams)

    if query is None:
        assert endpoint_class.query.brand is None
        assert endpoint_class.query.template is None
    else:
        assert endpoint_class.query.brand == query.get("brand")
        assert endpoint_class.query.template == query.get("template")


@pytest.mark.parametrize(
    "query,not_empty_values,sign_attrs",
    [
        (
                {
                    "brand": "brand",
                    "template": "template",
                }, {
                    "brand": "brand",
                    "template": "template",
                },
                None
        ),
        (
                {
                    "brand": "brand",
                    "template": None,
                }, {
                    "brand": "brand",
                },
                None
        ),
        (
                {
                    "brand": None,
                },
                {},
                None
        ),
        (
                {},
                {},
                None
        ),
        (
                None,
                {},
                None
        ),
    ],
)
def test_template_endpoint_query_params(query, not_empty_values, sign_attrs):
    brand_value = query.get("brand") if query is not None else None
    template_value = query.get("template") if query is not None else None

    qp = TemplateEndpoint.QueryParams(
        brand=brand_value,
        template=template_value
    )

    assert qp.get_not_empty_values() == not_empty_values

    if brand_value is None:
        assert qp.get_sign_attrs() == ()
    else:
        assert qp.get_sign_attrs() == (brand_value,)
