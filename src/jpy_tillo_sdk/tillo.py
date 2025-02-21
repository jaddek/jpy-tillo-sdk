from typing import Optional

from jpy_tillo_sdk.domain.float.services import FloatServiceAsyncInstance
from jpy_tillo_sdk.errors import AuthorizationErrorInvalidAPITokenOrSecret
from jpy_tillo_sdk.http_client import AsyncHttpClient, HttpClient
from jpy_tillo_sdk.http_client_factory import create_client_async, create_client


class TilloClient:
    def __init__(
            self,
            api_key: str,
            secret: str,
            options: Optional[dict] = None,
    ):
        if api_key is None or secret is None:
            raise AuthorizationErrorInvalidAPITokenOrSecret()

        self.__api_key = api_key
        self.__secret = secret
        self.__options = options
        self.__async_http_client = self.__get_async_client()

        self._floats: FloatServiceAsyncInstance | None = None

    @property
    def floats(self) -> FloatServiceAsyncInstance:
        if self._floats is None:
            self._floats = FloatServiceAsyncInstance(
                client=self.__async_http_client
            )

        return self._floats

    def brand(self):
        pass

    def template(self):
        pass

    def digital_card(self):
        pass

    def physical_card(self):
        pass

    def webhook(self):
        pass

    def __get_async_client(self) -> AsyncHttpClient:
        return create_client_async(
            self.__api_key,
            self.__secret,
            self.__options
        )

    def __get_client(self) -> HttpClient:
        return create_client(
            self.__api_key,
            self.__secret,
            self.__options
        )
