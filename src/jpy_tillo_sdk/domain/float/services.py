"""Tillo SDK Float Services Module.

This module provides services for managing float operations in the Tillo platform.
It includes both synchronous and asynchronous implementations for checking float
balances and requesting payment transfers.

The module consists of two main classes:
- FloatService: Synchronous implementation for float operations
- FloatServiceAsync: Asynchronous implementation for float operations

Example:
    ```python
    # Synchronous usage
    float_service = FloatService(client=http_client)
    response = float_service.check_floats()

    # Asynchronous usage
    float_service_async = FloatServiceAsync(client=async_http_client)
    response = await float_service_async.check_floats_async()
    ```
"""

import logging

from httpx import Response

from ...contracts import FloatServiceAsyncInterface, FloatServiceInterface, QueryParamsInterface
from ...http_client import AsyncHttpClient, HttpClient
from .endpoints import CheckFloatsEndpoint, RequestPaymentTransferEndpoint

logger = logging.getLogger("tillo.float_services")


class FloatService(FloatServiceInterface):
    """Synchronous service for managing float operations.

    This class provides methods for checking float balances and requesting
    payment transfers using synchronous HTTP requests.

    Args:
        client (HttpClient): The HTTP client instance for making requests

    Example:
        ```python
        float_service = FloatService(client=http_client)

        # Check float balance
        response = float_service.check_floats()

        # Request payment transfer
        transfer_body = RequestPaymentTransferEndpoint.RequestBody(
            amount=100.00,
            currency="USD"
        )
        response = float_service.request_payment_transfer(transfer_body)
        ```
    """

    def __init__(self, *, client: HttpClient):
        """Initialize the float service with an HTTP client.

        Args:
            client (HttpClient): The HTTP client instance for making requests
        """
        self.client = client
        logger.debug("Initialized FloatService with HTTP client")

    def check_floats(
        self,
        query_params: QueryParamsInterface | None = None,
    ) -> Response:
        """Check float balances for the account.

        This method retrieves the current float balances for the account,
        optionally filtered by the provided query parameters.

        Args:
            query_params (CheckFloatsEndpoint.QueryParams | None): Optional query
                parameters to filter the float check results

        Returns:
            Response: The HTTP response containing the float balance information

        Example:
            ```python
            # Check all floats
            response = float_service.check_floats()

            # Check floats with specific currency
            params = CheckFloatsEndpoint.QueryParams(currency="USD")
            response = float_service.check_floats(query_params=params)
            ```
        """
        logger.info("Checking float balances")
        logger.debug(
            "Request details: %s",
            {
                "query_params": query_params.__dict__ if query_params else None,
            },
        )

        endpoint = CheckFloatsEndpoint(query=query_params)

        response = self.client.request(
            endpoint=endpoint,
        )

        logger.debug(
            "Float check response: %s",
            {
                "status_code": response.status_code,
                "content": response.text,
            },
        )

        return response

    def request_payment_transfer(self, body: RequestPaymentTransferEndpoint.RequestBody) -> Response:
        """Request a payment transfer between floats.

        This method initiates a payment transfer between different float accounts
        using the provided transfer details.

        Args:
            body (RequestPaymentTransferEndpoint.RequestBody): The transfer request
                details including amount, currency, and accounts

        Returns:
            Response: The HTTP response containing the transfer request result

        Example:
            ```python
            transfer_body = RequestPaymentTransferEndpoint.RequestBody(
                amount=100.00,
                currency="USD",
                from_account="main",
                to_account="reserve"
            )
            response = float_service.request_payment_transfer(transfer_body)
            ```
        """
        logger.info("Requesting payment transfer")
        logger.debug(
            "Request details: %s",
            {
                "body": body.__dict__,
            },
        )

        endpoint = RequestPaymentTransferEndpoint(body=body)

        response = self.client.request(
            endpoint=endpoint,
        )

        logger.debug(
            "Payment transfer response: %s",
            {
                "status_code": response.status_code,
                "content": response.text,
            },
        )

        return response


class FloatServiceAsync(FloatServiceAsyncInterface):
    """Asynchronous service for managing float operations.

    This class provides methods for checking float balances and requesting
    payment transfers using asynchronous HTTP requests.

    Args:
        client (AsyncHttpClient): The asynchronous HTTP client instance for making requests

    Example:
        ```python
        float_service = FloatServiceAsync(client=async_http_client)

        # Check float balance
        response = await float_service.check_floats_async()

        # Request payment transfer
        transfer_body = RequestPaymentTransferEndpoint.RequestBody(
            amount=100.00,
            currency="USD"
        )
        response = await float_service.request_payment_transfer_async(transfer_body)
        ```
    """

    def __init__(self, *, client: AsyncHttpClient):
        """Initialize the async float service with an HTTP client.

        Args:
            client (AsyncHttpClient): The asynchronous HTTP client instance
        """
        self.client = client
        logger.debug("Initialized FloatServiceAsync with HTTP client")

    async def check_floats(
        self,
        query_params: QueryParamsInterface | None = None,
    ) -> Response:
        """Check float balances for the account asynchronously.

        This method retrieves the current float balances for the account,
        optionally filtered by the provided query parameters.

        Args:
            query_params (CheckFloatsEndpoint.QueryParams | None): Optional query
                parameters to filter the float check results

        Returns:
            Response: The HTTP response containing the float balance information

        Example:
            ```python
            # Check all floats
            response = await float_service.check_floats()

            # Check floats with specific currency
            params = CheckFloatsEndpoint.QueryParams(currency="USD")
            response = await float_service.check_floats(query_params=params)
            ```
        """
        logger.info("Checking float balances asynchronously")
        logger.debug(
            "Request details: %s",
            {
                "query_params": query_params.__dict__ if query_params else None,
            },
        )

        endpoint = CheckFloatsEndpoint(query=query_params)

        response = await self.client.request(
            endpoint=endpoint,
        )

        logger.debug(
            "Async float check response: %s",
            {
                "status_code": response.status_code,
                "content": response.text,
            },
        )

        return response

    async def request_payment_transfer(self, body: RequestPaymentTransferEndpoint.RequestBody) -> Response:
        """Request a payment transfer between floats asynchronously.

        This method initiates a payment transfer between different float accounts
        using the provided transfer details.

        Args:
            body (RequestPaymentTransferEndpoint.RequestBody): The transfer request
                details including amount, currency, and accounts

        Returns:
            Response: The HTTP response containing the transfer request result

        Example:
            ```python
            transfer_body = RequestPaymentTransferEndpoint.RequestBody(
                amount=100.00,
                currency="USD",
                from_account="main",
                to_account="reserve"
            )
            response = await float_service.request_payment_transfer_async(transfer_body)
            ```
        """
        logger.info("Requesting payment transfer asynchronously")
        logger.debug(
            "Request details: %s",
            {
                "body": body.__dict__,
            },
        )

        endpoint = RequestPaymentTransferEndpoint(body=body)

        response = await self.client.request(
            endpoint=endpoint,
        )

        logger.debug(
            "Async payment transfer response: %s",
            {
                "status_code": response.status_code,
                "content": response.text,
            },
        )

        return response
