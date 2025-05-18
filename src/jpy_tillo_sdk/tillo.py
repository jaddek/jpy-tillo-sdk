from typing import Any

from .contracts import DigitalCardServiceInterface, TemplateServiceAsyncInterface, TilloInterface
from .domain.brand.services import (
    BrandService,
    BrandServiceAsync,
    TemplateService,
    TemplateServiceAsync,
)
from .domain.digital_card.services import (
    DigitalCardService,
    DigitalCardServiceAsync,
)
from .domain.float.services import FloatService, FloatServiceAsync
from .domain.physical_card.services import PhysicalCardsAsyncService, PhysicalCardsService
from .domain.webhook.services import WebhookService, WebhookServiceAsync
from .errors import AuthorizationErrorInvalidAPITokenOrSecret
from .http_client import AsyncHttpClient, HttpClient
from .http_client_factory import create_client, create_client_async

# TBrandService = TypeVar('TBrandService', bound=ServiceInterface)


class Tillo(TilloInterface):
    """Main Tillo SDK client implementation.

    This class provides the concrete implementation of the TilloInterface,
    handling authentication and providing access to various Tillo services.

    Args:
        api_key (str): The API key for authentication.
        secret (str): The secret key for authentication.
        options (dict | None): Additional configuration options for the client.

    Raises:
        AuthorizationErrorInvalidAPITokenOrSecret: If either api_key or secret is None.
    """

    def __init__(
        self,
        api_key: str,
        secret: str,
        options: dict[str, Any] | None = None,
    ):
        if api_key is None or secret is None:
            raise AuthorizationErrorInvalidAPITokenOrSecret()

        self.__api_key = api_key
        self.__secret = secret
        self.__options = options
        self.__async_http_client: AsyncHttpClient = self.__get_async_client()
        self.__http_client: HttpClient = self.__get_client()

        self.__floats_async: FloatServiceAsync | None = None
        self.__floats: FloatService | None = None
        self.__brands: BrandService | None = None
        self.__brands_async: BrandServiceAsync | None = None
        self.__brand_templates: TemplateService | None = None
        self.__brand_templates_async: TemplateServiceAsync | None = None
        self.__digital_card: DigitalCardService | None = None
        self.__digital_card_async: DigitalCardServiceAsync | None = None
        self.__physical_card: PhysicalCardsService | None = None
        self.__physical_card_async: PhysicalCardsAsyncService | None = None
        self.__webhook: WebhookService | None = None
        self.__webhook_async: WebhookServiceAsync | None = None

    @property
    def floats_async(self) -> FloatServiceAsync:
        """Get the asynchronous floats service instance.

        Returns:
            FloatServiceAsync: Service for managing float operations asynchronously.
        """
        if self.__floats_async is None:
            self.__floats_async = FloatServiceAsync(client=self.__async_http_client)

        return self.__floats_async

    @property
    def floats(self) -> FloatService:
        """Get the synchronous floats service instance.

        Returns:
            FloatService: Service for managing float operations asynchronously.
        """
        if self.__floats is None:
            self.__floats = FloatService(client=self.__http_client)

        return self.__floats

    @property
    def brands(self) -> BrandService:
        """Get the brand service instance.

        Returns:
            BrandService: Service for managing brand-related operations.
        """
        if self.__brands is None:
            self.__brands = BrandService(client=self.__http_client)

        return self.__brands

    @property
    def brands_async(self) -> BrandServiceAsync:
        """Get the brand service instance.

        Returns:
            BrandService: Service for managing brand-related operations.
        """
        if self.__brands_async is None:
            self.__brands_async = BrandServiceAsync(client=self.__async_http_client)

        return self.__brands_async

    @property
    def templates(self) -> TemplateService:
        """Get the template service instance.

        Returns:
            TemplateService: Service for managing brand template-related operations.
        """
        if self.__brand_templates is None:
            self.__brand_templates = TemplateService(client=self.__http_client)

        return self.__brand_templates

    @property
    def templates_async(self) -> TemplateServiceAsyncInterface:
        """Get the template service instance.

        Returns:
            TemplateServiceAsync: Service for managing brand template-related operations.
        """
        if self.__brand_templates_async is None:
            self.__brand_templates_async = TemplateServiceAsync(client=self.__async_http_client)

        return self.__brand_templates_async

    @property
    def digital_card(self) -> DigitalCardServiceInterface:
        """Get the digital card service instance.

        Note: This feature is not yet implemented.

        Returns:
            DigitalCardService: Service for managing digital card operations.
        """
        if self.__digital_card is None:
            self.__digital_card = DigitalCardService(client=self.__http_client)

        return self.__digital_card

    @property
    def digital_card_async(self) -> DigitalCardServiceAsync:
        """Get the digital card service instance asynchronously.

        Note: This feature is not yet implemented.

        Returns:
            DigitalCardServiceAsync: Service for managing digital card operations.

        """
        if self.__digital_card_async is None:
            self.__digital_card_async = DigitalCardServiceAsync(client=self.__async_http_client)

        return self.__digital_card_async

    @property
    def physical_card(self) -> PhysicalCardsService:
        if self.__physical_card is None:
            self.__physical_card = PhysicalCardsService(client=self.__http_client)

        return self.__physical_card

    @property
    def physical_card_async(self) -> PhysicalCardsAsyncService:
        if self.__physical_card_async is None:
            self.__physical_card_async = PhysicalCardsAsyncService(client=self.__async_http_client)

        return self.__physical_card_async

    @property
    def webhook(self) -> None:
        """Get the webhook service instance.

        Note: This feature is not yet implemented.

        Returns:
            WebhookService: Service for managing webhook operations.

        Raises:
            NotImplementedError: This feature is not yet implemented.
        """
        raise NotImplementedError("Webhook service is not yet implemented")

    @property
    async def webhook_async(self) -> None:
        """Get the webhook service instance.

        Note: This feature is not yet implemented.

        Returns:
            WebhookService: Service for managing webhook operations.

        Raises:
            NotImplementedError: This feature is not yet implemented.
        """
        raise NotImplementedError("Webhook service is not yet implemented")

    def __get_async_client(self) -> AsyncHttpClient:
        """Create and return an asynchronous HTTP client.

        Returns:
            AsyncHttpClient: Configured asynchronous HTTP client instance.
        """
        return create_client_async(self.__api_key, self.__secret, self.__options)

    def __get_client(self) -> HttpClient:
        """Create and return a synchronous HTTP client.

        Returns:
            HttpClient: Configured synchronous HTTP client instance.
        """
        return create_client(self.__api_key, self.__secret, self.__options)

    def close_sync(self) -> None:
        self.__http_client.close_connection()

    async def close_async(self) -> None:
        await self.__async_http_client.close_connection()
