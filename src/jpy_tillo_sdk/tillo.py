from functools import cached_property

from jpy_tillo_sdk.http_client import AsyncHttpClient, HttpClient
from jpy_tillo_sdk.http_client_factory import create_client_async, create_client


class Tillo:
    def __init__(
            self,
            api_key,
            secret,
            options
    ):
        self.api_key = api_key
        self.secret = secret
        self.options = options

    def brand(self):
        pass

    def template(self):
        pass

    def digital_card(self):
        pass

    def float(self):
        pass

    def physical_card(self):
        pass

    def webhook(self):
        pass

    @cached_property
    async def get_async_client(self) -> AsyncHttpClient:
        return create_client_async(
            self.api_key,
            self.secret,
            self.options
        )

    @cached_property
    def get_client(self) -> HttpClient:
        return create_client(
            self.api_key,
            self.secret,
            self.options
        )
