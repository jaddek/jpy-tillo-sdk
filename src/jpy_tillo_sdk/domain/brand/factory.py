from .endpoints import TemplateEndpoint, TemplateListEndpoint


def create_brand_template_list_query_params(
    brand: str | None = None,
) -> TemplateListEndpoint.QueryParams:
    return TemplateListEndpoint.QueryParams(brand)


def create_brand_template_query_params(
    brand: str | None = None,
    template: str | None = None,
) -> TemplateEndpoint.QueryParams:
    return TemplateEndpoint.QueryParams(brand, template)
