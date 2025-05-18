"""Tillo SDK Enumerations.

This module contains all enumeration classes used throughout the Tillo SDK.
These enums provide type-safe constants for various aspects of the API,
including domains, statuses, currencies, and transaction types.

Example:
    ```python
    from jpy_tillo_sdk.enums import Currency, DeliveryMethod

    # Using enums in API requests
    currency = Currency.GBP
    delivery = DeliveryMethod.CODE
    ```
"""

from enum import Enum


class Domains(Enum):
    """API domain endpoints for different Tillo services.

    These domains represent the different service areas of the Tillo API.
    Each domain corresponds to a specific set of endpoints and functionality.

    Attributes:
        BRANDS: Endpoints for brand management
        TEMPLATES: Endpoints for template listing
        TEMPLATE: Endpoints for individual template operations
        DIGITAL_CARD: Endpoints for digital card operations
        CHECK_STOCK: Endpoints for stock checking
        CHECK_FLOATS: Endpoints for float checking
    """

    BRANDS = "brands"
    TEMPLATES = "templates"
    TEMPLATE = "template"
    DIGITAL_CARD = "digital"
    CHECK_STOCK = "check-stock"
    CHECK_FLOATS = "check-floats"


class Status(Enum):
    """Status values for various Tillo resources.

    Used to indicate whether a resource is enabled or disabled in the system.

    Attributes:
        DISABLED: Resource is not available for use
        ENABLED: Resource is available and active
    """

    DISABLED = "disabled"
    ENABLED = "enabled"


class Currency(Enum):
    """Supported currency codes for transactions.

    These are the currencies supported by the Tillo platform for
    gift card transactions and other monetary operations.

    Attributes:
        EUR: Euro
        GBP: British Pound Sterling
        UNIVERSAL_FLOAT = "some universal float"
    """

    EUR = "EUR"
    GBP = "GBP"
    UNIVERSAL_FLOAT = "universal-float"


class DeliveryMethod(Enum):
    """Methods for delivering gift card codes to customers.

    Defines how gift card codes are delivered to end users, either as
    plain codes or through hosted URLs.

    Attributes:
        CODE: Returns a plain code in the API response
        URL: Returns a hosted URL in the API response
        EXPIRING_URL: Returns a time-limited hosted URL

    Note:
        The delivery method affects how the gift card code is presented
        to the end user and may have different security implications.
    """

    CODE = "code"
    URL = "url"
    EXPIRING_URL = "expiring-url"


class TransactionType(Enum):
    """Types of transactions supported by the Tillo platform.

    Each transaction type corresponds to specific API endpoints and
    operations in the system.

    Attributes:
        DIGITAL_ISSUANCE: Creating a new digital gift card
        CANCELLED_DIGITAL_ISSUANCE: Cancelling a digital gift card
        PHYSICAL_ACTIVATION: Activating a physical gift card
        CANCELLED_PHYSICAL_ACTIVATION: Cancelling a physical card activation
        PHYSICAL_TOP_UP: Adding funds to a physical gift card
        CANCELLED_PHYSICAL_TOP_UP: Cancelling a physical card top-up

    Note:
        Each transaction type maps to specific API endpoints:
        - digital_issuance -> createGC
        - cancelled_digital_issuance -> cancelGC
        - physical_activation -> activateGC
        - cancelled_physical_activation -> cancelActivateGC
        - physical_top_up -> topupGC
        - cancelled_physical_top_up -> cancelTopupGC
    """

    DIGITAL_ISSUANCE = "digital_issuance"
    CANCELLED_DIGITAL_ISSUANCE = "cancelled_digital_issuance"
    PHYSICAL_ACTIVATION = "physical_activation"
    CANCELLED_PHYSICAL_ACTIVATION = "cancelled_physical_activation"
    PHYSICAL_TOP_UP = "physical_top_up"
    CANCELLED_PHYSICAL_TOP_UP = "cancelled_physical_top_up"


class FulfilmentType(Enum):
    """Types of fulfilment methods for gift cards.

    Defines how gift cards are fulfilled in the system, either through
    the partner or through Reward Cloud.

    Attributes:
        PARTNER: Fulfilment handled by the partner
        REWARD_CLOUD: Fulfilment handled by Reward Cloud
    """

    PARTNER = "partner"
    REWARD_CLOUD = "rewardcloud"


class OrderStatus(Enum):
    """Status values for gift card orders.

    Represents the various states an order can be in during its lifecycle.
    Each status indicates the current state of the order and what actions
    can be taken next.

    Attributes:
        REQUESTED: Initial order request received
        PENDING: Order is waiting to be processed
        PROCESSING: Order is being processed by Tillo
        SUCCESS: Order completed successfully
        ERROR: Order failed with an unrecoverable error

    Note:
        Status Flow and Actions:
        - REQUESTED/PENDING/PROCESSING: Wait before checking status again
        - SUCCESS: Code or URL will be provided
        - ERROR: Automatic refund issued, can retry order
    """

    REQUESTED = "requested"
    PENDING = "pending"
    PROCESSING = "processing"
    SUCCESS = "success"
    ERROR = "error"


class Sector(Enum):
    """Business sectors supported by Tillo.

    Defines the different types of businesses and use cases that
    Tillo supports for gift card operations.

    Attributes:
        GIFT_CARD_MALL: Online gift card marketplaces
        AGGREGATOR: Gift card aggregation services
        B2C_MARKETPLACE: Business-to-consumer marketplaces
        CASH_OUT: Cash out services
        CASHBACK: Cashback programs
        CONSUMER_REWARDS_AND_INCENTIVES: Consumer reward programs
        CRYPTO_OFF_RAMP: Cryptocurrency conversion services
        EMPLOYEE_BENEFITS: Employee benefit programs
        EMPLOYEE_REWARDS_AND_INCENTIVES: Employee reward programs
        OTHER: Other business types
        RELIEF_SUPPORT_AND_DISBURSEMENT: Relief and support programs
    """

    GIFT_CARD_MALL = "gift-card-mall"
    AGGREGATOR = "aggregator"
    B2C_MARKETPLACE = "b2c-marketplace"
    CASH_OUT = "cash-out"
    CASHBACK = "cashback"
    CONSUMER_REWARDS_AND_INCENTIVES = "consumer-rewards-and-incentives"
    CRYPTO_OFF_RAMP = "crypto-off-ramp"
    EMPLOYEE_BENEFITS = "employee-benefits"
    EMPLOYEE_REWARDS_AND_INCENTIVES = "employee-rewards-and-incentives"
    OTHER = "other"
    RELIEF_SUPPORT_AND_DISBURSEMENT = "relief-support-and-disbursement"


class Redemption(Enum):
    """Methods for redeeming gift cards.

    Defines the different ways a gift card can be redeemed by the end user.

    Attributes:
        ONLINE: Redemption through online channels
        INSTORE: Redemption at physical store locations
        PHONE: Redemption through phone channels
    """

    ONLINE = "Online"
    INSTORE = "Instore"
    PHONE = "Phone"
