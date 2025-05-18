import logging
import uuid
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Generic, TypeVar

from httpx import Response

if TYPE_CHECKING:
    from jpy_tillo_sdk.http_client import AsyncHttpClient, HttpClient

logger = logging.getLogger("tillo.contracts")


class EndpointInterface(ABC):
    @property
    @abstractmethod
    def method(self) -> str: ...

    @property
    @abstractmethod
    def endpoint(self) -> str: ...

    @property
    @abstractmethod
    def route(self) -> str: ...

    @property
    @abstractmethod
    def body(self) -> Any: ...

    @property
    @abstractmethod
    def query(self) -> Any: ...

    @property
    @abstractmethod
    def sign_attrs(self) -> tuple[str, ...]: ...


@dataclass(frozen=True)
class SignatureAttributesInterface(ABC):
    @property
    @abstractmethod
    def sign_attrs(self) -> tuple[str, ...]: ...


class ClientInterface(ABC):
    @abstractmethod
    def request(
        self,
        endpoint: EndpointInterface,
    ) -> Response: ...


TClient = TypeVar("TClient", bound=ClientInterface)


class ServiceInterface(ABC, Generic[TClient]):
    def __init__(self, *, client: TClient):
        self._client: TClient = client

    @property
    @abstractmethod
    def client(self) -> TClient: ...


class SyncServiceInterface(ServiceInterface["HttpClient"], ABC):
    @property
    def client(self) -> "HttpClient":
        return self._client


class AsyncServiceInterface(ServiceInterface["AsyncHttpClient"], ABC):
    @property
    def client(self) -> "AsyncHttpClient":
        return self._client


class TemplateServiceInterface(SyncServiceInterface, ABC):
    @abstractmethod
    def download_brand_template(
        self,
        query: Any = None,
    ) -> Response: ...

    @abstractmethod
    def get_templates_list(
        self,
        query: Any = None,
    ) -> Response: ...


class TemplateServiceAsyncInterface(AsyncServiceInterface, ABC):
    @abstractmethod
    async def download_brand_template(
        self,
        query: Any = None,
    ) -> Response: ...

    @abstractmethod
    async def get_brand_templates(
        self,
        query: Any = None,
    ) -> Response: ...


class FloatServiceAsyncInterface(AsyncServiceInterface, ABC):
    @abstractmethod
    async def check_floats(
        self,
        query: Any = None,
    ) -> Response: ...


class FloatServiceInterface(SyncServiceInterface, ABC):
    @abstractmethod
    def check_floats(
        self,
        query: Any = None,
    ) -> Response: ...


class BrandServiceInterface(SyncServiceInterface, ABC):
    @abstractmethod
    def get_available_brands(
        self,
        query: Any = None,
    ) -> Response: ...


class BrandServiceAsyncInterface(AsyncServiceInterface, ABC):
    @abstractmethod
    async def get_available_brands(
        self,
        query: Any = None,
    ) -> Response: ...


class DigitalCardServiceInterface(SyncServiceInterface, ABC):
    @abstractmethod
    def issue_digital_code(
        self,
        query: Any = None,
        body: Any = None,
    ) -> Response: ...

    @abstractmethod
    def order_digital_code(
        self,
        query: Any = None,
        body: Any = None,
    ) -> Response: ...

    @abstractmethod
    def check_digital_order(
        self,
        query: Any = None,
    ) -> Response: ...

    @abstractmethod
    def top_up_digital_code(
        self,
        query: Any = None,
        body: Any = None,
    ) -> Response: ...

    @abstractmethod
    def cancel_digital_url(
        self,
        query: Any = None,
        body: Any = None,
    ) -> Response: ...

    @abstractmethod
    def cancel_digital_code(
        self,
        query: Any = None,
        body: Any = None,
    ) -> Response: ...

    @abstractmethod
    def reverse_digital_code(
        self,
        query: Any = None,
        body: Any = None,
    ) -> Response: ...

    @abstractmethod
    def check_stock(
        self,
        query: Any = None,
    ) -> Response: ...

    @abstractmethod
    def check_balance(
        self,
        query: Any = None,
        body: Any = None,
    ) -> Response: ...


class DigitalCardServiceAsyncInterface(AsyncServiceInterface, ABC):
    @abstractmethod
    async def issue_digital_code(
        self,
        query: Any = None,
        body: Any = None,
    ) -> Response: ...

    @abstractmethod
    async def order_digital_code(
        self,
        query: Any = None,
        body: Any = None,
    ) -> Response: ...

    @abstractmethod
    async def check_digital_order(
        self,
        query: Any = None,
    ) -> Response: ...

    @abstractmethod
    async def top_up_digital_code(
        self,
        query: Any = None,
        body: Any = None,
    ) -> Response: ...

    @abstractmethod
    async def cancel_digital_url(
        self,
        query: Any = None,
        body: Any = None,
    ) -> Response: ...

    @abstractmethod
    async def cancel_digital_code(
        self,
        query: Any = None,
        body: Any = None,
    ) -> Response: ...

    @abstractmethod
    async def check_balance(
        self,
        query: Any = None,
        body: Any = None,
    ) -> Response: ...

    @abstractmethod
    async def check_stock(
        self,
        query: Any = None,
    ) -> Response: ...

    @abstractmethod
    async def reverse_digital_code(
        self,
        query: Any = None,
        body: Any = None,
    ) -> Response: ...


class PhysicalCardsAsyncServiceInterface(AsyncServiceInterface, ABC):
    @abstractmethod
    def activate_physical_card_async(
        self,
        query: Any = None,
        body: Any = None,
    ) -> Response: ...

    @abstractmethod
    async def cancel_activate_physical_card_async(
        self,
        query: Any = None,
        body: Any = None,
    ) -> Response: ...

    @abstractmethod
    async def order_status_async(
        self,
        body: Any,
    ) -> Response: ...

    @abstractmethod
    async def cash_out_original_transaction_physical_card_async(
        self,
        query: Any = None,
        body: Any = None,
    ) -> Response: ...

    @abstractmethod
    async def balance_check_physical_async(
        self,
        query: Any = None,
        body: Any = None,
    ) -> Response: ...

    @abstractmethod
    async def order_physical_card_async(
        self,
        query: Any = None,
        body: Any = None,
    ) -> Response: ...

    @abstractmethod
    async def cancel_top_up_on_physical_card_async(
        self,
        query: Any = None,
        body: Any = None,
    ) -> Response: ...

    @abstractmethod
    async def top_up_physical_card_async(
        self,
        query: Any = None,
        body: Any = None,
    ) -> Response: ...

    @abstractmethod
    async def fulfil_physical_card_order_async(
        self,
        body: Any = None,
    ) -> Response: ...


class PhysicalCardsServiceInterface(SyncServiceInterface, ABC):
    @abstractmethod
    def activate_physical_card(
        self,
        query: Any = None,
        body: Any = None,
    ) -> Response: ...

    @abstractmethod
    def cancel_activate_physical_card(
        self,
        query: Any = None,
        body: Any = None,
    ) -> Response: ...

    @abstractmethod
    def order_status(
        self,
        body: Any = None,
    ) -> Response: ...

    @abstractmethod
    def cash_out_original_transaction(
        self,
        query: Any = None,
        body: Any = None,
    ) -> Response: ...

    @abstractmethod
    def balance_check_physical(
        self,
        query: Any = None,
        body: Any = None,
    ) -> Response: ...

    @abstractmethod
    def order_physical_card(
        self,
        query: Any = None,
        body: Any = None,
    ) -> Response: ...

    @abstractmethod
    def cancel_top_up(
        self,
        body: Any = None,
    ) -> Response: ...

    @abstractmethod
    def top_up_physical_card(
        self,
        body: Any = None,
    ) -> Response: ...

    @abstractmethod
    def fulfil_order(
        self,
        body: Any = None,
    ) -> Response: ...


class SignatureGeneratorInterface(ABC):
    """Interface for generating secure signatures for Tillo API requests.

    This interface defines the contract for classes that generate HMAC-SHA256
    signatures used in Tillo API authentication. Implementations must provide
    methods for key management, timestamp generation, and signature creation.

    Example:
        ```python
        class MySignatureGenerator(SignatureGeneratorInterface):
            def get_api_key(self) -> str:
                return "my_api_key"

            # ... implement other required methods
        ```
    """

    @abstractmethod
    def get_api_key(self) -> str:
        """Get the API key used for authentication.

        Returns:
            str: The API key used for Tillo API authentication
        """
        ...

    @abstractmethod
    def get_secret_key_as_bytes(self) -> bytearray:
        """Get the secret key as bytes for HMAC generation.

        Returns:
            bytearray: The secret key encoded as UTF-8 bytes
        """
        ...

    @staticmethod
    @abstractmethod
    def generate_timestamp() -> str:
        """Generate a Unix timestamp in milliseconds.

        Returns:
            str: Current timestamp in milliseconds as a string
        """
        ...

    @staticmethod
    @abstractmethod
    def generate_unique_client_request_id() -> uuid.UUID:
        """Generate a unique identifier for client requests.

        Returns:
            uuid.UUID: A new UUID v4 for request identification
        """
        ...

    @abstractmethod
    def generate_signature_string(
        self, endpoint: str, request_type: str, timestamp: str, params: tuple[str, ...]
    ) -> str:
        """Generate the string to be signed for the request.

        Args:
            endpoint (str): The API endpoint path
            request_type (str): HTTP method (GET, POST, etc.)
            timestamp (str): Current timestamp in milliseconds
            params (tuple): Parameters to include in the signature

        Returns:
            str: The string to be signed according to Tillo's specification
        """
        ...

    @abstractmethod
    def generate_signature(self, seed: str) -> str:
        """Generate HMAC-SHA256 signature for the given string.

        Args:
            seed (str): The string to sign

        Returns:
            str: The hexadecimal HMAC-SHA256 signature
        """
        ...


class SignatureBridgeInterface(ABC):
    """Interface for generating complete request signatures.

    This interface defines the contract for classes that generate complete
    request signatures, including API key, signature, and timestamp. It acts
    as a bridge between the HTTP client and signature generation logic.

    Example:
        ```python
        class MySignatureBridge(SignatureBridgeInterface):
            def sign(self, endpoint: str, method: str, sign_attrs: tuple):
                # Implementation
                return api_key, signature, timestamp
        ```
    """

    @abstractmethod
    def sign(
        self,
        endpoint: str,
        method: str,
        sign_attrs: tuple[str, ...],
    ) -> tuple[str, ...]:
        """Generate a complete signature for an API request.

        Args:
            endpoint (str): The API endpoint path
            method (str): HTTP method (GET, POST, etc.)
            sign_attrs (tuple): Parameters to include in the signature

        Returns:
            tuple: A tuple containing (api_key, signature, timestamp)
        """
        ...


class TilloInterface(ABC):
    """Abstract base class defining the interface for Tillo SDK services.

    This interface defines the contract for all Tillo SDK implementations,
    ensuring consistent access to various Tillo services including floats,
    brands, templates, digital cards, physical cards, and webhooks.

    Example:
        ```python
        class TilloSDK(TilloInterface):
            def floats(self):
                return FloatServiceAsync()

            def brand(self):
                return BrandService()

            # ... implement other required methods
        ```
    """

    @property
    @abstractmethod
    def floats(self) -> FloatServiceInterface:
        """Get the floats service instance.

        Returns:
            FloatService: Service for managing float operations.

        Example:
            ```python
            float_service = tillo.floats()
            balance =  float_service.get_balance()
            ```
        """
        ...

    @property
    @abstractmethod
    def floats_async(self) -> FloatServiceAsyncInterface:
        """Get the asynchronous floats service instance.

        Returns:
            FloatServiceAsync: Service for managing float operations asynchronously.

        Example:
            ```python
            float_service = tillo.floats()
            balance = float_service.get_balance()
            ```
        """
        ...

    @property
    @abstractmethod
    def brands(self) -> BrandServiceInterface:
        """Get the brand service instance.

        Returns:
            BrandService: Service for managing brand-related operations.

        Example:
            ```python
            brand_service = tillo.brands()
            brand_info = brand_service.get_brand_details()
            ```
        """
        ...

    @property
    @abstractmethod
    def brands_async(self) -> BrandServiceAsyncInterface:
        """Get the brand service instance.

        Returns:
            BrandServiceAsync: Service for managing brand-related operations asynchronously.

        Example:
            ```python
            brand_service = tillo.brands()
            brand_info = brand_service.get_brand_details()
            ```
        """
        ...

    @property
    @abstractmethod
    def templates(self) -> TemplateServiceInterface:
        """Get the template service instance.

        Returns:
            TemplateService: Service for managing template-related operations.

        Example:
            ```python
            template_service = tillo.templates()
            templates = template_service.list_templates()
            ```
        """
        ...

    @property
    @abstractmethod
    def templates_async(self) -> TemplateServiceAsyncInterface:
        """Get the template service instance.

        Returns:
            TemplateService: Service for managing template-related operations.

        Example:
            ```python
            template_service = tillo.templates_async()
            templates = template_service.list_templates()
            ```
        """
        ...

    @property
    @abstractmethod
    def digital_card(self) -> DigitalCardServiceInterface:
        """Get the digital card service instance.

        Returns:
            IssueDigitalCodeService: Service for managing digital card operations.

        Example:
            ```python
            digital_card_service = tillo.digital_card()
            card = digital_card_service.issue_card(amount=50.00)
            ```
        """
        ...

    @property
    @abstractmethod
    def digital_card_async(self) -> DigitalCardServiceAsyncInterface:
        """Get the digital card service instance.

        Returns:
            IssueDigitalCodeServiceAsync: Service for managing digital card operations.

        Example:
            ```python
            digital_card_service = tillo.digital_card_async()
            card = digital_card_service.issue_card(amount=50.00)
            ```
        """
        ...

    @property
    @abstractmethod
    def physical_card(self) -> PhysicalCardsServiceInterface:
        """Get the physical card service instance.

        Returns:
            PhysicalGiftCardsService: Service for managing physical gift card operations.

        Example:
            ```python
            physical_card_service = tillo.physical_card()
            card = physical_card_service.order_card(amount=100.00)
            ```
        """
        ...

    @property
    @abstractmethod
    def physical_card_async(self) -> PhysicalCardsAsyncServiceInterface:
        """Get the physical card service instance.

        Returns:
            PhysicalGiftCardsService: Service for managing physical gift card operations.

        Example:
            ```python
            physical_card_service = tillo.physical_card_async()
            card = physical_card_service.order_card(amount=100.00)
            ```
        """
        ...

    @property
    @abstractmethod
    def webhook(self) -> None:
        """Get the webhook service instance.

        Returns:
            WebhookService: Service for managing webhook-related operations.

        Example:
            ```python
            webhook_service = tillo.webhook()
            webhooks = webhook_service.list_webhooks()
            ```
        """
        ...
