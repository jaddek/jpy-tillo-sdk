import pytest


class TestSignatureGenerator:
    def test_get_api_key(self, signature_generator, api_key):
        assert signature_generator.get_api_key() == api_key

    def test_get_secret_key_as_bytes(self, signature_generator, secret_key):
        result = signature_generator.get_secret_key_as_bytes()
        assert isinstance(result, bytearray)
        assert result == bytearray(secret_key, "utf-8")

    def test_generate_timestamp(self, signature_generator):
        timestamp = signature_generator.generate_timestamp()
        assert isinstance(timestamp, str)
        assert timestamp.isdigit()

    def test_generate_unique_client_request_id(self, signature_generator):
        request_id = signature_generator.generate_unique_client_request_id()
        assert str(request_id)  # Should be convertible to string
        assert len(str(request_id)) == 36  # UUID length

    @pytest.mark.parametrize(
        "endpoint,request_type,timestamp,params,expected",
        [
            (
                "/test",
                "GET",
                "1234567890",
                (),
                "test_api_key-GET-/test-1234567890",
            ),
            (
                "/test",
                "POST",
                "1234567890",
                ("param1", "param2"),
                "test_api_key-POST-/test-param1-param2-1234567890",
            ),
            (
                "/test",
                "PUT",
                "1234567890",
                ("param1", None, "param2"),
                "test_api_key-PUT-/test-param1-param2-1234567890",
            ),
        ],
    )
    def test_generate_signature_string(self, signature_generator, endpoint, request_type, timestamp, params, expected):
        result = signature_generator.generate_signature_string(endpoint, request_type, timestamp, params)
        assert result == expected

    def test_generate_signature(self, signature_generator):
        seed = "test-seed"
        signature = signature_generator.generate_signature(seed)
        assert isinstance(signature, str)
        assert len(signature) == 64  # SHA256 hex digest length


class TestSignatureBridge:
    def test_sign(self, signature_bridge):
        endpoint = "/test"
        method = "GET"
        sign_attrs = ("param1", "param2")

        api_key, signature, timestamp = signature_bridge.sign(endpoint, method, sign_attrs)

        assert isinstance(api_key, str)
        assert isinstance(signature, str)
        assert isinstance(timestamp, str)
        assert timestamp.isdigit()
        assert len(signature) == 64  # SHA256 hex digest length
