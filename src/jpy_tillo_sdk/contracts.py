"""Tillo SDK Interface Contracts Module.

This module defines the core interfaces and contracts used throughout the Tillo SDK.
It provides abstract base classes that define the structure and behavior of key
components including signature generation, request signing, and service access.

The module consists of three main interfaces:
- SignatureGeneratorInterface: Defines the contract for signature generation
- SignatureBridgeInterface: Defines the contract for request signing
- TilloInterface: Defines the contract for accessing Tillo services

Example:
    ```python
    # Implementing the TilloInterface
    class TilloSDK(TilloInterface):
        def floats(self):
            return FloatServiceAsync()

        def brand(self):
            return BrandService()

        # ... implement other required methods
    ```
"""

import logging
import uuid
from abc import ABC, abstractmethod
from typing import Any, Optional

from httpx import Response

logger = logging.getLogger("tillo.contracts")


class IssueDigitalCodeServiceInterface(ABC):
    @abstractmethod
    async def issue_digital_code(
        self,
        query_params: Optional[Any] = None,
        body: Optional[Any] = None,
    ) -> Response: ...

    @abstractmethod
    def order_digital_code(
        self,
        query_params: Optional[dict] = None,
        body: Optional[Any] = None,
    ) -> Response: ...

    @abstractmethod
    def check_digital_order(
        self,
        query_params: Optional[dict] = None,
    ) -> Response: ...

    @abstractmethod
    def top_up_digital_code(
        self,
        query_params: Optional[dict] = None,
        body: Optional[Any] = None,
    ): ...

    @abstractmethod
    def cancel_digital_url(
        self,
        query_params: Optional[dict] = None,
        body: Optional[Any] = None,
    ) -> Response: ...

    @abstractmethod
    def cancel_digital_code(
        self,
        query_params: Optional[dict] = None,
        body: Optional[Any] = None,
    ) -> Response: ...

    @abstractmethod
    def reverse_digital_code(
        self,
        query_params: Optional[dict] = None,
        body: Optional[Any] = None,
    ) -> Response: ...

    @abstractmethod
    def check_stock(
        self,
        query_params: Optional[dict] = None,
    ) -> Response: ...

    @abstractmethod
    def check_balance(
        self,
        query_params: Optional[dict] = None,
        body: Optional[Any] = None,
    ) -> Response: ...


class IssueDigitalCodeServiceAsyncInterface(ABC):
    @abstractmethod
    async def issue_digital_code(
        self,
        query_params: Optional[Any] = None,
        body: Optional[Any] = None,
    ) -> Response: ...

    @abstractmethod
    async def order_digital_code(
        self,
        query_params: Optional[dict] = None,
        body: Optional[Any] = None,
    ) -> Response: ...

    @abstractmethod
    async def check_digital_order(
        self,
        query_params: Optional[dict] = None,
    ) -> Response: ...

    @abstractmethod
    async def top_up_digital_code(
        self,
        query_params: Optional[dict] = None,
        body: Optional[Any] = None,
    ) -> Response: ...

    @abstractmethod
    async def cancel_digital_url(
        self,
        query_params: Optional[dict] = None,
        body: Optional[Any] = None,
    ) -> Response: ...

    @abstractmethod
    async def cancel_digital_code(
        self,
        query_params: Optional[dict] = None,
        body: Optional[Any] = None,
    ) -> Response: ...

    @abstractmethod
    async def check_balance(
        self,
        query_params: Optional[dict] = None,
        body: Optional[Any] = None,
    ) -> Response: ...

    @abstractmethod
    async def check_stock(
        self,
        query_params: Optional[dict] = None,
    ) -> Response: ...

    @abstractmethod
    async def reverse_digital_code(
        self,
        query_params: Optional[dict] = None,
        body: Optional[Any] = None,
    ) -> Response: ...


class TemplateServiceInterface(ABC):
    @abstractmethod
    def download_brand_template(
        self,
        query_params: Optional[Any] = None,
    ) -> Response: ...

    @abstractmethod
    def get_brand_templates(
        self,
        query_params: Optional[Any] = None,
    ) -> Response: ...


class TemplateServiceAsyncInterface(ABC):
    @abstractmethod
    async def download_brand_template(
        self,
        query_params: Optional[Any] = None,
    ) -> Response: ...

    @abstractmethod
    async def get_brand_templates(
        self,
        query_params: Optional[Any] = None,
    ) -> Response: ...


class FloatServiceAsyncInterface(ABC):
    @abstractmethod
    async def check_floats(
        self,
        query_params: Optional[Any] = None,
    ) -> Response: ...


class FloatServiceInterface(ABC):
    @abstractmethod
    def check_floats(
        self,
        query_params: Optional[Any] = None,
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
    def generate_signature_string(self, endpoint: str, request_type: str, timestamp: str, params: tuple) -> str:
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
        sign_attrs: tuple,
    ):
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
    def brands(self):
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
    def brands_async(self):
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
    def digital_card(self) -> IssueDigitalCodeServiceInterface:
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
    def digital_card_async(self) -> IssueDigitalCodeServiceAsyncInterface:
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
    def physical_card(self):
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
    def webhook(self):
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
