import hashlib
import hmac
import time
import uuid


class SignatureGenerator:
    def __init__(self, api_key: str, secret_key: str):
        self.__api_key = api_key
        self.__secret_key = secret_key

    def get_api_key(self) -> str:
        return self.__api_key

    def get_secret_key_as_bytes(self):
        return bytearray(self.__secret_key, "utf-8")

    @staticmethod
    def generate_timestamp() -> str:
        return str(int(round(time.time() * 1000)))

    @staticmethod
    def generate_unique_client_request_id() -> uuid.UUID:
        return uuid.uuid4()

    def generate_signature_string(
        self, endpoint: str, request_type: str, timestamp: str, params: tuple
    ):
        query: str = ""

        if params and len(params):
            for v in params:
                if v is not None:
                    query += f"-{v}"

        return f"{self.__api_key}-{request_type}-{endpoint}{query}-{timestamp}"

    def generate_signature(self, seed: str) -> str:
        signature_hmac = hmac.new(
            self.get_secret_key_as_bytes(), bytearray(seed, "utf-8"), hashlib.sha256
        )

        return str(signature_hmac.hexdigest())


class SignatureBridge:
    __signature_generator: SignatureGenerator

    def __init__(self, signature_generator: SignatureGenerator):
        self.__signature_generator = signature_generator

    def sign(
        self,
        endpoint: str,
        method: str,
        sign_attrs: tuple,
    ):
        request_timestamp = self.__signature_generator.generate_timestamp()

        signature_string = self.__signature_generator.generate_signature_string(
            endpoint,
            method,
            request_timestamp,
            sign_attrs,
        )

        request_signature = self.__signature_generator.generate_signature(
            signature_string
        )

        request_api_key = self.__signature_generator.get_api_key()

        return request_api_key, request_signature, request_timestamp
