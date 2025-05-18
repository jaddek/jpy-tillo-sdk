from typing import Any
from unittest.mock import AsyncMock, Mock

import pytest
from httpx import Response

from jpy_tillo_sdk.domain.brand.endpoints import (
    BrandEndpoint,
    BrandEndpointRequestQuery,
    DownloadBrandTemplateEndpoint,
    TemplatesListEndpoint,
)
from jpy_tillo_sdk.domain.brand.services import (
    BrandService,
    BrandServiceAsync,
    TemplateService,
    TemplateServiceAsync,
)


class TestBrandServiceAsync:
    @pytest.mark.asyncio  # type: ignore[misc]
    async def test_get_available_brands_async(self, mock_async_http_client: AsyncMock) -> None:
        service = BrandServiceAsync(client=mock_async_http_client)
        response = await service.get_available_brands(BrandEndpointRequestQuery())

        mock_async_http_client.request.assert_called_once()
        assert isinstance(response, Response)


class TestTemplateServiceAsync:
    @pytest.mark.asyncio  # type: ignore[misc]
    async def test_get_brand_templates_async(self, mock_async_http_client: AsyncMock) -> None:
        service = TemplateServiceAsync(client=mock_async_http_client)
        response = await service.get_brand_templates()

        mock_async_http_client.request.assert_called_once()
        assert isinstance(response, Response)

    @pytest.mark.asyncio  # type: ignore[misc]
    async def test_download_brand_template_async(self, mock_async_http_client: AsyncMock) -> None:
        service = TemplateServiceAsync(client=mock_async_http_client)
        response = await service.download_brand_template()

        mock_async_http_client.request.assert_called_once()
        assert isinstance(response, Response)


class TestBrandService:
    def test_get_available_brands(self, mock_http_client: Mock) -> None:
        service = BrandService(client=mock_http_client)
        response = service.get_available_brands(BrandEndpointRequestQuery())

        mock_http_client.request.assert_called_once()
        assert isinstance(response, Response)


class TestTemplateService:
    def test_get_brand_templates(self, mock_http_client: Mock) -> None:
        service = TemplateService(client=mock_http_client)
        response = service.get_templates_list()

        mock_http_client.request.assert_called_once()
        assert isinstance(response, Response)

    def test_download_brand_template(self, mock_http_client: Mock) -> None:
        service = TemplateService(client=mock_http_client)
        response = service.download_brand_template()

        mock_http_client.request.assert_called_once()
        assert isinstance(response, Response)


@pytest.mark.parametrize(  # type: ignore[misc]
    "service,method_name,endpoint_class",
    [
        (TemplateService, "get_templates_list", TemplatesListEndpoint),
        (TemplateService, "download_brand_template", DownloadBrandTemplateEndpoint),
    ],
)
def test_service_methods_endpoint_types(
    service: type[Any], method_name: str, endpoint_class: type[Any], mock_http_client: Mock
) -> None:
    instance = service(client=mock_http_client)

    method = getattr(instance, method_name)
    method()

    assert isinstance(mock_http_client.request.call_args[1]["endpoint"], endpoint_class)


def test_brand_service_methods_endpoint_types(mock_http_client: Mock) -> None:
    instance = BrandService(client=mock_http_client)
    instance.get_available_brands(BrandEndpointRequestQuery())

    assert isinstance(mock_http_client.request.call_args[1]["endpoint"], BrandEndpoint)


@pytest.mark.asyncio  # type: ignore[misc]
@pytest.mark.parametrize(  # type: ignore[misc]
    "service,method_name,endpoint_class",
    [
        (TemplateServiceAsync, "get_brand_templates", TemplatesListEndpoint),
        (TemplateServiceAsync, "download_brand_template", DownloadBrandTemplateEndpoint),
    ],
)
async def test_service_methods_endpoint_types_async(
    service: type[Any], method_name: str, endpoint_class: type[Any], mock_async_http_client: Mock
) -> None:
    instance = service(client=mock_async_http_client)

    method = getattr(instance, method_name)
    await method()

    assert isinstance(mock_async_http_client.request.call_args[1]["endpoint"], endpoint_class)


@pytest.mark.asyncio  # type: ignore[misc]
async def test_brand_service_methods_endpoint_types_async(mock_async_http_client: AsyncMock) -> None:
    instance = BrandServiceAsync(client=mock_async_http_client)
    await instance.get_available_brands(BrandEndpointRequestQuery())

    assert isinstance(mock_async_http_client.request.call_args[1]["endpoint"], BrandEndpoint)
