import logging
from abc import ABC
from typing import Any

from jpy_tillo_sdk.contracts import (
    EndpointInterface,
    SignatureAttributesInterface,
)

logger = logging.getLogger("tillo.endpoint")


class SignedEndpointInterface(EndpointInterface, ABC):
    _sign_attrs: list[str] = []

    @property
    def sign_attrs(self) -> tuple[str, ...]:
        logger.debug("Getting signature attributes for request")
        _sign_attrs: list[str] = []

        if isinstance(self.body, SignatureAttributesInterface):
            _sign_attrs += self.body.sign_attrs

        if isinstance(self.query, SignatureAttributesInterface):
            _sign_attrs += self.query.sign_attrs

        _sign_attrs = [attr for attr in _sign_attrs if attr is not None]

        logger.debug("Generated signature attributes: %s", _sign_attrs)
        return tuple(_sign_attrs)


class Endpoint(SignedEndpointInterface, ABC):
    _method: str
    _endpoint: str
    _route: str
    _query: Any
    _body: Any

    def __init__(
        self,
        query: Any = None,
        body: Any = None,
    ):
        if self._method is None:
            raise RuntimeError("Endpoint _method has not been initialized.")

        if self._endpoint is None:
            raise RuntimeError("Endpoint _endpoint has not been initialized.")

        if self._route is None:
            raise RuntimeError("Endpoint _route has not been initialized.")

        self._query = query
        self._body = body

    @property
    def method(self) -> str:
        return self._method

    @property
    def endpoint(self) -> str:
        return self._endpoint

    @property
    def route(self) -> str:
        return self._route

    @property
    def body(self) -> Any:
        return self._body

    @property
    def query(self) -> Any:
        return self._query
