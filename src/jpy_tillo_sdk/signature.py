"""Tillo SDK Signature Generation Module.

This module provides functionality for generating secure signatures for Tillo API requests.
It implements HMAC-SHA256 signature generation using API keys and secret keys to ensure
secure communication with the Tillo platform.

The module consists of two main classes:
- SignatureGenerator: Core signature generation functionality
- SignatureBridge: High-level interface for request signing

Example:
    ```python
    # Initialize signature generator
    generator = SignatureGenerator(api_key="your_api_key", secret_key="your_secret_key")

    # Create signature bridge
    bridge = SignatureBridge(generator)

    # Generate signature for a request
    api_key, signature, timestamp = bridge.sign(
        endpoint="/api/v1/endpoint",
        method="POST",
        sign_attrs=("param1", "param2")
    )
    ```
"""

import hashlib
import hmac
import logging
import time
import uuid

from .contracts import SignatureBridgeInterface, SignatureGeneratorInterface

logger = logging.getLogger("tillo.signature")


class SignatureGenerator(SignatureGeneratorInterface):
    """Core class for generating secure signatures for Tillo API requests.

    This class handles the generation of HMAC-SHA256 signatures using the provided
    API key and secret key. It implements the signature algorithm required by the
    Tillo API for request authentication.

    Args:
        api_key (str): Your Tillo API key
        secret_key (str): Your Tillo secret key

    Note:
        The API key and secret key should be kept secure and never exposed
        in client-side code or public repositories.
    """

    def __init__(self, api_key: str, secret_key: str):
        """Initialize the signature generator with API credentials.

        Args:
            api_key (str): Your Tillo API key
            secret_key (str): Your Tillo secret key
        """
        self.__api_key = api_key
        self.__secret_key = secret_key
        logger.debug("Initialized SignatureGenerator")

    def get_api_key(self) -> str:
        """Get the API key used for authentication.

        Returns:
            str: The API key
        """
        logger.debug("Retrieving API key")
        return self.__api_key

    def get_secret_key_as_bytes(self) -> bytearray:
        """Get the secret key as bytes for HMAC generation.

        Returns:
            bytes: The secret key encoded as UTF-8 bytes
        """
        logger.debug("Converting secret key to bytes")
        return bytearray(self.__secret_key, "utf-8")

    @staticmethod
    def generate_timestamp() -> str:
        """Generate a Unix timestamp in milliseconds.

        Returns:
            str: Current timestamp in milliseconds as a string
        """
        timestamp = str(int(round(time.time() * 1000)))
        logger.debug("Generated timestamp: %s", timestamp)
        return timestamp

    @staticmethod
    def generate_unique_client_request_id() -> uuid.UUID:
        """Generate a unique identifier for client requests.

        Returns:
            uuid.UUID: A new UUID v4
        """
        request_id = uuid.uuid4()
        logger.debug("Generated request ID: %s", request_id)
        return request_id

    def generate_signature_string(
        self, endpoint: str, request_type: str, timestamp: str, params: tuple[str, ...]
    ) -> str:
        """Generate the string to be signed for the request.

        This method creates the signature string according to Tillo's specification:
        {api_key}-{request_type}-{endpoint}{params}-{timestamp}

        Args:
            endpoint (str): The API endpoint path
            request_type (str): HTTP method (GET, POST, etc.)
            timestamp (str): Current timestamp in milliseconds
            params (tuple): Parameters to include in the signature

        Returns:
            str: The string to be signed
        """
        logger.debug(
            "Generating signature string: %s",
            {
                "endpoint": endpoint,
                "request_type": request_type,
                "timestamp": timestamp,
                "params": params,
            },
        )

        query: str = ""

        if params and len(params):
            for v in params:
                if v is not None:
                    query += f"-{v}"

        signature_string = f"{self.__api_key}-{request_type}-{endpoint}{query}-{timestamp}"
        logger.debug("Generated signature string: %s", signature_string)
        return signature_string

    def generate_signature(self, seed: str) -> str:
        """Generate HMAC-SHA256 signature for the given string.

        Args:
            seed (str): The string to sign

        Returns:
            str: The hexadecimal HMAC-SHA256 signature
        """
        logger.debug("Generating HMAC-SHA256 signature for seed")
        signature_hmac = hmac.new(self.get_secret_key_as_bytes(), bytearray(seed, "utf-8"), hashlib.sha256)
        signature = str(signature_hmac.hexdigest())
        logger.debug("Generated signature: %s", signature)
        return signature


class SignatureBridge(SignatureBridgeInterface):
    """High-level interface for generating request signatures.

    This class provides a simplified interface for generating complete request
    signatures, including the API key, signature, and timestamp required for
    Tillo API authentication.

    Args:
        signature_generator (SignatureGenerator): The signature generator instance

    Note:
        This class acts as a bridge between the HTTP client and the signature
        generation logic, providing a clean interface for request signing.
    """

    __signature_generator: SignatureGenerator

    def __init__(self, signature_generator: SignatureGenerator):
        """Initialize the signature bridge with a signature generator.

        Args:
            signature_generator (SignatureGenerator): The signature generator instance
        """
        self.__signature_generator = signature_generator
        logger.debug("Initialized SignatureBridge")

    def sign(
        self,
        endpoint: str,
        method: str,
        sign_attrs: tuple[str, ...],
    ) -> tuple[str, ...]:
        """Generate a complete signature for an API request.

        This method generates all components needed for request authentication:
        - API key
        - Request signature
        - Timestamp

        Args:
            endpoint (str): The API endpoint path
            method (str): HTTP method (GET, POST, etc.)
            sign_attrs (tuple): Parameters to include in the signature

        Returns:
            tuple: A tuple containing (api_key, signature, timestamp)

        Example:
            ```python
            api_key, signature, timestamp = bridge.sign(
                endpoint="/api/v1/endpoint",
                method="POST",
                sign_attrs=("param1", "param2")
            )
            ```
        """
        logger.info("Generating signature for %s %s", method, endpoint)
        logger.debug(
            "Signature request details: %s",
            {
                "endpoint": endpoint,
                "method": method,
                "sign_attrs": sign_attrs,
            },
        )

        request_timestamp = self.__signature_generator.generate_timestamp()

        signature_string = self.__signature_generator.generate_signature_string(
            endpoint,
            method,
            request_timestamp,
            sign_attrs,
        )

        request_signature = self.__signature_generator.generate_signature(signature_string)

        request_api_key = self.__signature_generator.get_api_key()

        logger.debug(
            "Generated signature components: %s",
            {
                "api_key": request_api_key,
                "timestamp": request_timestamp,
                "signature_length": len(request_signature),
            },
        )

        return request_api_key, request_signature, request_timestamp
