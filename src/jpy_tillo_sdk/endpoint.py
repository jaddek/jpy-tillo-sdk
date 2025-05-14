"""Tillo SDK Endpoint Module.

This module provides classes for handling API endpoints and request parameters.
It includes base classes for query parameters, request bodies, and endpoint
definitions used throughout the SDK.

The module consists of three main classes:
- QP: Base class for query parameters
- AbstractBodyRequest: Base class for request bodies
- Endpoint: Base class for API endpoints

Example:
    ```python
    @dataclass(frozen=True)
    class MyQueryParams(QP):
        param1: str
        param2: int

    @dataclass(frozen=True)
    class MyRequestBody(AbstractBodyRequest):
        data: str

        def get_sign_attrs(self) -> tuple:
            return (self.data,)

    class MyEndpoint(Endpoint):
        _method = "POST"
        _endpoint = "/api/v1/endpoint"
        _route = "https://api.tillo.io/api/v1/endpoint"
    ```
"""

import logging
from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass
from typing import Any, Optional

logger = logging.getLogger("tillo.endpoint")


@dataclass(frozen=True)
class QP:
    """Base class for query parameters.

    This class provides common functionality for handling query parameters
    in API requests, including filtering empty values and generating
    signature attributes.
    """

    def get_not_empty_values(self) -> dict:
        """Get dictionary of non-empty parameter values.

        Returns:
            dict: Dictionary containing only non-None parameter values
        """
        values = {k: v for k, v in self.__dict__.items() if v is not None}
        logger.debug("Filtered query parameters: %s", values)
        return values

    def get_sign_attrs(self) -> tuple:
        """Get parameters to include in request signature.

        Returns:
            tuple: Empty tuple by default, should be overridden by subclasses
        """
        logger.debug("Getting signature attributes from query parameters")
        return ()


@dataclass(frozen=True)
class AbstractBodyRequest(ABC):
    """Base class for request bodies.

    This class provides common functionality for handling request bodies
    in API requests, including converting to dictionary format and generating
    signature attributes.
    """

    @abstractmethod
    def get_sign_attrs(self) -> tuple:
        """Get attributes to include in request signature.

        Returns:
            tuple: Empty tuple by default, should be overridden by subclasses
        """
        logger.debug("Getting signature attributes from request body")
        return ()

    def get_as_dict(self) -> dict:
        """Convert request body to dictionary format.

        Returns:
            dict: Dictionary representation of the request body
        """
        body_dict = asdict(self)
        logger.debug("Converted request body to dictionary: %s", body_dict)
        return body_dict


class Endpoint:
    """Base class for API endpoints.

    This class provides common functionality for handling API endpoints,
    including method, path, and parameter management. It handles both
    query parameters and request bodies, and manages signature generation
    for request authentication.

    Attributes:
        _method (Optional[str]): HTTP method (GET, POST, etc.)
        _endpoint (Optional[str]): API endpoint path
        _route (Optional[str]): Full API route including base URL
        _query (Optional[QP]): Query parameters
        _body (Optional[AbstractBodyRequest]): Request body
        _sign_attrs (Optional[tuple]): Attributes for signature generation
    """

    _method: Optional[str] = None
    _endpoint: Optional[str] = None
    _route: Optional[str] = None
    _query: Optional[Any] = None
    _body: Optional[AbstractBodyRequest] = None
    _sign_attrs = None

    def __init__(
        self,
        query: Optional[Any] = None,
        body: Optional[AbstractBodyRequest] = None,
        sign_attrs: Optional[tuple] = None,
    ):
        """Initialize the endpoint with query parameters and request body.

        Args:
            query (Optional[QP]): Query parameters for the request
            body (Optional[AbstractBodyRequest]): Request body
            sign_attrs (Optional[tuple]): Attributes for signature generation
        """
        if type(self) is Endpoint:
            raise TypeError("Endpoint is an abstract class and cannot be instantiated directly.")

        self._query = query
        self._body = body
        self._sign_attrs = sign_attrs
        logger.debug(
            "Initialized endpoint: %s",
            {
                "method": self._method,
                "endpoint": self._endpoint,
                "has_query": query is not None,
                "has_body": body is not None,
                "has_sign_attrs": sign_attrs is not None,
            },
        )

    @property
    def method(self) -> str:
        """Get the HTTP method for the endpoint.

        Returns:
            Optional[str]: HTTP method (GET, POST, etc.)
        """
        if self._method is None:
            raise RuntimeError("Endpoint _method has not been initialized.")

        return self._method

    @property
    def endpoint(self) -> str:
        """Get the API endpoint path.

        Returns:
            Optional[str]: API endpoint path
        """
        if self._endpoint is None:
            raise RuntimeError("Endpoint _endpoint has not been initialized.")

        return self._endpoint

    @property
    def route(self) -> str:
        """Get the full API route including base URL.

        Returns:
            Optional[str]: Full API route
        """
        if self._route is None:
            raise RuntimeError("Endpoint _route has not been initialized.")

        return self._route

    @property
    def body(self) -> AbstractBodyRequest | dict:
        """Get the request body.

        Returns:
            Optional[AbstractBodyRequest]: Request body or empty dict if None
        """
        return {} if self._body is None else self._body

    def is_body_not_empty(self) -> bool:
        """Check if the request has a body.

        Returns:
            bool: True if request has a body, False otherwise
        """
        has_body = self._body is not None
        logger.debug("Checking request body: %s", has_body)
        return has_body

    @property
    def sign_attrs(self) -> Optional[tuple]:
        """Get attributes for signature generation.

        Returns:
            Optional[tuple]: Attributes for signature generation
        """
        return self._sign_attrs

    @property
    def query(self) -> QP | None:
        """Get the query parameters.

        Returns:
            QP | None: Query parameters or None
        """
        return self._query

    @property
    def params(self) -> dict:
        """Get non-empty query parameters as a dictionary.

        Returns:
            dict: Dictionary of non-empty query parameters
        """
        params = self._query.get_not_empty_values() if self._query is not None else {}
        logger.debug("Getting request parameters: %s", params)
        return params

    def get_sign_attrs(self) -> tuple:
        """Get attributes to include in request signature.

        This method determines which attributes to include in the signature
        based on whether the request has a body or query parameters.

        Returns:
            tuple: Attributes to include in request signature
        """
        logger.debug("Getting signature attributes for request")
        sign_attrs: tuple = ()

        if self.is_body_not_empty():
            logger.debug("Using body attributes for signature")
            sign_attrs += self.body.get_sign_attrs() if self.is_body_not_empty() else ()
        else:
            logger.debug("Using query parameters for signature")
            sign_attrs += self.query.get_sign_attrs() if self.query is not None else ()

        logger.debug("Generated signature attributes: %s", sign_attrs)
        return sign_attrs
