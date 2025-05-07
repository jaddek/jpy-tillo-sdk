from abc import ABC, abstractmethod
import uuid


class SignatureGeneratorInterface(ABC):
    @abstractmethod
    def get_api_key(self) -> str:
        pass

    @abstractmethod
    def get_secret_key_as_bytes(self) -> bytearray:
        pass

    @staticmethod
    @abstractmethod
    def generate_timestamp() -> str:
        pass

    @staticmethod
    @abstractmethod
    def generate_unique_client_request_id() -> uuid.UUID:
        pass

    @abstractmethod
    def generate_signature_string(
            self, endpoint: str, request_type: str, timestamp: str, params: tuple
    ) -> str:
        pass

    @abstractmethod
    def generate_signature(self, seed: str) -> str:
        pass


class SignatureBridgeInterface(ABC):
    @abstractmethod
    def sign(
            self,
            endpoint: str,
            method: str,
            sign_attrs: tuple,
    ):
        pass


class TilloInterface(ABC):
    """Abstract base class defining the interface for Tillo SDK services.

    This interface defines the contract for all Tillo SDK implementations,
    ensuring consistent access to various Tillo services including floats,
    brands, templates, digital cards, physical cards, and webhooks.
    """

    @abstractmethod
    def floats(self):
        """Get the asynchronous floats service instance.

        Returns:
            FloatServiceAsyncInstance: Service for managing float operations asynchronously.
        """
        pass

    @abstractmethod
    def brand(self):
        """Get the brand service instance.

        Returns:
            BrandService: Service for managing brand-related operations.
        """
        pass

    @abstractmethod
    def template(self):
        """Get the template service instance.

        Returns:
            TemplateService: Service for managing template-related operations.
        """
        pass

    @abstractmethod
    def digital_card(self):
        """Get the digital card service instance.

        Returns:
            IssueDigitalCodeService: Service for managing digital card operations.
        """
        pass

    @abstractmethod
    def physical_card(self):
        """Get the physical card service instance.

        Returns:
            PhysicalGiftCardsService: Service for managing physical gift card operations.
        """
        pass

    @abstractmethod
    def webhook(self):
        """Get the webhook service instance.

        Returns:
            WebhookService: Service for managing webhook operations.
        """
        pass
