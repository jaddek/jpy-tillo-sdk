from typing import Optional

from .contracts import TilloInterface
from .domain.float.services import FloatServiceAsync, FloatService
from .errors import AuthorizationErrorInvalidAPITokenOrSecret
from .http_client import AsyncHttpClient, HttpClient
from .http_client_factory import create_client_async, create_client


class Tillo(TilloInterface):
    """Main Tillo SDK client implementation.

    This class provides the concrete implementation of the TilloInterface,
    handling authentication and providing access to various Tillo services.

    Args:
        api_key (str): The API key for authentication.
        secret (str): The secret key for authentication.
        options (Optional[dict]): Additional configuration options for the client.

    Raises:
        AuthorizationErrorInvalidAPITokenOrSecret: If either api_key or secret is None.
    """

    def __init__(
        self,
        api_key: str,
        secret: str,
        options: Optional[dict] = None,
    ):
        if api_key is None or secret is None:
            raise AuthorizationErrorInvalidAPITokenOrSecret()

        self.__api_key = api_key
        self.__secret = secret
        self.__options = options
        self.__async_http_client = self.__get_async_client()
        self.__http_client = self.__get_client()

        self._floats_async: FloatServiceAsync | None = None
        self._floats: FloatService | None = None

    @property
    def floats_async(self) -> FloatServiceAsync:
        """Get the asynchronous floats service instance.

        Returns:
            FloatServiceAsync: Service for managing float operations asynchronously.
        """
        if self._floats_async is None:
            self._floats_async = FloatServiceAsync(client=self.__async_http_client)

        return self._floats_async

    @property
    def floats(self) -> FloatService | None:
        """Get the synchronous floats service instance.

        Returns:
            FloatService: Service for managing float operations asynchronously.
        """
        if self._floats is None:
            self._floats = FloatService(client=self.__http_client)

        return self._floats

    def brand(self):
        """Get the brand service instance.

        Returns:
            BrandService: Service for managing brand-related operations.
        """
        pass

    def template(self):
        """Get the template service instance.

        Returns:
            TemplateService: Service for managing brand template-related operations.
        """
        pass

    def digital_card(self):
        """Get the digital card service instance.

        Returns:
            IssueDigitalCodeService: Service for managing digital card operations.
        """
        pass

    def physical_card(self):
        """Get the physical card service instance.

        Returns:
            PhysicalGiftCardsService: Service for managing physical gift card operations.
        """
        pass

    def webhook(self):
        """Get the webhook service instance.

        Returns:
            WebhookService: Service for managing webhook operations.
        """
        pass

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
