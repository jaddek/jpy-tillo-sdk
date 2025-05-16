import logging
from typing import final

from httpx import Response

from ...contracts import (
    BrandServiceAsyncInterface,
    BrandServiceInterface,
    TemplateServiceAsyncInterface,
    TemplateServiceInterface,
)
from .endpoints import (
    BrandEndpoint,
    BrandEndpointRequestQuery,
    DownloadBrandTemplateEndpoint,
    DownloadBrandTemplateEndpointRequestQuery,
    TemplatesListEndpoint,
    TemplatesListEndpointRequestQuery,
)

logger = logging.getLogger("tillo.brand_services")


@final
class BrandService(BrandServiceInterface):
    def get_available_brands(
        self,
        query: BrandEndpointRequestQuery | None = None,
    ) -> Response:
        endpoint: BrandEndpoint = BrandEndpoint(query=query)
        return self.client.request(endpoint=endpoint)


@final
class BrandServiceAsync(BrandServiceAsyncInterface):
    async def get_available_brands(
        self,
        query: BrandEndpointRequestQuery | None = None,
    ) -> Response:
        endpoint = BrandEndpoint(query=query)
        return await self.client.request(endpoint=endpoint)


@final
class TemplateService(TemplateServiceInterface):
    def get_templates_list(
        self,
        query: TemplatesListEndpointRequestQuery | None = None,
    ) -> Response:
        endpoint = TemplatesListEndpoint(query=query)
        return self.client.request(endpoint=endpoint)

    def download_brand_template(
        self,
        query: DownloadBrandTemplateEndpointRequestQuery | None = None,
    ) -> Response:
        endpoint = DownloadBrandTemplateEndpoint(query=query)
        return self.client.request(endpoint=endpoint)


@final
class TemplateServiceAsync(TemplateServiceAsyncInterface):
    async def download_brand_template(
        self,
        query: DownloadBrandTemplateEndpointRequestQuery | None = None,
    ) -> Response:
        endpoint = DownloadBrandTemplateEndpoint(query)
        return await self.client.request(endpoint=endpoint)

    async def get_brand_templates(
        self,
        query: TemplatesListEndpointRequestQuery | None = None,
    ) -> Response:
        endpoint = TemplatesListEndpoint(query)
        return await self.client.request(endpoint=endpoint)
