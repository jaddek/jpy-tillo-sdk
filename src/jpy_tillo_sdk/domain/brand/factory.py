from typing import Optional

from .endpoints import BrandEndpoint, TemplateEndpoint, TemplateListEndpoint


def create_brands_query_params(
    detail: bool = True,
    currency: Optional[str] = None,
    country: Optional[str] = None,
    brand: Optional[str] = None,
    category: Optional[str] = None,
) -> BrandEndpoint.QueryParams:
    return BrandEndpoint.QueryParams(detail, currency, country, brand, category)


def create_brand_template_list_query_params(
    brand: Optional[str] = None,
) -> TemplateListEndpoint.QueryParams:
    return TemplateListEndpoint.QueryParams(brand)


def create_brand_template_query_params(
    brand: Optional[str] = None,
    template: Optional[str] = None,
) -> TemplateEndpoint.QueryParams:
    return TemplateEndpoint.QueryParams(brand, template)
