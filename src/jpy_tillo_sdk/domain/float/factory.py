from jpy_tillo_sdk.domain.float.endpoints import CheckFloatsEndpoint
from jpy_tillo_sdk.enums import Currency


def create_check_floats_query(currency: Currency):
    return CheckFloatsEndpoint.QueryParams(currency=currency.value)
