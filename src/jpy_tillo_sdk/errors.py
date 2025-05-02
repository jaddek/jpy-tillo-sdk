class TilloException(Exception):
    TILLO_ERROR_CODE: str = None
    HTTP_ERROR_CODE: int = None
    MESSAGE: str = None
    DESCRIPTION: str = None
    API_VERSION: int = None

    def __init__(self, *args):
        super().__init__(*args)
        self.message = self.MESSAGE
        self.description = self.DESCRIPTION
        self.tillo_error_code = self.TILLO_ERROR_CODE
        self.http_error_code = self.HTTP_ERROR_CODE
        self.api_version = self.API_VERSION

    def __str__(self):
        return f"{self.message} (Tillo Error {self.tillo_error_code}, HTTP {self.http_error_code})"


'''
Library exceptions
'''


class AuthenticationError(TilloException):
    TILLO_ERROR_CODE = None
    HTTP_ERROR_CODE = 401
    MESSAGE = "Pair API-Token or Secret-key not provided."
    DESCRIPTION = "No API key provided. (HINT: set your API key using 'client = jpy_tillo_sdk.TilloClient(<API-KEY>, <SECRET-KEY>)')"
    API_VERSION = 1

class AuthorizationErrorInvalidAPITokenOrSecret(AuthenticationError):
    pass

'''
Tillo exceptions
'''


class InvalidApiToken(TilloException):
    TILLO_ERROR_CODE = "060"
    HTTP_ERROR_CODE = 400
    MESSAGE = "Token mismatch error"
    DESCRIPTION = "Invalid or expired API Token"
    API_VERSION = 1


class MissingParameters(TilloException):
    TILLO_ERROR_CODE = "070"
    HTTP_ERROR_CODE = 400
    MESSAGE = "Missing parameter"
    DESCRIPTION = "Missing parameter amount or personalisation"
    API_VERSION = 2


class MissingParameterAmount(TilloException):
    TILLO_ERROR_CODE = "071"
    HTTP_ERROR_CODE = 400
    MESSAGE = "Missing parameter"
    DESCRIPTION = "Missing additionalParams"
    API_VERSION = 1


class BrandNotFound(TilloException):
    TILLO_ERROR_CODE = "072"
    HTTP_ERROR_CODE = 400
    MESSAGE = "Brand not found"
    DESCRIPTION = "The requested brand does not exist"
    API_VERSION = 2


class InvalidBrandForPartner(TilloException):
    TILLO_ERROR_CODE = "072"
    HTTP_ERROR_CODE = 401
    MESSAGE = "Invalid brand for partner"
    DESCRIPTION = "Brand is not available for this partner"
    API_VERSION = 2


class GiftCodeCancelled(TilloException):
    TILLO_ERROR_CODE = "100"
    HTTP_ERROR_CODE = 422
    MESSAGE = "The gift code has already been cancelled"
    DESCRIPTION = "Attempted action on a cancelled gift code"
    API_VERSION = 2


class InvalidIpAddress(TilloException):
    TILLO_ERROR_CODE = "210"
    HTTP_ERROR_CODE = 401
    MESSAGE = "Invalid IP address"
    DESCRIPTION = "IP address is not authorized"
    API_VERSION = 2


class InsufficientMonies(TilloException):
    TILLO_ERROR_CODE = "610"
    HTTP_ERROR_CODE = 403
    MESSAGE = "Insufficient Monies"
    DESCRIPTION = "Insufficient balance on account"
    API_VERSION = 2


class InsufficientMoniesOnAccount(TilloException):
    TILLO_ERROR_CODE = "610"
    HTTP_ERROR_CODE = 422
    MESSAGE = "Insufficient balance"
    DESCRIPTION = "Insufficient balance on account"
    API_VERSION = 2


class InvalidValue(TilloException):
    TILLO_ERROR_CODE = "704"
    HTTP_ERROR_CODE = 400
    MESSAGE = "Invalid value"
    DESCRIPTION = "Invalid or unsupported value provided"
    API_VERSION = 2


class SaleDisabled(TilloException):
    TILLO_ERROR_CODE = "706"
    HTTP_ERROR_CODE = 401
    MESSAGE = "Sale is disabled"
    DESCRIPTION = "The brand is not available for sale"
    API_VERSION = 2


class DuplicateClientRequest(TilloException):
    TILLO_ERROR_CODE = "708"
    HTTP_ERROR_CODE = 400
    MESSAGE = "Duplicate clientRequestID"
    DESCRIPTION = "The clientRequestID already exists with mismatched brand or value"
    API_VERSION = 2


class RelationshipNotFound(TilloException):
    TILLO_ERROR_CODE = "709"
    HTTP_ERROR_CODE = 404
    MESSAGE = "No relationship found"
    DESCRIPTION = "No relationship exists between partner and brand"
    API_VERSION = 2


class CancelNotActive(TilloException):
    TILLO_ERROR_CODE = "711"
    HTTP_ERROR_CODE = 400
    MESSAGE = "Cancel not active"
    DESCRIPTION = "Card no longer active"
    API_VERSION = 2


class DeliveryMethodNotFound(TilloException):
    TILLO_ERROR_CODE = "712"
    HTTP_ERROR_CODE = 404
    MESSAGE = "Delivery method not found"
    DESCRIPTION = "The requested delivery method was not found"
    API_VERSION = 2


class InvalidDeliveryMethod(TilloException):
    TILLO_ERROR_CODE = "713"
    HTTP_ERROR_CODE = 400
    MESSAGE = "Invalid delivery method"
    DESCRIPTION = "The delivery method is not allowed"
    API_VERSION = 2


class MissingDeliveryMethod(TilloException):
    TILLO_ERROR_CODE = "714"
    HTTP_ERROR_CODE = 400
    MESSAGE = "Missing delivery method"
    DESCRIPTION = "You did not supply a delivery method"
    API_VERSION = 2


class UrlHostingServiceUnavailable(TilloException):
    TILLO_ERROR_CODE = "715"
    HTTP_ERROR_CODE = 503
    MESSAGE = "URL hosting service unavailable"
    DESCRIPTION = "The URL hosting service is currently unavailable"
    API_VERSION = 2


class TemplateNotFound(TilloException):
    TILLO_ERROR_CODE = "716"
    HTTP_ERROR_CODE = 400
    MESSAGE = "Template not found"
    DESCRIPTION = "The requested template was not found"
    API_VERSION = 2


class TemplateAccessDenied(TilloException):
    TILLO_ERROR_CODE = "717"
    HTTP_ERROR_CODE = 401
    MESSAGE = "Template access denied"
    DESCRIPTION = (
        "The partner does not have access to the template for the requested brand"
    )
    API_VERSION = 2


class UnsupportedTransactionType(TilloException):
    TILLO_ERROR_CODE = "719"
    HTTP_ERROR_CODE = 422
    MESSAGE = "Transaction type not supported"
    DESCRIPTION = "The transaction type is not supported by the partner"
    API_VERSION = 2


class UnsupportedBrandTransactionType(TilloException):
    TILLO_ERROR_CODE = "720"
    HTTP_ERROR_CODE = 422
    MESSAGE = "Brand transaction type not supported"
    DESCRIPTION = "The transaction type is not supported for the requested brand"
    API_VERSION = 2


class CurrencyIsoCodeNotFound(TilloException):
    TILLO_ERROR_CODE = "721"
    HTTP_ERROR_CODE = 422
    MESSAGE = "Currency ISO code not found"
    DESCRIPTION = "The requested currency was not found"
    API_VERSION = 2


class MissingCurrencyIsoCode(TilloException):
    TILLO_ERROR_CODE = "722"
    HTTP_ERROR_CODE = 400
    MESSAGE = "Missing currency iso code"
    DESCRIPTION = "You did not supply a currency"
    API_VERSION = 2


class UnsupportedCurrencyIsoCode(TilloException):
    TILLO_ERROR_CODE = "723"
    HTTP_ERROR_CODE = 422
    MESSAGE = "Unsupported currency iso code"
    DESCRIPTION = "The requested currency iso code is not supported by this brand"
    API_VERSION = 2


class SaleNotFound(TilloException):
    TILLO_ERROR_CODE = "724"
    HTTP_ERROR_CODE = 422
    MESSAGE = "Sale reference not found"
    DESCRIPTION = "The sale reference could not be found"
    API_VERSION = 2


class DenominationNotInStock(TilloException):
    TILLO_ERROR_CODE = "725"
    HTTP_ERROR_CODE = 500
    MESSAGE = "Denomination not in stock"
    DESCRIPTION = "The requested denomination is not in stock"
    API_VERSION = 2


class FeatureNotEnabled(TilloException):
    TILLO_ERROR_CODE = "726"
    HTTP_ERROR_CODE = 503
    MESSAGE = "Feature not enabled"
    DESCRIPTION = "The requested feature has not been enabled"
    API_VERSION = 2


class InsufficientBalanceOnCard(TilloException):
    TILLO_ERROR_CODE = "728"
    HTTP_ERROR_CODE = 403
    MESSAGE = "Insufficient balance on card"
    DESCRIPTION = "Insufficient balance on card"
    API_VERSION = 2


class DuplicateRequestIncomplete(TilloException):
    TILLO_ERROR_CODE = "729"
    HTTP_ERROR_CODE = 400
    MESSAGE = "Duplicate request"
    DESCRIPTION = "The original request is still being processed"
    API_VERSION = 2


class InvalidSaleReference(TilloException):
    TILLO_ERROR_CODE = "730"
    HTTP_ERROR_CODE = 400
    MESSAGE = "Invalid sale reference"
    DESCRIPTION = "The provided sale reference is invalid"
    API_VERSION = 2


class SaleRedemptionInProgress(TilloException):
    TILLO_ERROR_CODE = "732"
    HTTP_ERROR_CODE = 425
    MESSAGE = "Sale redemption in progress"
    DESCRIPTION = "Redemption for this sale is already in progress"
    API_VERSION = 2


class InvalidOrderStatus(TilloException):
    TILLO_ERROR_CODE = "733"
    HTTP_ERROR_CODE = 422
    MESSAGE = "Invalid order status"
    DESCRIPTION = "Cannot fulfil order, invalid status"
    API_VERSION = 2


class InvalidRedemptionStatus(TilloException):
    TILLO_ERROR_CODE = "734"
    HTTP_ERROR_CODE = 422
    MESSAGE = "Invalid redemption status"
    DESCRIPTION = "Cannot fulfil order, invalid redemption status"
    API_VERSION = 2


class SaleExpired(TilloException):
    TILLO_ERROR_CODE = "735"
    HTTP_ERROR_CODE = 410
    MESSAGE = "Sale expired"
    DESCRIPTION = "The sale has expired, preventing any further action"
    API_VERSION = 2


class InvalidFinancialRelationship(TilloException):
    TILLO_ERROR_CODE = "736"
    HTTP_ERROR_CODE = 400
    MESSAGE = "Invalid financial relationship"
    DESCRIPTION = "Cannot fulfil order, invalid financial relationship"
    API_VERSION = 2


class CurrencyForInternationalPaymentsOnly(TilloException):
    TILLO_ERROR_CODE = "738"
    HTTP_ERROR_CODE = 422
    MESSAGE = "Currency only for international payments"
    DESCRIPTION = "The requested currency is only available with International Payments"
    API_VERSION = 2


class UnsupportedBrandForInternationalPayments(TilloException):
    TILLO_ERROR_CODE = "739"
    HTTP_ERROR_CODE = 422
    MESSAGE = "Brand not supported for international payments"
    DESCRIPTION = "The requested brand is not supported by International Payments"
    API_VERSION = 2


class FeatureOnlyAvailableInApiV2(TilloException):
    TILLO_ERROR_CODE = "740"
    HTTP_ERROR_CODE = 400
    MESSAGE = "Feature only available in API v2"
    DESCRIPTION = "The requested feature is only available through API v2"
    API_VERSION = "2"


class EndpointNotFound(TilloException):
    TILLO_ERROR_CODE = "999"
    HTTP_ERROR_CODE = 404
    MESSAGE = "Endpoint not found"
    DESCRIPTION = "The requested endpoint was not found"
    API_VERSION = 2


class MethodNotAllowed(TilloException):
    TILLO_ERROR_CODE = "999"
    HTTP_ERROR_CODE = 405
    MESSAGE = "Method not allowed"
    DESCRIPTION = "The requested method is not allowed"
    API_VERSION = 2


class InternalServerError(TilloException):
    TILLO_ERROR_CODE = "999"
    HTTP_ERROR_CODE = 500
    MESSAGE = "Internal error"
    DESCRIPTION = "An internal server error occurred"
    API_VERSION = 2
