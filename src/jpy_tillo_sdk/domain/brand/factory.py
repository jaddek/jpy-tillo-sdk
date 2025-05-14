from .endpoints import BrandEndpoint, TemplateEndpoint, TemplateListEndpoint


def create_brands_query_params(
    detail: bool = True,
    currency: str | None = None,
    country: str | None = None,
    brand: str | None = None,
    category: str | None = None,
) -> BrandEndpoint.QueryParams:
    return BrandEndpoint.QueryParams(detail, currency, country, brand, category)


def create_brand_template_list_query_params(
    brand: str | None = None,
) -> TemplateListEndpoint.QueryParams:
    return TemplateListEndpoint.QueryParams(brand)


def create_brand_template_query_params(
    brand: str | None = None,
    template: str | None = None,
) -> TemplateEndpoint.QueryParams:
    return TemplateEndpoint.QueryParams(brand, template)
