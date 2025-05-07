import pytest
from httpx import Response

from jpy_tillo_sdk.domain.brand.endpoints import (
    BrandEndpoint,
    TemplateListEndpoint,
    TemplateEndpoint,
)
from jpy_tillo_sdk.domain.brand.services import BrandService, TemplateService


class TestBrandAssetsService:
    def test_get_available_brands(self, mock_http_client):
        response = BrandService.get_available_brands(mock_http_client)

        mock_http_client.request.assert_called_once()
        assert isinstance(response, Response)

    @pytest.mark.asyncio
    async def test_get_available_brands_async(self, mock_async_http_client):
        response = await BrandService.get_available_brands_async(mock_async_http_client)

        mock_async_http_client.request.assert_called_once()
        assert isinstance(response, Response)

    def test_get_brand_templates(self, mock_http_client):
        response = TemplateService.get_brand_templates(mock_http_client)

        mock_http_client.request.assert_called_once()
        assert isinstance(response, Response)

    @pytest.mark.asyncio
    async def test_get_brand_templates_async(self, mock_async_http_client):
        response = await TemplateService.get_brand_templates_async(
            mock_async_http_client
        )

        mock_async_http_client.request.assert_called_once()
        assert isinstance(response, Response)

    def test_download_brand_template(self, mock_http_client):
        response = TemplateService.download_brand_template(mock_http_client)

        mock_http_client.request.assert_called_once()
        assert isinstance(response, Response)

    @pytest.mark.asyncio
    async def test_download_brand_template_async(self, mock_async_http_client):
        response = await TemplateService.download_brand_template_async(
            mock_async_http_client
        )

        mock_async_http_client.request.assert_called_once()
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
    method = getattr(service, method_name)
    method(mock_http_client)

    assert isinstance(mock_http_client.request.call_args[1]["endpoint"], endpoint_class)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "service,method_name,endpoint_class",
    [
        (BrandService, "get_available_brands_async", BrandEndpoint),
        (TemplateService, "get_brand_templates_async", TemplateListEndpoint),
        (TemplateService, "download_brand_template_async", TemplateEndpoint),
    ],
)
async def test_service_methods_endpoint_types_async(
    service, method_name, endpoint_class, mock_async_http_client
):
    method = getattr(service, method_name)
    await method(mock_async_http_client)

    assert isinstance(
        mock_async_http_client.request.call_args[1]["endpoint"], endpoint_class
    )
