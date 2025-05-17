"""Tillo SDK HTTP Client Factory Module.

This module provides factory functions for creating HTTP clients and signature generators.
It handles the initialization of both synchronous and asynchronous clients with
proper authentication and configuration.

Example:
    ```python
    # Create a synchronous client
    client = create_client(
        api_key="your_api_key",
        secret_key="your_secret_key",
        tillo_client_params={"base_url": "https://api.tillo.io"}
    )

    # Create an asynchronous client
    async_client = create_client_async(
        api_key="your_api_key",
        secret_key="your_secret_key",
        tillo_client_params={"base_url": "https://api.tillo.io"}
    )
    ```
"""

import logging
from typing import Any

from .errors import AuthorizationErrorInvalidAPITokenOrSecret
from .http_client import AsyncHttpClient, ErrorHandler, HttpClient, RequestDataExtractor
from .signature import SignatureBridge, SignatureGenerator

logger = logging.getLogger("tillo.http_client_factory")


def create_signer(api_key: str, secret_key: str) -> SignatureBridge:
    """Create a signature bridge for request signing.

    Args:
        api_key (str): Your Tillo API key
        secret_key (str): Your Tillo secret key

    Returns:
        SignatureBridge: A configured signature bridge instance

    Raises:
        AuthorizationErrorInvalidAPITokenOrSecret: If api_key or secret_key is None
    """
    logger.debug("Creating signature bridge")
    if api_key is None or secret_key is None:
        logger.error("Invalid API credentials provided")
        raise AuthorizationErrorInvalidAPITokenOrSecret()

    generator = SignatureGenerator(api_key, secret_key)
    return SignatureBridge(generator)


def create_client_async(api_key: str, secret_key: str, tillo_client_params: dict[str, Any] | None) -> AsyncHttpClient:
    """Create an asynchronous HTTP client.

    Args:
        api_key (str): Your Tillo API key
        secret_key (str): Your Tillo secret key
        tillo_client_params (dict[str, Any]): Configuration parameters for the client

    Returns:
        AsyncHttpClient: A configured asynchronous HTTP client

    Raises:
        AuthorizationErrorInvalidAPITokenOrSecret: If api_key or secret_key is None
    """
    logger.info("Creating asynchronous HTTP client")
    logger.debug(
        "Client configuration: %s",
        {
            "api_key": api_key[:4] + "..." if api_key else None,
            "client_params": tillo_client_params,
        },
    )

    if api_key is None or secret_key is None:
        logger.error("Invalid API credentials provided")
        raise AuthorizationErrorInvalidAPITokenOrSecret()

    signer = create_signer(api_key, secret_key)
    client = AsyncHttpClient(tillo_client_params, error_handler=ErrorHandler(), extractor=RequestDataExtractor(signer))
    logger.debug("Asynchronous HTTP client created successfully")
    return client


def create_client(
    api_key: str,
    secret_key: str,
    tillo_client_params: dict[str, Any] | None,
) -> HttpClient:
    """Create a synchronous HTTP client.

    Args:
        api_key (str): Your Tillo API key
        secret_key (str): Your Tillo secret key
        tillo_client_params (dict[str, Any]): Configuration parameters for the client

    Returns:
        HttpClient: A configured synchronous HTTP client

    Raises:
        AuthorizationErrorInvalidAPITokenOrSecret: If api_key or secret_key is None
    """
    logger.info("Creating synchronous HTTP client")
    logger.debug(
        "Client configuration: %s",
        {
            "api_key": api_key[:4] + "..." if api_key else None,
            "client_params": tillo_client_params,
        },
    )

    if api_key is None or secret_key is None:
        logger.error("Invalid API credentials provided")
        raise AuthorizationErrorInvalidAPITokenOrSecret()

    signer = create_signer(api_key, secret_key)
    client = HttpClient(tillo_client_params, error_handler=ErrorHandler(), extractor=RequestDataExtractor(signer))
    logger.debug("Synchronous HTTP client created successfully")
    return client
