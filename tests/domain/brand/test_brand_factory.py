import pytest

from jaddek_tillo_sdk.domain.brand.endpoints import (
    BrandEndpoint,
    TemplateListEndpoint,
    TemplateEndpoint,
)
from jaddek_tillo_sdk.domain.brand.factory import (
    create_brands_query_params,
    create_brand_template_list_query_params,
    create_brand_template_query_params,
)


class TestBrandFactory:
    def test_create_brands_query_params_default(self):
        params = create_brands_query_params()

        assert isinstance(params, BrandEndpoint.QueryParams)
        assert params.detail is True
        assert params.currency is None
        assert params.country is None
        assert params.brand is None
        assert params.category is None

    @pytest.mark.parametrize(
        "detail,currency,country,brand,category",
        [
            (False, "USD", "US", "test_brand", "test_category"),
            (True, "EUR", "UK", "another_brand", None),
            (False, None, None, None, "category_only"),
            (True, "GBP", None, "brand_only", None),
        ],
    )
    def test_create_brands_query_params_with_values(
        self, detail, currency, country, brand, category
    ):
        params = create_brands_query_params(
            detail=detail,
            currency=currency,
            country=country,
            brand=brand,
            category=category,
        )

        assert isinstance(params, BrandEndpoint.QueryParams)
        assert params.detail is detail
        assert params.currency == currency
        assert params.country == country
        assert params.brand == brand
        assert params.category == category

    def test_create_brand_template_list_query_params_empty(self):
        params = create_brand_template_list_query_params(brand=None)

        assert isinstance(params, TemplateListEndpoint.QueryParams)
        assert params.brand is None
        assert params.get_sign_attrs() == ()

    def test_create_brand_template_list_query_params_with_brand(self):
        brand = "test_brand"
        params = create_brand_template_list_query_params(brand=brand)

        assert isinstance(params, TemplateListEndpoint.QueryParams)
        assert params.brand == brand
        assert params.get_sign_attrs() == (brand,)

    def test_create_brand_template_query_params_empty(self):
        params = create_brand_template_query_params(brand=None, template=None)

        assert isinstance(params, TemplateEndpoint.QueryParams)
        assert params.brand is None
        assert params.template is None
        assert params.get_sign_attrs() == ()

    @pytest.mark.parametrize(
        "brand,template",
        [
            ("test_brand", "test_template"),
            ("test_brand", None),
            (None, "test_template"),
            (None, None),
        ],
    )
    def test_create_brand_template_query_params_with_values(self, brand, template):
        params = create_brand_template_query_params(
            brand=brand,
            template=template,
        )

        assert isinstance(params, TemplateEndpoint.QueryParams)
        assert params.brand == brand
        assert params.template == template

        if brand:
            assert params.get_sign_attrs() == (brand,)
        else:
            assert params.get_sign_attrs() == ()

    def test_get_not_empty_values(self):
        """Test that get_not_empty_values works correctly for all factory functions"""

        brands_params = create_brands_query_params(
            detail=True, currency="USD", country=None
        )
        assert brands_params.get_not_empty_values() == {
            "detail": True,
            "currency": "USD",
        }

        template_list_params = create_brand_template_list_query_params(
            brand="test_brand"
        )
        assert template_list_params.get_not_empty_values() == {"brand": "test_brand"}

        template_params = create_brand_template_query_params(
            brand="test_brand", template="test_template"
        )
        assert template_params.get_not_empty_values() == {
            "brand": "test_brand",
            "template": "test_template",
        }
