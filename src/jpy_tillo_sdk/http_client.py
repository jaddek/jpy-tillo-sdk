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
from typing import Any

from httpx import AsyncClient, Client, Response

from .endpoint import AbstractBodyRequest, Endpoint
from .errors import AuthenticationFailed, InvalidIpAddress, UnprocessableContent, ValidationError
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

    def __init__(self, tillo_client_options: dict[str, Any] | None, signer: SignatureBridge):
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
        self.tillo_client_options = tillo_client_options or {}
        self._signer = signer
        logger.debug("Initialized HTTP client with options: %s", tillo_client_options)

    @abstractmethod
    def request(
        self,
        endpoint: Endpoint,
    ) -> Response:
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
        sign_attrs: tuple[str, ...] = (),
    ) -> dict[str, Any]:
        """Generate headers for the HTTP request including authentication.

        This method creates the necessary headers for authenticating requests
        to the Tillo API, including the API key, signature, and timestamp.

        Args:
            method (str): HTTP method (GET, POST, etc.)
            endpoint (str): API endpoint path
            sign_attrs (tuple | None): Attributes to include in signature.
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
            {k: v for k, v in headers.items() if k not in ["Signature", "API-Key"]},
        )
        return headers

    def _catch_non_200_response(
        self,
        response: Response,
    ) -> None:
        """Handle non-200 HTTP response codes.

        This method checks the response code and raises appropriate exceptions
        for specific error conditions.

        Args:
            status_code (int): HTTP status code from the response

        Raises:
            InvalidIpAddress: If the response code is 201, indicating an IP
                address validation error
        """

        status_code = response.status_code
        content_code = response.json().get("code")

        logger.debug(
            "Checking response code and content code: %d - %s",
            status_code,
            content_code,
        )

        if status_code == 201:
            logger.error("Received 201 response code, raising InvalidIpAddress")
            raise InvalidIpAddress(response)
        elif status_code == 422:
            if content_code == UnprocessableContent.TILLO_ERROR_CODE:
                logger.error("Received 422 response code, invalid data")
                raise UnprocessableContent(response)
            elif content_code == UnprocessableContent.TILLO_ERROR_CODE:
                logger.error("Received 401 response code, unauthorized")
                raise ValidationError(response)
        elif status_code == 401:
            if content_code == AuthenticationFailed.TILLO_ERROR_CODE:
                logger.error("Received 401 response code, unauthorized")
                raise AuthenticationFailed(response)


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
        json: dict[str, Any] | None = None

        if isinstance(endpoint.body, AbstractBodyRequest):
            logger.debug("Requesting endpoint using body for signing: %s", endpoint.body)
            json = endpoint.body.get_as_dict()

        logger.info("Making async request to %s %s", endpoint.method, endpoint.endpoint)
        logger.debug(
            "Request details: %s",
            {
                "method": endpoint.method,
                "endpoint": endpoint.endpoint,
                "params": endpoint.params,
                "route": endpoint.route,
                "body": endpoint.body,
                "has_body": endpoint.is_body_not_empty(),
            },
        )

        sign_attrs = endpoint.get_sign_attrs()
        logger.debug(
            "Retrieved signature attributes: %s",
            sign_attrs if sign_attrs is not None else "None",
        )

        headers = self._get_request_headers(
            endpoint.method,
            endpoint.endpoint,
            sign_attrs,
        )

        try:
            async with AsyncClient(**self.tillo_client_options) as client:
                logger.debug(
                    "Sending async request to %s with method %s",
                    endpoint.route,
                    endpoint.method,
                )
                response = await client.request(
                    url=endpoint.route,
                    method=endpoint.method,
                    params=endpoint.params,
                    json=json,
                    headers=headers,
                )
                logger.debug("Received response with status code: %d", response.status_code)

                if response.status_code != 200:
                    self._catch_non_200_response(response)
                return response
        except Exception as e:
            logger.error("Error making async request to %s: %s", endpoint.route, str(e))
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
            InvalidIpAddress: If the response code is 201
            Exception: For other HTTP or network errors
        """
        json: dict[str, Any] | None = None

        if isinstance(endpoint.body, AbstractBodyRequest):
            logger.debug("Requesting endpoint using body for signing: %s", endpoint.body)
            json = endpoint.body.get_as_dict()

        logger.info("Making sync request to %s %s", endpoint.method, endpoint.endpoint)
        logger.debug(
            "Request details: %s",
            {
                "method": endpoint.method,
                "endpoint": endpoint.endpoint,
                "params": endpoint.params,
                "route": endpoint.route,
                "has_body": endpoint.is_body_not_empty(),
            },
        )

        sign_attrs = endpoint.get_sign_attrs()
        logger.debug(
            "Retrieved signature attributes: %s",
            sign_attrs if sign_attrs is not None else "None",
        )

        headers = self._get_request_headers(
            endpoint.method,
            endpoint.endpoint,
            sign_attrs,
        )

        try:
            with Client(**self.tillo_client_options) as client:
                logger.debug(
                    "Sending sync request to %s with method %s",
                    endpoint.route,
                    endpoint.method,
                )
                response = client.request(
                    url=endpoint.route,
                    method=endpoint.method,
                    params=endpoint.params,
                    json=json,
                    headers=headers,
                )
                logger.debug("Received response with status code: %d", response.status_code)

                if response.status_code != 200:
                    self._catch_non_200_response(response)

                return response
        except Exception as e:
            logger.error("Error making sync request to %s: %s", endpoint.route, str(e))
            raise
