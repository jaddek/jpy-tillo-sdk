import pytest

from jpy_tillo_sdk.domain.brand.endpoints import (
    BrandEndpoint,
    TemplateListEndpoint,
    TemplateEndpoint,
)
from jpy_tillo_sdk.enums import Domains
from jpy_tillo_sdk.http_methods import HttpMethods


def test_brand_endpoint():
    endpoint = BrandEndpoint()

    assert endpoint.method == HttpMethods.GET.value
    assert endpoint.endpoint == Domains.BRANDS.value
    assert endpoint.route == "/api/v2/" + Domains.BRANDS.value
    assert endpoint.query is None
    assert endpoint.body == {}
    assert endpoint.sign_attrs is None
    assert endpoint.is_body_not_empty() is False
    assert endpoint.params == {}


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
    endpoint_class = BrandEndpoint(query=BrandEndpoint.QueryParams(**query))

    if query is None:
        assert endpoint_class.query is None
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
                "detail": True,
            },
            {
                "brand": "brand",
                "category": "category",
                "country": "country",
                "currency": "currency",
                "detail": True,
            },
            None,
        ),
        (
            {
                "brand": "brand",
                "category": "category",
                "country": "country",
                "currency": "currency",
                "detail": False,
            },
            {
                "brand": "brand",
                "category": "category",
                "country": "country",
                "currency": "currency",
                "detail": False,
            },
            None,
        ),
        (
            {
                "brand": "brand",
                "category": "category",
                "country": None,
                "currency": None,
                "detail": True,
            },
            {"brand": "brand", "category": "category", "detail": True},
            None,
        ),
        ({}, {}, None),
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
    assert qp.get_sign_attrs() == ()


def test_template_list_endpoint():
    endpoint = TemplateListEndpoint()

    assert endpoint.method == HttpMethods.GET.value
    assert endpoint.endpoint == Domains.TEMPLATES.value
    assert endpoint.route == "/api/v2/" + Domains.TEMPLATES.value
    assert endpoint.query is None
    assert endpoint.body == {}
    assert endpoint.sign_attrs is None
    assert endpoint.is_body_not_empty() is False
    assert endpoint.params == {}


@pytest.mark.parametrize(
    "query,not_empty_values,sign_attrs",
    [
        (
            {
                "brand": "brand",
            },
            {
                "brand": "brand",
            },
            None,
        ),
        (
            {
                "brand": None,
            },
            {},
            None,
        ),
        ({}, {}, None),
        (None, {}, None),
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
    endpoint_class = TemplateListEndpoint(
        query=TemplateListEndpoint.QueryParams(**query)
    )

    assert isinstance(endpoint_class.query, TemplateListEndpoint.QueryParams)

    if query is None:
        assert endpoint_class.query.brand is None
    else:
        assert endpoint_class.query.brand == query.get("brand")


def test_endpoint():
    endpoint = TemplateEndpoint()

    assert endpoint.method == HttpMethods.GET.value
    assert endpoint.endpoint == Domains.TEMPLATE.value
    assert endpoint.route == "/api/v2/" + Domains.TEMPLATE.value
    assert endpoint.query is None
    assert endpoint.body == {}
    assert endpoint.sign_attrs is None
    assert endpoint.is_body_not_empty() is False
    assert endpoint.params == {}


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
    endpoint_class = TemplateEndpoint(query=TemplateEndpoint.QueryParams(**query))

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
            },
            {
                "brand": "brand",
                "template": "template",
            },
            None,
        ),
        (
            {
                "brand": "brand",
                "template": None,
            },
            {
                "brand": "brand",
            },
            None,
        ),
        (
            {
                "brand": None,
            },
            {},
            None,
        ),
        ({}, {}, None),
        (None, {}, None),
    ],
)
def test_endpoint_query_params(query, not_empty_values, sign_attrs):
    brand_value = query.get("brand") if query is not None else None
    template_value = query.get("template") if query is not None else None

    qp = TemplateEndpoint.QueryParams(brand=brand_value, template=template_value)

    assert qp.get_not_empty_values() == not_empty_values

    if brand_value is None:
        assert qp.get_sign_attrs() == ()
    else:
        assert qp.get_sign_attrs() == (brand_value,)
