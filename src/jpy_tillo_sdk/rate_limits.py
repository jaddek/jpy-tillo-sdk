"""Tillo SDK Rate Limits Module.

This module defines rate limits for various API operations in the Tillo platform.
It provides classes for different types of operations (gift cards, digital issues,
balance checks, etc.) with their respective rate limits.

The module consists of several classes:
- RateLimit: Base class for rate limits
- GC: Gift card operation rate limits
- DigitalIssue: Digital card issuance rate limits
- DigitalCheckBalance: Balance check rate limits
- DigitalOrderStatus: Order status check rate limits

Example:
    ```python
    # Check gift card creation rate limit
    rate_limit = GC.post_create_gc()

    # Check digital card issuance rate limit
    rate_limit = DigitalIssue.post()
    ```
"""

import logging

logger = logging.getLogger("tillo.rate_limits")


class RateLimit:
    """Base class for rate limits.

    This class provides the foundation for rate limit implementations
    across different types of operations in the Tillo API.
    """

    def __init__(self, limit: int):
        """Initialize rate limit with maximum requests per period.

        Args:
            limit (int): Maximum number of requests allowed per period
        """
        self.limit = limit
        logger.debug("Initialized rate limit: %d requests per period", limit)


class GC(RateLimit):
    """Rate limits for gift card operations.

    This class defines rate limits for various gift card operations:
    - Creating gift cards
    - Checking gift card balances
    - Canceling gift cards
    """

    __CREATE_RATE_LIMIT: int = 600
    __CREATE_GET_BALANCE_GC_LIMIT: int = 50
    __CREATE_CANCEL_GC_LIMIT: int = 50

    @staticmethod
    def post_create_gc() -> RateLimit:
        """Get rate limit for creating gift cards.

        Returns:
            RateLimit: Rate limit of 600 requests per period
        """
        logger.debug("Getting gift card creation rate limit: %d", GC.__CREATE_RATE_LIMIT)
        return RateLimit(GC.__CREATE_RATE_LIMIT)

    @staticmethod
    def post_get_balance_gc() -> RateLimit:
        """Get rate limit for checking gift card balances.

        Returns:
            RateLimit: Rate limit of 50 requests per period
        """
        logger.debug(
            "Getting gift card balance check rate limit: %d",
            GC.__CREATE_GET_BALANCE_GC_LIMIT,
        )
        return RateLimit(GC.__CREATE_GET_BALANCE_GC_LIMIT)

    @staticmethod
    def post_cancel_gc() -> RateLimit:
        """Get rate limit for canceling gift cards.

        Returns:
            RateLimit: Rate limit of 50 requests per period
        """
        logger.debug("Getting gift card cancellation rate limit: %d", GC.__CREATE_CANCEL_GC_LIMIT)
        return RateLimit(GC.__CREATE_CANCEL_GC_LIMIT)


class DigitalIssue(RateLimit):
    """Rate limits for digital card issuance operations.

    This class defines rate limits for digital card operations:
    - Issuing digital cards
    - Deleting digital cards
    """

    @staticmethod
    def delete() -> RateLimit:
        """Get rate limit for deleting digital cards.

        Returns:
            RateLimit: Rate limit of 900 requests per period
        """
        limit = 900
        logger.debug("Getting digital card deletion rate limit: %d", limit)
        return RateLimit(limit)

    @staticmethod
    def post() -> RateLimit:
        """Get rate limit for issuing digital cards.

        Returns:
            RateLimit: Rate limit of 50 requests per period
        """
        limit = 50
        logger.debug("Getting digital card issuance rate limit: %d", limit)
        return RateLimit(limit)


class DigitalCheckBalance(RateLimit):
    """Rate limits for digital card balance checks.

    This class defines rate limits for checking digital card balances.
    """

    __POST_RATE_LIMIT: int = 50

    @staticmethod
    def post() -> RateLimit:
        """Get rate limit for checking digital card balances.

        Returns:
            RateLimit: Rate limit of 50 requests per period
        """
        logger.debug(
            "Getting digital card balance check rate limit: %d",
            DigitalCheckBalance.__POST_RATE_LIMIT,
        )
        return RateLimit(DigitalCheckBalance.__POST_RATE_LIMIT)


class DigitalOrderStatus(RateLimit):
    """Rate limits for digital card order status checks.

    This class defines rate limits for checking digital card order statuses.
    """

    __GET_RATE_LIMIT: int = 5000

    @staticmethod
    def get() -> RateLimit:
        """Get rate limit for checking digital card order statuses.

        Returns:
            RateLimit: Rate limit of 5000 requests per period
        """
        logger.debug(
            "Getting digital card order status check rate limit: %d",
            DigitalOrderStatus.__GET_RATE_LIMIT,
        )
        return RateLimit(DigitalOrderStatus.__GET_RATE_LIMIT)
