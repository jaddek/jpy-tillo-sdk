from typing import Any

from .http_client import AsyncHttpClient, HttpClient
from .signature import SignatureBridge, SignatureGenerator


def create_signer(api_key: str, secret_key: str) -> SignatureBridge:
    return SignatureBridge(
        SignatureGenerator(
            api_key,
            secret_key,
        )
    )


def create_client_async(
    api_key: str, secret_key: str, tillo_client_params: dict[str, Any]
) -> AsyncHttpClient:
    signer = create_signer(api_key, secret_key)

    return AsyncHttpClient(tillo_client_params, signer)


def create_client(
    api_key: str,
    secret_key: str,
    tillo_client_params: dict[str, Any],
) -> HttpClient:
    signer = create_signer(api_key, secret_key)

    return HttpClient(tillo_client_params, signer)
