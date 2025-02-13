from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict
from typing import Optional

@dataclass(frozen=True)
class QP(ABC):
    def get_not_empty_values(self) -> dict:
        return {k: v for k, v in self.__dict__.items() if v is not None}

    def get_sign_attrs(self) -> Optional[tuple]:
        return None


@dataclass(frozen=True)
class AbstractBodyRequest(ABC):
    @abstractmethod
    def get_sign_attrs(self) -> tuple:
        pass

    def get_as_dict(self) -> dict:
        return asdict(self)


class Endpoint(ABC):
    _method: Optional[str] = None
    _endpoint: Optional[str] = None
    _route: Optional[str] = None
    _query: Optional[QP] = None
    _body: Optional[AbstractBodyRequest] = None
    _sign_attrs = None

    def __init__(
            self,
            query: Optional[dict] = None,
            body: Optional[AbstractBodyRequest] = None,
            sign_attrs: Optional[tuple] = None,
    ):
        self._query = query
        self._body = body
        self._sign_attrs = sign_attrs

    @property
    def method(self) -> Optional[str]:
        return self._method

    @property
    def endpoint(self) -> Optional[str]:
        return self._endpoint

    @property
    def route(self) -> Optional[str]:
        return self._route

    @property
    def body(self) -> Optional[AbstractBodyRequest]:
        return {} if self._body is None else self._body

    def is_body_not_empty(self) -> bool:
        return self._body is not None

    @property
    def sign_attrs(self) -> Optional[tuple]:
        return self._sign_attrs

    @property
    def query(self) -> QP:
        return QP()

    @property
    def params(self) -> dict:
        return self.query.get_not_empty_values()
