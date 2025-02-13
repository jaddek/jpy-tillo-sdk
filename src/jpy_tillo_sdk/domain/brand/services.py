from typing import Optional, Any

from .endpoints import BrandEndpoint, TemplateListEndpoint, TemplateEndpoint
from ...http_client import HttpClient, AsyncHttpClient


class BrandService:
    @staticmethod
    def get_available_brands(
            client: HttpClient,
            query_params: Optional[dict] = None,
    ) -> Any:
        endpoint = BrandEndpoint(query=query_params or {})
        return client.request(endpoint=endpoint)

    @staticmethod
    async def get_available_brands_async(
            client: AsyncHttpClient,
            query_params: Optional[dict] = None,
    ) -> Any:
        endpoint = BrandEndpoint(query=query_params or {})
        return await client.request(endpoint=endpoint)


class TemplateService:
    @staticmethod
    def get_brand_templates(
            client: HttpClient,
            query_params: Optional[dict] = None,
    ) -> Any:
        endpoint = TemplateListEndpoint(query_params or {})
        return client.request(endpoint=endpoint)

    @staticmethod
    async def get_brand_templates_async(
            client: AsyncHttpClient,
            query_params: Optional[dict] = None,
    ) -> Any:
        endpoint = TemplateListEndpoint(query_params or {})
        return await client.request(endpoint=endpoint)

    @staticmethod
    def download_brand_template(
            client: HttpClient,
            query_params: Optional[dict] = None,
    ) -> Any:
        endpoint = TemplateEndpoint(query_params or {})
        return client.request(endpoint=endpoint)

    @staticmethod
    async def download_brand_template_async(
            client: AsyncHttpClient,
            query_params: Optional[dict] = None,
    ) -> Any:
        endpoint = TemplateEndpoint(query_params or {})
        return await client.request(endpoint=endpoint)
