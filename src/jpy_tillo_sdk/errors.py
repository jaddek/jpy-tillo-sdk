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

from httpx import Response


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

    response: Response | None = None

    def __init__(self, response: Response | None = None) -> None:
        self.response = response

    TILLO_ERROR_CODE: str | None = None
    HTTP_ERROR_CODE: int | None = None
    MESSAGE: str | None = None
    DESCRIPTION: str | None = None
    API_VERSION: int | None = None

    def __str__(self) -> str:
        return f"{self.MESSAGE} (Tillo Error {self.TILLO_ERROR_CODE}, HTTP {self.HTTP_ERROR_CODE})"


# Authentication Errors
class AuthenticationError(TilloException):
    """Base class for authentication-related errors.

    This error is raised when there are issues with API authentication,
    such as missing or invalid credentials.
    """

    TILLO_ERROR_CODE: str | None = None
    HTTP_ERROR_CODE: int | None = 401
    MESSAGE: str | None = "Pair API-Token or Secret-key not provided."
    DESCRIPTION: str | None = "No API key provided."
    API_VERSION: int | None = 1


class ValidationError(TilloException):
    TILLO_ERROR_CODE: str | None = "433"
    HTTP_ERROR_CODE: int | None = 422
    MESSAGE: str | None = "Validation Errors"
    DESCRIPTION: str | None = "There were errors validating the request"
    API_VERSION: int | None = 2


class AuthenticationFailed(TilloException):
    TILLO_ERROR_CODE: str | None = "434"
    HTTP_ERROR_CODE: int | None = 404
    MESSAGE: str | None = "Authentication failed"
    DESCRIPTION: str | None = "Authentication failed"
    API_VERSION: int | None = 2


class AuthorizationErrorInvalidAPITokenOrSecret(AuthenticationError):
    """Raised when the provided API token or secret is invalid.

    This error occurs when either the API token or secret key is missing,
    invalid, or expired.
    """

    TILLO_ERROR_CODE: str | None = "-1"
    HTTP_ERROR_CODE: int | None = -1
    MESSAGE: str | None = "Invalid API or Secret Key provided."
    DESCRIPTION: str | None = "Check API token or secret key provided for Tillo SDK."
    API_VERSION: int | None = 0


# API-Specific Errors
class InvalidApiToken(TilloException):
    """Raised when the API token is invalid or expired.

    This error occurs when the provided API token is either invalid or has expired.
    A new valid API token should be obtained from the Tillo dashboard.
    """

    TILLO_ERROR_CODE: str | None = "060"
    HTTP_ERROR_CODE: int | None = 400
    MESSAGE: str | None = "Token mismatch error"
    DESCRIPTION: str | None = "Invalid or expired API Token"
    API_VERSION: int | None = 1


class MissingParameters(TilloException):
    """Raised when required parameters are missing from the request.

    This error occurs when essential parameters like amount or personalization
    are not provided in the API request.
    """

    TILLO_ERROR_CODE: str | None = "070"
    HTTP_ERROR_CODE: int | None = 400
    MESSAGE: str | None = "Missing parameter"
    DESCRIPTION: str | None = "Missing parameter amount or personalisation"
    API_VERSION: int | None = 2


class MissingParameterAmount(TilloException):
    """Raised when the amount parameter is missing.

    This error occurs when the additionalParams parameter is not provided
    in the API request.
    """

    TILLO_ERROR_CODE: str | None = "071"
    HTTP_ERROR_CODE: int | None = 400
    MESSAGE: str | None = "Missing parameter"
    DESCRIPTION: str | None = "Missing additionalParams"
    API_VERSION: int | None = 1


class BrandNotFound(TilloException):
    """Raised when the requested brand does not exist.

    This error occurs when attempting to access a brand that doesn't exist
    in the Tillo system.
    """

    TILLO_ERROR_CODE: str | None = "072"
    HTTP_ERROR_CODE: int | None = 400
    MESSAGE: str | None = "Brand not found"
    DESCRIPTION: str | None = "The requested brand does not exist"
    API_VERSION: int | None = 2


class InvalidBrandForPartner(TilloException):
    """Raised when the brand is not available for the partner.

    This error occurs when a partner attempts to access a brand they
    don't have permission to use.
    """

    TILLO_ERROR_CODE: str | None = "072"
    HTTP_ERROR_CODE: int | None = 401
    MESSAGE: str | None = "Invalid brand for partner"
    DESCRIPTION: str | None = "Brand is not available for this partner"
    API_VERSION: int | None = 2


class GiftCodeCancelled(TilloException):
    """Raised when attempting to perform an action on a cancelled gift code.

    This error occurs when trying to perform operations on a gift code
    that has already been cancelled.
    """

    TILLO_ERROR_CODE: str | None = "100"
    HTTP_ERROR_CODE: int | None = 422
    MESSAGE: str | None = "The gift code has already been cancelled"
    DESCRIPTION: str | None = "Attempted action on a cancelled gift code"
    API_VERSION: int | None = 2


class UnprocessableContent(TilloException):
    TILLO_ERROR_CODE: str | None = "100"
    HTTP_ERROR_CODE: int | None = 422
    MESSAGE: str | None = "Unprocessable Content"
    DESCRIPTION: str | None = "Unprocessable Content"
    API_VERSION: int | None = 2


class InvalidIpAddress(TilloException):
    """Raised when the request comes from an unauthorized IP address.

    This error occurs when the request originates from an IP address
    that is not whitelisted in the Tillo system.
    """

    TILLO_ERROR_CODE: str | None = "210"
    HTTP_ERROR_CODE: int | None = 401
    MESSAGE: str | None = "Invalid IP address"
    DESCRIPTION: str | None = "IP address is not authorized"
    API_VERSION: int | None = 2


class InsufficientMonies(TilloException):
    """Raised when there are insufficient funds in the account.

    This error occurs when attempting to perform an operation that
    requires more funds than are available in the account.
    """

    TILLO_ERROR_CODE: str | None = "610"
    HTTP_ERROR_CODE: int | None = 403
    MESSAGE: str | None = "Insufficient Monies"
    DESCRIPTION: str | None = "Insufficient balance on account"
    API_VERSION: int | None = 2


class InsufficientMoniesOnAccount(TilloException):
    """Raised when there are insufficient funds for the operation.

    This error occurs when the account balance is too low to complete
    the requested operation.
    """

    TILLO_ERROR_CODE: str | None = "610"
    HTTP_ERROR_CODE: int | None = 422
    MESSAGE: str | None = "Insufficient balance"
    DESCRIPTION: str | None = "Insufficient balance on account"
    API_VERSION: int | None = 2


class InvalidValue(TilloException):
    """Raised when an invalid or unsupported value is provided.

    This error occurs when a parameter value is outside the allowed
    range or format.
    """

    TILLO_ERROR_CODE: str | None = "704"
    HTTP_ERROR_CODE: int | None = 400
    MESSAGE: str | None = "Invalid value"
    DESCRIPTION: str | None = "Invalid or unsupported value provided"
    API_VERSION: int | None = 2


class SaleDisabled(TilloException):
    """Raised when attempting to make a sale for a disabled brand.

    This error occurs when trying to process a sale for a brand that
    is currently not available for sale.
    """

    TILLO_ERROR_CODE: str | None = "706"
    HTTP_ERROR_CODE: int | None = 401
    MESSAGE: str | None = "Sale is disabled"
    DESCRIPTION: str | None = "The brand is not available for sale"
    API_VERSION: int | None = 2


class DuplicateClientRequest(TilloException):
    """Raised when a duplicate clientRequestID is detected.

    This error occurs when attempting to use a clientRequestID that
    already exists with different brand or value parameters.
    """

    TILLO_ERROR_CODE: str | None = "708"
    HTTP_ERROR_CODE: int | None = 400
    MESSAGE: str | None = "Duplicate clientRequestID"
    DESCRIPTION: str | None = "The clientRequestID already exists with mismatched brand or value"
    API_VERSION: int | None = 2


class RelationshipNotFound(TilloException):
    """Raised when no relationship exists between partner and brand.

    This error occurs when attempting to perform operations that require
    an established relationship between the partner and brand.
    """

    TILLO_ERROR_CODE: str | None = "709"
    HTTP_ERROR_CODE: int | None = 404
    MESSAGE: str | None = "No relationship found"
    DESCRIPTION: str | None = "No relationship exists between partner and brand"
    API_VERSION: int | None = 2


class CancelNotActive(TilloException):
    """Raised when attempting to cancel an inactive card.

    This error occurs when trying to cancel a card that is no longer
    in an active state.
    """

    TILLO_ERROR_CODE: str | None = "711"
    HTTP_ERROR_CODE: int | None = 400
    MESSAGE: str | None = "Cancel not active"
    DESCRIPTION: str | None = "Card no longer active"
    API_VERSION: int | None = 2


class DeliveryMethodNotFound(TilloException):
    """Raised when the requested delivery method doesn't exist.

    This error occurs when attempting to use a delivery method that
    is not available in the system.
    """

    TILLO_ERROR_CODE: str | None = "712"
    HTTP_ERROR_CODE: int | None = 404
    MESSAGE: str | None = "Delivery method not found"
    DESCRIPTION: str | None = "The requested delivery method was not found"
    API_VERSION: int | None = 2


class InvalidDeliveryMethod(TilloException):
    """Raised when the delivery method is not allowed.

    This error occurs when attempting to use a delivery method that
    is not permitted for the current operation.
    """

    TILLO_ERROR_CODE: str | None = "713"
    HTTP_ERROR_CODE: int | None = 400
    MESSAGE: str | None = "Invalid delivery method"
    DESCRIPTION: str | None = "The delivery method is not allowed"
    API_VERSION: int | None = 2


class MissingDeliveryMethod(TilloException):
    """Raised when no delivery method is specified.

    This error occurs when a delivery method is required but not
    provided in the request.
    """

    TILLO_ERROR_CODE: str | None = "714"
    HTTP_ERROR_CODE: int | None = 400
    MESSAGE: str | None = "Missing delivery method"
    DESCRIPTION: str | None = "You did not supply a delivery method"
    API_VERSION: int | None = 2


class UrlHostingServiceUnavailable(TilloException):
    """Raised when the URL hosting service is unavailable.

    This error occurs when the service responsible for hosting URLs
    is temporarily unavailable.
    """

    TILLO_ERROR_CODE: str | None = "715"
    HTTP_ERROR_CODE: int | None = 503
    MESSAGE: str | None = "URL hosting service unavailable"
    DESCRIPTION: str | None = "The URL hosting service is currently unavailable"
    API_VERSION: int | None = 2


class TemplateNotFound(TilloException):
    """Raised when the requested template doesn't exist.

    This error occurs when attempting to use a template that
    is not found in the system.
    """

    TILLO_ERROR_CODE: str | None = "716"
    HTTP_ERROR_CODE: int | None = 400
    MESSAGE: str | None = "Template not found"
    DESCRIPTION: str | None = "The requested template was not found"
    API_VERSION: int | None = 2


class TemplateAccessDenied(TilloException):
    """Raised when access to the template is denied.

    This error occurs when the partner doesn't have permission
    to access the requested template for the brand.
    """

    TILLO_ERROR_CODE: str | None = "717"
    HTTP_ERROR_CODE: int | None = 401
    MESSAGE: str | None = "Template access denied"
    DESCRIPTION: str | None = "The partner does not have access to the template for the requested brand"
    API_VERSION: int | None = 2


class UnsupportedTransactionType(TilloException):
    """Raised when the transaction type is not supported.

    This error occurs when attempting to perform a transaction type
    that is not supported by the partner.
    """

    TILLO_ERROR_CODE: str | None = "719"
    HTTP_ERROR_CODE: int | None = 422
    MESSAGE: str | None = "Transaction type not supported"
    DESCRIPTION: str | None = "The transaction type is not supported by the partner"
    API_VERSION: int | None = 2


class UnsupportedBrandTransactionType(TilloException):
    """Raised when the transaction type is not supported for the brand.

    This error occurs when attempting to perform a transaction type
    that is not supported for the requested brand.
    """

    TILLO_ERROR_CODE: str | None = "720"
    HTTP_ERROR_CODE: int | None = 422
    MESSAGE: str | None = "Brand transaction type not supported"
    DESCRIPTION: str | None = "The transaction type is not supported for the requested brand"
    API_VERSION: int | None = 2


class CurrencyIsoCodeNotFound(TilloException):
    """Raised when the requested currency is not found.

    This error occurs when attempting to use a currency that
    is not available in the system.
    """

    TILLO_ERROR_CODE: str | None = "721"
    HTTP_ERROR_CODE: int | None = 422
    MESSAGE: str | None = "Currency ISO code not found"
    DESCRIPTION: str | None = "The requested currency was not found"
    API_VERSION: int | None = 2


class MissingCurrencyIsoCode(TilloException):
    """Raised when no currency is specified.

    This error occurs when a currency is required but not
    provided in the request.
    """

    TILLO_ERROR_CODE: str | None = "722"
    HTTP_ERROR_CODE: int | None = 400
    MESSAGE: str | None = "Missing currency iso code"
    DESCRIPTION: str | None = "You did not supply a currency"
    API_VERSION: int | None = 2


class UnsupportedCurrencyIsoCode(TilloException):
    """Raised when the currency is not supported for the brand.

    This error occurs when attempting to use a currency that
    is not supported by the requested brand.
    """

    TILLO_ERROR_CODE: str | None = "723"
    HTTP_ERROR_CODE: int | None = 422
    MESSAGE: str | None = "Unsupported currency iso code"
    DESCRIPTION: str | None = "The requested currency iso code is not supported by this brand"
    API_VERSION: int | None = 2


class SaleNotFound(TilloException):
    """Raised when the sale reference cannot be found.

    This error occurs when attempting to access a sale that
    doesn't exist in the system.
    """

    TILLO_ERROR_CODE: str | None = "724"
    HTTP_ERROR_CODE: int | None = 422
    MESSAGE: str | None = "Sale reference not found"
    DESCRIPTION: str | None = "The sale reference could not be found"
    API_VERSION: int | None = 2


class DenominationNotInStock(TilloException):
    """Raised when the requested denomination is out of stock.

    This error occurs when attempting to use a denomination that
    is currently not available in stock.
    """

    TILLO_ERROR_CODE: str | None = "725"
    HTTP_ERROR_CODE: int | None = 500
    MESSAGE: str | None = "Denomination not in stock"
    DESCRIPTION: str | None = "The requested denomination is not in stock"
    API_VERSION: int | None = 2


class FeatureNotEnabled(TilloException):
    """Raised when the requested feature is not enabled.

    This error occurs when attempting to use a feature that
    has not been enabled for the account.
    """

    TILLO_ERROR_CODE: str | None = "726"
    HTTP_ERROR_CODE: int | None = 503
    MESSAGE: str | None = "Feature not enabled"
    DESCRIPTION: str | None = "The requested feature has not been enabled"
    API_VERSION: int | None = 2


class InsufficientBalanceOnCard(TilloException):
    """Raised when there are insufficient funds on the card.

    This error occurs when attempting to perform an operation that
    requires more funds than are available on the card.
    """

    TILLO_ERROR_CODE: str | None = "728"
    HTTP_ERROR_CODE: int | None = 403
    MESSAGE: str | None = "Insufficient balance on card"
    DESCRIPTION: str | None = "Insufficient balance on card"
    API_VERSION: int | None = 2


class DuplicateRequestIncomplete(TilloException):
    """Raised when a duplicate request is still being processed.

    This error occurs when attempting to submit a request that
    is identical to one that is still being processed.
    """

    TILLO_ERROR_CODE: str | None = "729"
    HTTP_ERROR_CODE: int | None = 400
    MESSAGE: str | None = "Duplicate request"
    DESCRIPTION: str | None = "The original request is still being processed"
    API_VERSION: int | None = 2


class InvalidSaleReference(TilloException):
    """Raised when the sale reference is invalid.

    This error occurs when attempting to use a sale reference that
    is not in the correct format or is invalid.
    """

    TILLO_ERROR_CODE: str | None = "730"
    HTTP_ERROR_CODE: int | None = 400
    MESSAGE: str | None = "Invalid sale reference"
    DESCRIPTION: str | None = "The provided sale reference is invalid"
    API_VERSION: int | None = 2


class SaleRedemptionInProgress(TilloException):
    """Raised when redemption is already in progress for the sale.

    This error occurs when attempting to start a redemption process
    for a sale that is already being redeemed.
    """

    TILLO_ERROR_CODE: str | None = "732"
    HTTP_ERROR_CODE: int | None = 425
    MESSAGE: str | None = "Sale redemption in progress"
    DESCRIPTION: str | None = "Redemption for this sale is already in progress"
    API_VERSION: int | None = 2


class InvalidOrderStatus(TilloException):
    """Raised when the order status is invalid for the operation.

    This error occurs when attempting to perform an operation that
    is not allowed in the current order status.
    """

    TILLO_ERROR_CODE: str | None = "733"
    HTTP_ERROR_CODE: int | None = 422
    MESSAGE: str | None = "Invalid order status"
    DESCRIPTION: str | None = "Cannot fulfil order, invalid status"
    API_VERSION: int | None = 2


class InvalidRedemptionStatus(TilloException):
    """Raised when the redemption status is invalid for the operation.

    This error occurs when attempting to perform an operation that
    is not allowed in the current redemption status.
    """

    TILLO_ERROR_CODE: str | None = "734"
    HTTP_ERROR_CODE: int | None = 422
    MESSAGE: str | None = "Invalid redemption status"
    DESCRIPTION: str | None = "Cannot fulfil order, invalid redemption status"
    API_VERSION: int | None = 2


class SaleExpired(TilloException):
    """Raised when attempting to perform an action on an expired sale.

    This error occurs when trying to perform operations on a sale
    that has passed its expiration date.
    """

    TILLO_ERROR_CODE: str | None = "735"
    HTTP_ERROR_CODE: int | None = 410
    MESSAGE: str | None = "Sale expired"
    DESCRIPTION: str | None = "The sale has expired, preventing any further action"
    API_VERSION: int | None = 2


class InvalidFinancialRelationship(TilloException):
    """Raised when the financial relationship is invalid.

    This error occurs when attempting to perform an operation that
    requires a valid financial relationship that doesn't exist.
    """

    TILLO_ERROR_CODE: str | None = "736"
    HTTP_ERROR_CODE: int | None = 400
    MESSAGE: str | None = "Invalid financial relationship"
    DESCRIPTION: str | None = "Cannot fulfil order, invalid financial relationship"
    API_VERSION: int | None = 2


class CurrencyForInternationalPaymentsOnly(TilloException):
    """Raised when the currency is only available for international payments.

    This error occurs when attempting to use a currency that is
    restricted to international payment operations only.
    """

    TILLO_ERROR_CODE: str | None = "738"
    HTTP_ERROR_CODE: int | None = 422
    MESSAGE: str | None = "Currency only for international payments"
    DESCRIPTION: str | None = "The requested currency is only available with International Payments"
    API_VERSION: int | None = 2


class UnsupportedBrandForInternationalPayments(TilloException):
    """Raised when the brand is not supported for international payments.

    This error occurs when attempting to use a brand that is not
    supported for international payment operations.
    """

    TILLO_ERROR_CODE: str | None = "739"
    HTTP_ERROR_CODE: int | None = 422
    MESSAGE: str | None = "Brand not supported for international payments"
    DESCRIPTION: str | None = "The requested brand is not supported by International Payments"
    API_VERSION: int | None = 2


class FeatureOnlyAvailableInApiV2(TilloException):
    """Raised when attempting to use a feature only available in API v2.

    This error occurs when trying to use a feature that is
    exclusively available in API version 2.
    """

    TILLO_ERROR_CODE: str | None = "740"
    HTTP_ERROR_CODE: int | None = 400
    MESSAGE: str | None = "Feature only available in API v2"
    DESCRIPTION: str | None = "The requested feature is only available through API v2"
    API_VERSION: int | None = 2


class EndpointNotFound(TilloException):
    """Raised when the requested endpoint doesn't exist.

    This error occurs when attempting to access an API endpoint
    that is not available in the system.
    """

    TILLO_ERROR_CODE: str | None = "999"
    HTTP_ERROR_CODE: int | None = 404
    MESSAGE: str | None = "Endpoint not found"
    DESCRIPTION: str | None = "The requested endpoint was not found"
    API_VERSION: int | None = 2


class MethodNotAllowed(TilloException):
    """Raised when the HTTP method is not allowed for the endpoint.

    This error occurs when attempting to use an HTTP method that
    is not supported for the requested endpoint.
    """

    TILLO_ERROR_CODE: str | None = "999"
    HTTP_ERROR_CODE: int | None = 405
    MESSAGE: str | None = "Method not allowed"
    DESCRIPTION: str | None = "The requested method is not allowed"
    API_VERSION: int | None = 2


class InternalServerError(TilloException):
    """Raised when an internal server error occurs.

    This error occurs when there is an unexpected error on the
    Tillo server side.
    """

    TILLO_ERROR_CODE: str | None = "999"
    HTTP_ERROR_CODE: int | None = 500
    MESSAGE: str | None = "Internal error"
    DESCRIPTION: str | None = "An internal server error occurred"
    API_VERSION: int | None = 2
