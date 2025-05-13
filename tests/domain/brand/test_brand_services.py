import pytest
from httpx import Response

from jpy_tillo_sdk.domain.brand.endpoints import (
    BrandEndpoint,
    TemplateListEndpoint,
    TemplateEndpoint,
)
from jpy_tillo_sdk.domain.brand.services import (
    BrandService,
    TemplateService,
    BrandServiceAsync,
    TemplateServiceAsync,
)


class TestBrandServiceAsync:
    @pytest.mark.asyncio
    async def test_get_available_brands_async(self, mock_async_http_client):
        service = BrandServiceAsync(client=mock_async_http_client)
        response = await service.get_available_brands()

        mock_async_http_client.request.assert_called_once()
        assert isinstance(response, Response)


class TestTemplateServiceAsync:
    @pytest.mark.asyncio
    async def test_get_brand_templates_async(self, mock_async_http_client):
        service = TemplateServiceAsync(client=mock_async_http_client)
        response = await service.get_brand_templates()

        mock_async_http_client.request.assert_called_once()
        assert isinstance(response, Response)

    @pytest.mark.asyncio
    async def test_download_brand_template_async(self, mock_async_http_client):
        service = TemplateServiceAsync(client=mock_async_http_client)
        response = await service.download_brand_template()

        mock_async_http_client.request.assert_called_once()
        assert isinstance(response, Response)


class TestBrandService:
    def test_get_available_brands(self, mock_http_client):
        service = BrandService(client=mock_http_client)
        response = service.get_available_brands()

        mock_http_client.request.assert_called_once()
        assert isinstance(response, Response)


class TestTemplateService:
    def test_get_brand_templates(self, mock_http_client):
        service = TemplateService(client=mock_http_client)
        response = service.get_brand_templates()

        mock_http_client.request.assert_called_once()
        assert isinstance(response, Response)

    def test_download_brand_template(self, mock_http_client):
        service = TemplateService(client=mock_http_client)
        response = service.download_brand_template()

        mock_http_client.request.assert_called_once()
        assert isinstance(response, Response)


@pytest.mark.parametrize(
    "service,method_name,endpoint_class",
    [
        (BrandService, "get_available_brands", BrandEndpoint),
        (TemplateService, "get_brand_templates", TemplateListEndpoint),
        (TemplateService, "download_brand_template", TemplateEndpoint),
    ],
)
def test_service_methods_endpoint_types(
    service, method_name, endpoint_class, mock_http_client
):
    instance = service(client=mock_http_client)

    method = getattr(instance, method_name)
    method()

    assert isinstance(mock_http_client.request.call_args[1]["endpoint"], endpoint_class)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "service,method_name,endpoint_class",
    [
        (BrandServiceAsync, "get_available_brands", BrandEndpoint),
        (TemplateServiceAsync, "get_brand_templates", TemplateListEndpoint),
        (TemplateServiceAsync, "download_brand_template", TemplateEndpoint),
    ],
)
async def test_service_methods_endpoint_types_async(
    service, method_name, endpoint_class, mock_async_http_client
):
    instance = service(client=mock_async_http_client)

    method = getattr(instance, method_name)
    await method()

    assert isinstance(
        mock_async_http_client.request.call_args[1]["endpoint"], endpoint_class
    )
