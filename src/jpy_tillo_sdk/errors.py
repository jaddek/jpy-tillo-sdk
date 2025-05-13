"""Tillo SDK Error Classes.

This module contains all error classes used in the Tillo SDK. These errors are raised
when API requests fail or when invalid operations are attempted. Each error class
includes specific error codes, HTTP status codes, and descriptive messages.

The error hierarchy is organized as follows:
- TilloException (base class)
  - AuthenticationError
    - AuthorizationErrorInvalidAPITokenOrSecret
  - Various API-specific exceptions
"""


class TilloException(Exception):
    """Base exception class for all Tillo SDK errors.

    This class provides a standardized format for all Tillo-related errors,
    including error codes, HTTP status codes, and descriptive messages.

    Attributes:
        TILLO_ERROR_CODE (str): The Tillo-specific error code.
        HTTP_ERROR_CODE (int): The HTTP status code associated with the error.
        MESSAGE (str): A short, user-friendly error message.
        DESCRIPTION (str): A detailed description of the error and how to resolve it.
        API_VERSION (int): The API version where this error is applicable.
    """

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


# Authentication Errors
class AuthenticationError(TilloException):
    """Base class for authentication-related errors.

    This error is raised when there are issues with API authentication,
    such as missing or invalid credentials.
    """

    TILLO_ERROR_CODE = None
    HTTP_ERROR_CODE = 401
    MESSAGE = "Pair API-Token or Secret-key not provided."
    DESCRIPTION = "No API key provided."
    API_VERSION = 1


class AuthorizationErrorInvalidAPITokenOrSecret(AuthenticationError):
    """Raised when the provided API token or secret is invalid.

    This error occurs when either the API token or secret key is missing,
    invalid, or expired.
    """

    pass


# API-Specific Errors
class InvalidApiToken(TilloException):
    """Raised when the API token is invalid or expired.

    This error occurs when the provided API token is either invalid or has expired.
    A new valid API token should be obtained from the Tillo dashboard.
    """

    TILLO_ERROR_CODE = "060"
    HTTP_ERROR_CODE = 400
    MESSAGE = "Token mismatch error"
    DESCRIPTION = "Invalid or expired API Token"
    API_VERSION = 1


class MissingParameters(TilloException):
    """Raised when required parameters are missing from the request.

    This error occurs when essential parameters like amount or personalization
    are not provided in the API request.
    """

    TILLO_ERROR_CODE = "070"
    HTTP_ERROR_CODE = 400
    MESSAGE = "Missing parameter"
    DESCRIPTION = "Missing parameter amount or personalisation"
    API_VERSION = 2


class MissingParameterAmount(TilloException):
    """Raised when the amount parameter is missing.

    This error occurs when the additionalParams parameter is not provided
    in the API request.
    """

    TILLO_ERROR_CODE = "071"
    HTTP_ERROR_CODE = 400
    MESSAGE = "Missing parameter"
    DESCRIPTION = "Missing additionalParams"
    API_VERSION = 1


class BrandNotFound(TilloException):
    """Raised when the requested brand does not exist.

    This error occurs when attempting to access a brand that doesn't exist
    in the Tillo system.
    """

    TILLO_ERROR_CODE = "072"
    HTTP_ERROR_CODE = 400
    MESSAGE = "Brand not found"
    DESCRIPTION = "The requested brand does not exist"
    API_VERSION = 2


class InvalidBrandForPartner(TilloException):
    """Raised when the brand is not available for the partner.

    This error occurs when a partner attempts to access a brand they
    don't have permission to use.
    """

    TILLO_ERROR_CODE = "072"
    HTTP_ERROR_CODE = 401
    MESSAGE = "Invalid brand for partner"
    DESCRIPTION = "Brand is not available for this partner"
    API_VERSION = 2


class GiftCodeCancelled(TilloException):
    """Raised when attempting to perform an action on a cancelled gift code.

    This error occurs when trying to perform operations on a gift code
    that has already been cancelled.
    """

    TILLO_ERROR_CODE = "100"
    HTTP_ERROR_CODE = 422
    MESSAGE = "The gift code has already been cancelled"
    DESCRIPTION = "Attempted action on a cancelled gift code"
    API_VERSION = 2


class UnprocessableContent(TilloException):
    TILLO_ERROR_CODE = "100"
    HTTP_ERROR_CODE = 422
    MESSAGE = "Unprocessable Content"
    DESCRIPTION = "Unprocessable Content"
    API_VERSION = 2


class InvalidIpAddress(TilloException):
    """Raised when the request comes from an unauthorized IP address.

    This error occurs when the request originates from an IP address
    that is not whitelisted in the Tillo system.
    """

    TILLO_ERROR_CODE = "210"
    HTTP_ERROR_CODE = 401
    MESSAGE = "Invalid IP address"
    DESCRIPTION = "IP address is not authorized"
    API_VERSION = 2


class InsufficientMonies(TilloException):
    """Raised when there are insufficient funds in the account.

    This error occurs when attempting to perform an operation that
    requires more funds than are available in the account.
    """

    TILLO_ERROR_CODE = "610"
    HTTP_ERROR_CODE = 403
    MESSAGE = "Insufficient Monies"
    DESCRIPTION = "Insufficient balance on account"
    API_VERSION = 2


class InsufficientMoniesOnAccount(TilloException):
    """Raised when there are insufficient funds for the operation.

    This error occurs when the account balance is too low to complete
    the requested operation.
    """

    TILLO_ERROR_CODE = "610"
    HTTP_ERROR_CODE = 422
    MESSAGE = "Insufficient balance"
    DESCRIPTION = "Insufficient balance on account"
    API_VERSION = 2


class InvalidValue(TilloException):
    """Raised when an invalid or unsupported value is provided.

    This error occurs when a parameter value is outside the allowed
    range or format.
    """

    TILLO_ERROR_CODE = "704"
    HTTP_ERROR_CODE = 400
    MESSAGE = "Invalid value"
    DESCRIPTION = "Invalid or unsupported value provided"
    API_VERSION = 2


class SaleDisabled(TilloException):
    """Raised when attempting to make a sale for a disabled brand.

    This error occurs when trying to process a sale for a brand that
    is currently not available for sale.
    """

    TILLO_ERROR_CODE = "706"
    HTTP_ERROR_CODE = 401
    MESSAGE = "Sale is disabled"
    DESCRIPTION = "The brand is not available for sale"
    API_VERSION = 2


class DuplicateClientRequest(TilloException):
    """Raised when a duplicate clientRequestID is detected.

    This error occurs when attempting to use a clientRequestID that
    already exists with different brand or value parameters.
    """

    TILLO_ERROR_CODE = "708"
    HTTP_ERROR_CODE = 400
    MESSAGE = "Duplicate clientRequestID"
    DESCRIPTION = "The clientRequestID already exists with mismatched brand or value"
    API_VERSION = 2


class RelationshipNotFound(TilloException):
    """Raised when no relationship exists between partner and brand.

    This error occurs when attempting to perform operations that require
    an established relationship between the partner and brand.
    """

    TILLO_ERROR_CODE = "709"
    HTTP_ERROR_CODE = 404
    MESSAGE = "No relationship found"
    DESCRIPTION = "No relationship exists between partner and brand"
    API_VERSION = 2


class CancelNotActive(TilloException):
    """Raised when attempting to cancel an inactive card.

    This error occurs when trying to cancel a card that is no longer
    in an active state.
    """

    TILLO_ERROR_CODE = "711"
    HTTP_ERROR_CODE = 400
    MESSAGE = "Cancel not active"
    DESCRIPTION = "Card no longer active"
    API_VERSION = 2


class DeliveryMethodNotFound(TilloException):
    """Raised when the requested delivery method doesn't exist.

    This error occurs when attempting to use a delivery method that
    is not available in the system.
    """

    TILLO_ERROR_CODE = "712"
    HTTP_ERROR_CODE = 404
    MESSAGE = "Delivery method not found"
    DESCRIPTION = "The requested delivery method was not found"
    API_VERSION = 2


class InvalidDeliveryMethod(TilloException):
    """Raised when the delivery method is not allowed.

    This error occurs when attempting to use a delivery method that
    is not permitted for the current operation.
    """

    TILLO_ERROR_CODE = "713"
    HTTP_ERROR_CODE = 400
    MESSAGE = "Invalid delivery method"
    DESCRIPTION = "The delivery method is not allowed"
    API_VERSION = 2


class MissingDeliveryMethod(TilloException):
    """Raised when no delivery method is specified.

    This error occurs when a delivery method is required but not
    provided in the request.
    """

    TILLO_ERROR_CODE = "714"
    HTTP_ERROR_CODE = 400
    MESSAGE = "Missing delivery method"
    DESCRIPTION = "You did not supply a delivery method"
    API_VERSION = 2


class UrlHostingServiceUnavailable(TilloException):
    """Raised when the URL hosting service is unavailable.

    This error occurs when the service responsible for hosting URLs
    is temporarily unavailable.
    """

    TILLO_ERROR_CODE = "715"
    HTTP_ERROR_CODE = 503
    MESSAGE = "URL hosting service unavailable"
    DESCRIPTION = "The URL hosting service is currently unavailable"
    API_VERSION = 2


class TemplateNotFound(TilloException):
    """Raised when the requested template doesn't exist.

    This error occurs when attempting to use a template that
    is not found in the system.
    """

    TILLO_ERROR_CODE = "716"
    HTTP_ERROR_CODE = 400
    MESSAGE = "Template not found"
    DESCRIPTION = "The requested template was not found"
    API_VERSION = 2


class TemplateAccessDenied(TilloException):
    """Raised when access to the template is denied.

    This error occurs when the partner doesn't have permission
    to access the requested template for the brand.
    """

    TILLO_ERROR_CODE = "717"
    HTTP_ERROR_CODE = 401
    MESSAGE = "Template access denied"
    DESCRIPTION = "The partner does not have access to the template for the requested brand"
    API_VERSION = 2


class UnsupportedTransactionType(TilloException):
    """Raised when the transaction type is not supported.

    This error occurs when attempting to perform a transaction type
    that is not supported by the partner.
    """

    TILLO_ERROR_CODE = "719"
    HTTP_ERROR_CODE = 422
    MESSAGE = "Transaction type not supported"
    DESCRIPTION = "The transaction type is not supported by the partner"
    API_VERSION = 2


class UnsupportedBrandTransactionType(TilloException):
    """Raised when the transaction type is not supported for the brand.

    This error occurs when attempting to perform a transaction type
    that is not supported for the requested brand.
    """

    TILLO_ERROR_CODE = "720"
    HTTP_ERROR_CODE = 422
    MESSAGE = "Brand transaction type not supported"
    DESCRIPTION = "The transaction type is not supported for the requested brand"
    API_VERSION = 2


class CurrencyIsoCodeNotFound(TilloException):
    """Raised when the requested currency is not found.

    This error occurs when attempting to use a currency that
    is not available in the system.
    """

    TILLO_ERROR_CODE = "721"
    HTTP_ERROR_CODE = 422
    MESSAGE = "Currency ISO code not found"
    DESCRIPTION = "The requested currency was not found"
    API_VERSION = 2


class MissingCurrencyIsoCode(TilloException):
    """Raised when no currency is specified.

    This error occurs when a currency is required but not
    provided in the request.
    """

    TILLO_ERROR_CODE = "722"
    HTTP_ERROR_CODE = 400
    MESSAGE = "Missing currency iso code"
    DESCRIPTION = "You did not supply a currency"
    API_VERSION = 2


class UnsupportedCurrencyIsoCode(TilloException):
    """Raised when the currency is not supported for the brand.

    This error occurs when attempting to use a currency that
    is not supported by the requested brand.
    """

    TILLO_ERROR_CODE = "723"
    HTTP_ERROR_CODE = 422
    MESSAGE = "Unsupported currency iso code"
    DESCRIPTION = "The requested currency iso code is not supported by this brand"
    API_VERSION = 2


class SaleNotFound(TilloException):
    """Raised when the sale reference cannot be found.

    This error occurs when attempting to access a sale that
    doesn't exist in the system.
    """

    TILLO_ERROR_CODE = "724"
    HTTP_ERROR_CODE = 422
    MESSAGE = "Sale reference not found"
    DESCRIPTION = "The sale reference could not be found"
    API_VERSION = 2


class DenominationNotInStock(TilloException):
    """Raised when the requested denomination is out of stock.

    This error occurs when attempting to use a denomination that
    is currently not available in stock.
    """

    TILLO_ERROR_CODE = "725"
    HTTP_ERROR_CODE = 500
    MESSAGE = "Denomination not in stock"
    DESCRIPTION = "The requested denomination is not in stock"
    API_VERSION = 2


class FeatureNotEnabled(TilloException):
    """Raised when the requested feature is not enabled.

    This error occurs when attempting to use a feature that
    has not been enabled for the account.
    """

    TILLO_ERROR_CODE = "726"
    HTTP_ERROR_CODE = 503
    MESSAGE = "Feature not enabled"
    DESCRIPTION = "The requested feature has not been enabled"
    API_VERSION = 2


class InsufficientBalanceOnCard(TilloException):
    """Raised when there are insufficient funds on the card.

    This error occurs when attempting to perform an operation that
    requires more funds than are available on the card.
    """

    TILLO_ERROR_CODE = "728"
    HTTP_ERROR_CODE = 403
    MESSAGE = "Insufficient balance on card"
    DESCRIPTION = "Insufficient balance on card"
    API_VERSION = 2


class DuplicateRequestIncomplete(TilloException):
    """Raised when a duplicate request is still being processed.

    This error occurs when attempting to submit a request that
    is identical to one that is still being processed.
    """

    TILLO_ERROR_CODE = "729"
    HTTP_ERROR_CODE = 400
    MESSAGE = "Duplicate request"
    DESCRIPTION = "The original request is still being processed"
    API_VERSION = 2


class InvalidSaleReference(TilloException):
    """Raised when the sale reference is invalid.

    This error occurs when attempting to use a sale reference that
    is not in the correct format or is invalid.
    """

    TILLO_ERROR_CODE = "730"
    HTTP_ERROR_CODE = 400
    MESSAGE = "Invalid sale reference"
    DESCRIPTION = "The provided sale reference is invalid"
    API_VERSION = 2


class SaleRedemptionInProgress(TilloException):
    """Raised when redemption is already in progress for the sale.

    This error occurs when attempting to start a redemption process
    for a sale that is already being redeemed.
    """

    TILLO_ERROR_CODE = "732"
    HTTP_ERROR_CODE = 425
    MESSAGE = "Sale redemption in progress"
    DESCRIPTION = "Redemption for this sale is already in progress"
    API_VERSION = 2


class InvalidOrderStatus(TilloException):
    """Raised when the order status is invalid for the operation.

    This error occurs when attempting to perform an operation that
    is not allowed in the current order status.
    """

    TILLO_ERROR_CODE = "733"
    HTTP_ERROR_CODE = 422
    MESSAGE = "Invalid order status"
    DESCRIPTION = "Cannot fulfil order, invalid status"
    API_VERSION = 2


class InvalidRedemptionStatus(TilloException):
    """Raised when the redemption status is invalid for the operation.

    This error occurs when attempting to perform an operation that
    is not allowed in the current redemption status.
    """

    TILLO_ERROR_CODE = "734"
    HTTP_ERROR_CODE = 422
    MESSAGE = "Invalid redemption status"
    DESCRIPTION = "Cannot fulfil order, invalid redemption status"
    API_VERSION = 2


class SaleExpired(TilloException):
    """Raised when attempting to perform an action on an expired sale.

    This error occurs when trying to perform operations on a sale
    that has passed its expiration date.
    """

    TILLO_ERROR_CODE = "735"
    HTTP_ERROR_CODE = 410
    MESSAGE = "Sale expired"
    DESCRIPTION = "The sale has expired, preventing any further action"
    API_VERSION = 2


class InvalidFinancialRelationship(TilloException):
    """Raised when the financial relationship is invalid.

    This error occurs when attempting to perform an operation that
    requires a valid financial relationship that doesn't exist.
    """

    TILLO_ERROR_CODE = "736"
    HTTP_ERROR_CODE = 400
    MESSAGE = "Invalid financial relationship"
    DESCRIPTION = "Cannot fulfil order, invalid financial relationship"
    API_VERSION = 2


class CurrencyForInternationalPaymentsOnly(TilloException):
    """Raised when the currency is only available for international payments.

    This error occurs when attempting to use a currency that is
    restricted to international payment operations only.
    """

    TILLO_ERROR_CODE = "738"
    HTTP_ERROR_CODE = 422
    MESSAGE = "Currency only for international payments"
    DESCRIPTION = "The requested currency is only available with International Payments"
    API_VERSION = 2


class UnsupportedBrandForInternationalPayments(TilloException):
    """Raised when the brand is not supported for international payments.

    This error occurs when attempting to use a brand that is not
    supported for international payment operations.
    """

    TILLO_ERROR_CODE = "739"
    HTTP_ERROR_CODE = 422
    MESSAGE = "Brand not supported for international payments"
    DESCRIPTION = "The requested brand is not supported by International Payments"
    API_VERSION = 2


class FeatureOnlyAvailableInApiV2(TilloException):
    """Raised when attempting to use a feature only available in API v2.

    This error occurs when trying to use a feature that is
    exclusively available in API version 2.
    """

    TILLO_ERROR_CODE = "740"
    HTTP_ERROR_CODE = 400
    MESSAGE = "Feature only available in API v2"
    DESCRIPTION = "The requested feature is only available through API v2"
    API_VERSION = "2"


class EndpointNotFound(TilloException):
    """Raised when the requested endpoint doesn't exist.

    This error occurs when attempting to access an API endpoint
    that is not available in the system.
    """

    TILLO_ERROR_CODE = "999"
    HTTP_ERROR_CODE = 404
    MESSAGE = "Endpoint not found"
    DESCRIPTION = "The requested endpoint was not found"
    API_VERSION = 2


class MethodNotAllowed(TilloException):
    """Raised when the HTTP method is not allowed for the endpoint.

    This error occurs when attempting to use an HTTP method that
    is not supported for the requested endpoint.
    """

    TILLO_ERROR_CODE = "999"
    HTTP_ERROR_CODE = 405
    MESSAGE = "Method not allowed"
    DESCRIPTION = "The requested method is not allowed"
    API_VERSION = 2


class InternalServerError(TilloException):
    """Raised when an internal server error occurs.

    This error occurs when there is an unexpected error on the
    Tillo server side.
    """

    TILLO_ERROR_CODE = "999"
    HTTP_ERROR_CODE = 500
    MESSAGE = "Internal error"
    DESCRIPTION = "An internal server error occurred"
    API_VERSION = 2
