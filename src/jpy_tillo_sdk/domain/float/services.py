import logging
from typing import final

from httpx import Response

from ...contracts import FloatServiceAsyncInterface, FloatServiceInterface
from .endpoints import (
    CheckFloatsEndpoint,
    CheckFloatsEndpointRequestQuery,
    RequestPaymentTransferEndpoint,
    RequestPaymentTransferEndpointRequestBody,
)

logger = logging.getLogger("tillo.float_services")


@final
class FloatService(FloatServiceInterface):
    def check_floats(
        self,
        query: CheckFloatsEndpointRequestQuery | None = None,
    ) -> Response:
        endpoint = CheckFloatsEndpoint(query=query)
        response = self.client.request(
            endpoint=endpoint,
        )

        return response

    def request_payment_transfer(self, body: RequestPaymentTransferEndpointRequestBody) -> Response:
        endpoint = RequestPaymentTransferEndpoint(body=body)
        response = self.client.request(
            endpoint=endpoint,
        )

        return response


@final
class FloatServiceAsync(FloatServiceAsyncInterface):
    async def check_floats(
        self,
        query: CheckFloatsEndpointRequestQuery | None = None,
    ) -> Response:
        endpoint = CheckFloatsEndpoint(query=query)
        response = await self.client.request(
            endpoint=endpoint,
        )

        return response

    async def request_payment_transfer(self, body: RequestPaymentTransferEndpointRequestBody) -> Response:
        endpoint = RequestPaymentTransferEndpoint(body=body)
        response = await self.client.request(
            endpoint=endpoint,
        )

        return response
