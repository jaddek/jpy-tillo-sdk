import logging
from typing import Optional

from httpx import Response

from ...contracts import TemplateServiceAsyncInterface, TemplateServiceInterface
from ...http_client import AsyncHttpClient, HttpClient
from .endpoints import BrandEndpoint, TemplateEndpoint, TemplateListEndpoint

logger = logging.getLogger("tillo.brand_services")


class BrandService:
    def __init__(self, *, client: HttpClient):
        """Initialize the float service with an HTTP client.

        Args:
            client (HttpClient): The HTTP client instance for making requests
        """
        self.client = client
        logger.debug("Initialized BrandService with HTTP client")

    def get_available_brands(
        self,
        query_params: Optional[BrandEndpoint.QueryParams] = None,
    ) -> Response:
        endpoint = BrandEndpoint(query=query_params)

        return self.client.request(endpoint=endpoint)


class BrandServiceAsync:
    def __init__(self, *, client: AsyncHttpClient):
        """Initialize the float service with an HTTP client.

        Args:
            client (AsyncHttpClient): The HTTP client instance for making requests
        """
        self.client = client
        logger.debug("Initialized BrandServiceAsync with async HTTP client")

    async def get_available_brands(
        self,
        query_params: Optional[BrandEndpoint.QueryParams] = None,
    ) -> Response:
        endpoint = BrandEndpoint(query=query_params)
        return await self.client.request(endpoint=endpoint)


class TemplateService(TemplateServiceInterface):
    def __init__(self, *, client: HttpClient):
        """Initialize the float service with an HTTP client.

        Args:
            client (HttpClient): The HTTP client instance for making requests
        """
        self.client = client
        logger.debug("Initialized TemplateService with HTTP client")

    def get_brand_templates(
        self,
        query_params: Optional[TemplateListEndpoint.QueryParams] = None,
    ) -> Response:
        endpoint = TemplateListEndpoint(query_params)
        return self.client.request(endpoint=endpoint)

    def download_brand_template(
        self,
        query_params: Optional[TemplateEndpoint.QueryParams] = None,
    ) -> Response:
        endpoint = TemplateEndpoint(query_params)
        return self.client.request(endpoint=endpoint)


class TemplateServiceAsync(TemplateServiceAsyncInterface):
    def __init__(self, *, client: AsyncHttpClient):
        """Initialize the float service with an HTTP client.

        Args:
            client (AsyncHttpClient): The HTTP client instance for making requests
        """
        self.client = client
        logger.debug("Initialized TemplateServiceAsync with HTTP client")

    async def download_brand_template(
        self,
        query_params: Optional[TemplateEndpoint.QueryParams] = None,
    ) -> Response:
        endpoint = TemplateEndpoint(query_params)
        return await self.client.request(endpoint=endpoint)

    async def get_brand_templates(
        self,
        query_params: Optional[TemplateListEndpoint.QueryParams] = None,
    ) -> Response:
        endpoint = TemplateListEndpoint(query_params)
        return await self.client.request(endpoint=endpoint)
