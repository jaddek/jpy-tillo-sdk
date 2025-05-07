"""HTTP Client Module for Tillo SDK.

This module provides HTTP client implementations for making API requests to the Tillo platform.
It includes both synchronous and asynchronous clients that handle request signing, authentication,
and response processing.

The module consists of three main classes:
- AbstractClient: Base class providing common functionality
- HttpClient: Synchronous client implementation
- AsyncHttpClient: Asynchronous client implementation

Example:
    ```python
    # Synchronous client usage
    client = HttpClient(options, signer)
    response = client.request(endpoint)

    # Asynchronous client usage
    async_client = AsyncHttpClient(options, signer)
    response = await async_client.request(endpoint)
    ```

Note:
    All requests are automatically signed and authenticated using the provided signer.
    The clients handle both GET and POST requests, with appropriate parameter handling
    for each method type.
"""

import logging
from abc import abstractmethod
from typing import Optional

from httpx import Client, AsyncClient, Response

from .endpoint import Endpoint
from .errors import InvalidIpAddress
from .signature import SignatureBridge

logger = logging.getLogger("tillo.http_client")


class AbstractClient:
    """Abstract base class for HTTP clients.

    This class provides common functionality for both synchronous and asynchronous
    HTTP clients, including request signing and header generation. It handles the
    core HTTP request lifecycle and authentication.

    Attributes:
        _signer (SignatureBridge): Service for generating request signatures
        tillo_client_options (dict): Configuration options for the HTTP client

    Note:
        This is an abstract class and should not be instantiated directly.
        Use either HttpClient or AsyncHttpClient instead.
    """

    _signer: SignatureBridge

    def __init__(self, tillo_client_options: dict, signer: SignatureBridge):
        """Initialize the HTTP client.

        Args:
            tillo_client_options (dict): Configuration options for the HTTP client.
                Supported options include:
                - timeout: Request timeout in seconds
                - base_url: Base URL for API requests
                - verify: SSL verification settings
            signer (SignatureBridge): Service for generating request signatures.
                This is used to authenticate requests to the Tillo API.

        Note:
            The tillo_client_options are passed directly to the underlying HTTP client
            (httpx.Client or httpx.AsyncClient).
        """
        self.tillo_client_options = tillo_client_options
        self._signer = signer
        logger.debug("Initialized HTTP client with options: %s", tillo_client_options)

    @abstractmethod
    def request(
        self,
        endpoint: Endpoint,
    ):
        """Make an HTTP request to the specified endpoint.

        Args:
            endpoint (Endpoint): The endpoint to request. This includes:
                - method: HTTP method (GET, POST, etc.)
                - endpoint: API endpoint path
                - params: Query parameters
                - body: Request body (for POST requests)

        Returns:
            Response: The HTTP response from the Tillo API.

        Raises:
            InvalidIpAddress: If the response code is 201
            Exception: For other HTTP or network errors
        """
        pass

    def _get_request_headers(
        self,
        method: str,
        endpoint: str,
        sign_attrs: Optional[tuple] = None,
    ) -> dict:
        """Generate headers for the HTTP request including authentication.

        This method creates the necessary headers for authenticating requests
        to the Tillo API, including the API key, signature, and timestamp.

        Args:
            method (str): HTTP method (GET, POST, etc.)
            endpoint (str): API endpoint path
            sign_attrs (Optional[tuple]): Attributes to include in signature.
                These are used to generate a unique signature for the request.

        Returns:
            dict: Headers for the HTTP request, including:
                - Accept: application/json
                - Content-Type: application/json
                - API-Key: Your API key
                - Signature: Generated request signature
                - Timestamp: Request timestamp
                - User-Agent: SDK identifier
        """
        logger.debug("Generating headers for %s %s", method, endpoint)

        (request_api_key, request_signature, request_timestamp) = self._signer.sign(
            endpoint,
            method,
            sign_attrs,
        )

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "API-Key": request_api_key,
            "Signature": request_signature,
            "Timestamp": request_timestamp,
            "User-Agent": "JpyTilloSDKClient/0.2",
        }

        logger.debug(
            "Generated headers: %s",
            {k: v for k, v in headers.items() if k != "Signature"},
        )
        return headers

    def _catch_non_200_response(self, code: int) -> None:
        """Handle non-200 HTTP response codes.

        This method checks the response code and raises appropriate exceptions
        for specific error conditions.

        Args:
            code (int): HTTP status code from the response

        Raises:
            InvalidIpAddress: If the response code is 201, indicating an IP
                address validation error
        """
        logger.debug("Checking response code: %d", code)
        if code == 201:
            logger.error("Received 201 response code, raising InvalidIpAddress")
            raise InvalidIpAddress()


class AsyncHttpClient(AbstractClient):
    """Asynchronous HTTP client for making API requests.

    This client provides asynchronous methods for making HTTP requests to the
    Tillo API. It uses httpx.AsyncClient for non-blocking I/O operations.

    Example:
        ```python
        async def make_request():
            client = AsyncHttpClient(options, signer)
            response = await client.request(endpoint)
            return response.json()
        ```
    """

    async def request(
        self,
        endpoint: Endpoint,
    ) -> Response:
        """Make an asynchronous HTTP request to the specified endpoint.

        This method handles the complete request lifecycle for asynchronous
        requests, including header generation, request signing, and response
        processing.

        Args:
            endpoint (Endpoint): The endpoint to request. This includes:
                - method: HTTP method (GET, POST, etc.)
                - endpoint: API endpoint path
                - params: Query parameters
                - body: Request body (for POST requests)

        Returns:
            Response: The HTTP response from the Tillo API.

        Raises:
            InvalidIpAddress: If the response code is 201
            Exception: For other HTTP or network errors

        Note:
            This method should be called with await in an async context.
        """
        json: Optional[dict] = None

        logger.info("Making async request to %s %s", endpoint.method, endpoint.endpoint)
        logger.debug(
            "Request details: %s",
            {
                "method": endpoint.method,
                "endpoint": endpoint.endpoint,
                "params": endpoint.params,
                "route": endpoint.route,
            },
        )

        sign_attrs = endpoint.get_sign_attrs()

        headers = self._get_request_headers(
            endpoint.method,
            endpoint.endpoint,
            sign_attrs,
        )

        logger.debug(
            "Request headers prepared with method <%s>, endpoint <%s>, signing attributes <%s>",
            endpoint.method,
            endpoint.endpoint,
            sign_attrs if sign_attrs is not None else "No arguments",
        )

        try:
            async with AsyncClient(**self.tillo_client_options) as client:
                logger.debug("Sending async request to %s", endpoint.route)
                response = await client.request(
                    url=endpoint.route,
                    method=endpoint.method,
                    params=endpoint.params,
                    json=json,
                    headers=headers,
                )
                logger.debug(
                    "Received response with status code: %d", response.status_code
                )

            self._catch_non_200_response(response.status_code)

            logger.info("Successfully completed async request to %s", endpoint.endpoint)
            return response

        except Exception as e:
            logger.error(
                "Error during async request to %s: %s", endpoint.endpoint, str(e)
            )
            raise


class HttpClient(AbstractClient):
    """Synchronous HTTP client for making API requests.

    This client provides synchronous methods for making HTTP requests to the
    Tillo API. It uses httpx.Client for blocking I/O operations.

    Example:
        ```python
        def make_request():
            client = HttpClient(options, signer)
            response = client.request(endpoint)
            return response.json()
        ```
    """

    def request(
        self,
        endpoint: Endpoint,
    ) -> Response:
        """Make a synchronous HTTP request to the specified endpoint.

        This method handles the complete request lifecycle for synchronous
        requests, including header generation, request signing, and response
        processing.

        Args:
            endpoint (Endpoint): The endpoint to request. This includes:
                - method: HTTP method (GET, POST, etc.)
                - endpoint: API endpoint path
                - params: Query parameters
                - body: Request body (for POST requests)

        Returns:
            Response: The HTTP response from the Tillo API.

        Raises:
            Exception: For HTTP or network errors

        Note:
            This method blocks until the request is complete.
        """
        json: Optional[dict] = None

        logger.info("Making sync request to %s %s", endpoint.method, endpoint.endpoint)
        logger.debug(
            "Request details: %s",
            {
                "method": endpoint.method,
                "endpoint": endpoint.endpoint,
                "params": endpoint.params,
                "route": endpoint.route,
            },
        )

        sign_attrs = None

        if endpoint.is_body_not_empty():
            logger.debug("Using request body for signing: %s", endpoint.body)
            sign_attrs = endpoint.body.get_sign_attrs()
            json = endpoint.body.get_as_dict()
        else:
            logger.debug("Using query parameters for signing: %s", endpoint.query)
            if endpoint.query:
                sign_attrs = endpoint.query.get_sign_attrs()

        headers = self._get_request_headers(
            endpoint.method,
            endpoint.endpoint,
            sign_attrs,
        )

        logger.debug(
            "Request headers prepared with method <%s>, endpoint <%s>, signing attributes <%s>",
            endpoint.method,
            endpoint.endpoint,
            sign_attrs if sign_attrs is not None else "No arguments",
        )

        try:
            with Client(**self.tillo_client_options) as client:
                logger.debug("Sending sync request to %s", endpoint.route)
                response = client.request(
                    url=endpoint.route,
                    method=endpoint.method,
                    params=endpoint.params,
                    json=json,
                    headers=headers,
                )
                logger.debug(
                    "Received response with status code: %d", response.status_code
                )

            logger.info("Successfully completed sync request to %s", endpoint.endpoint)
            return response

        except Exception as e:
            logger.error(
                "Error during sync request to %s: %s", endpoint.endpoint, str(e)
            )
            raise
