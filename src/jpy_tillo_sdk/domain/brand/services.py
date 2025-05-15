import logging

from httpx import Response
from pre_commit.xargs import ArgumentTooLongError

from ...contracts import (
    BrandServiceAsyncInterface,
    BrandServiceInterface,
    BrandsRequestInterface,
    QueryParamsInterface,
    TemplateServiceAsyncInterface,
    TemplateServiceInterface,
)
from ...http_client import AsyncHttpClient, HttpClient
from .endpoints import BrandEndpoint, TemplateEndpoint, TemplateListEndpoint

logger = logging.getLogger("tillo.brand_services")


class BrandsRequest(BrandsRequestInterface):
    @property
    def get_available_brands_query(self) -> type[BrandEndpoint.QueryParams]:
        return BrandEndpoint.QueryParams


class BrandService(BrandServiceInterface, BrandsRequest):
    def __init__(self, *, client: HttpClient):
        """Initialize the float service with an HTTP client.

        Args:
            client (HttpClient): The HTTP client instance for making requests
        """
        self.client = client
        logger.debug("Initialized BrandService with HTTP client")

    def get_available_brands(self, query: QueryParamsInterface) -> Response:
        if not isinstance(query, BrandEndpoint.QueryParams):
            raise ArgumentTooLongError("Argument query should be an instance of BrandEndpoint.QueryParams")

        endpoint: BrandEndpoint = BrandEndpoint(query=query)
        return self.client.request(endpoint=endpoint)


class BrandServiceAsync(BrandServiceAsyncInterface, BrandsRequest):
    def __init__(self, *, client: AsyncHttpClient):
        """Initialize the float service with an HTTP client.

        Args:
            client (AsyncHttpClient): The HTTP client instance for making requests
        """
        self.client = client
        logger.debug("Initialized BrandServiceAsync with async HTTP client")

    async def get_available_brands_async(self, query: QueryParamsInterface) -> Response:
        if not isinstance(query, BrandEndpoint.QueryParams):
            raise ArgumentTooLongError("Argument query should be an instance of BrandEndpoint.QueryParams")

        endpoint = BrandEndpoint(query=query)
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
        query_params: QueryParamsInterface | None = None,
    ) -> Response:
        endpoint = TemplateListEndpoint(query_params)
        return self.client.request(endpoint=endpoint)

    def download_brand_template(
        self,
        query_params: QueryParamsInterface | None = None,
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
        query_params: QueryParamsInterface | None = None,
    ) -> Response:
        endpoint = TemplateEndpoint(query_params)
        return await self.client.request(endpoint=endpoint)

    async def get_brand_templates(
        self,
        query_params: QueryParamsInterface | None = None,
    ) -> Response:
        endpoint = TemplateListEndpoint(query_params)
        return await self.client.request(endpoint=endpoint)
