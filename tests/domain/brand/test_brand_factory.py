import pytest

from jpy_tillo_sdk.domain.brand.endpoints import (
    TemplateEndpoint,
    TemplateListEndpoint,
)
from jpy_tillo_sdk.domain.brand.factory import (
    create_brand_template_list_query_params,
    create_brand_template_query_params,
)


class TestBrandFactory:
    def test_create_brand_template_list_query_params_empty(self) -> None:
        params = create_brand_template_list_query_params(brand=None)

        assert isinstance(params, TemplateListEndpoint.QueryParams)
        assert params.brand is None
        assert params.get_sign_attrs() == ()

    def test_create_brand_template_list_query_params_with_brand(self) -> None:
        brand = "test_brand"
        params = create_brand_template_list_query_params(brand=brand)

        assert isinstance(params, TemplateListEndpoint.QueryParams)
        assert params.brand == brand
        assert params.get_sign_attrs() == (brand,)

    def test_create_brand_template_query_params_empty(self) -> None:
        params = create_brand_template_query_params(brand=None, template=None)

        assert isinstance(params, TemplateEndpoint.QueryParams)
        assert params.brand is None
        assert params.template is None
        assert params.get_sign_attrs() == ()

    @pytest.mark.parametrize(  # type: ignore[misc]
        "brand,template",
        [
            ("test_brand", "test_template"),
            ("test_brand", None),
            (None, "test_template"),
            (None, None),
        ],
    )
    def test_create_brand_template_query_params_with_values(self, brand: str | None, template: str | None) -> None:
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

    def test_get_not_empty_values(self) -> None:
        template_list_params = create_brand_template_list_query_params(brand="test_brand")
        assert template_list_params.get_not_empty_values() == {"brand": "test_brand"}

        template_params = create_brand_template_query_params(brand="test_brand", template="test_template")
        assert template_params.get_not_empty_values() == {
            "brand": "test_brand",
            "template": "test_template",
        }
