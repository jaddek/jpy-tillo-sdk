from enum import Enum

class Domains(Enum):
    BRANDS = 'brands'
    TEMPLATES = 'templates'
    TEMPLATE = 'template'
    DIGITAL_CARD = 'digital'


class Status(Enum):
    DISABLED = "disabled"
    ENABLED = "enabled"


class Currency(Enum):
    EUR = "EUR"
    GBP = "GBP"


class DeliveryMethod(Enum):
    """
    code    - The plain code is returned in the API response
    url     - A hosted URL is returned in the API response
    """

    CODE = ("code",)
    URL = ("url",)
    EXPIRING_URL = "expiring-url"


class TransactionType(Enum):
    """
    Transaction Type              | Endpoint
    -----------------------------------------
    digital_issuance              - createGC
    cancelled_digital_issuance    - cancelGC
    physical_activation           - activateGC
    cancelled_physical_activation - cancelActivateGC
    physical_top_up               - topupGC
    cancelled_physical_top_up     - cancelTopupGC
    """

    DIGITAL_ISSUANCE = "digital_issuance"
    CANCELLED_DIGITAL_ISSUANCE = "cancelled_digital_issuance"
    PHYSICAL_ACTIVATION = "physical_activation"
    CANCELLED_PHYSICAL_ACTIVATION = "cancelled_physical_activation"
    PHYSICAL_TOP_UP = "physical_top_up"
    CANCELLED_PHYSICAL_TOP_UP = "cancelled_physical_top_up"


class FulfilmentType(Enum):
    PARTNER = "partner"
    REWARD_CLOUD = "rewardcloud"


class OrderStatus(Enum):
    """
    Status	   | Description                      | Next Steps
    --
    REQUESTED
    PENDING
    PROCESSING | The order was submitted          | Wait before making another order status check.
                 to Tillo successfully            | See our throttling documentation.
    --
    SUCCESS	   | The order succeeded.             | The code or URL will be provided
    --
    ERROR	   | There was an unrecoverable       | We will have automatically refunded you for your transaction.
                 issue with processing your order | In the majority of cases you will be able to order the code from
                                                  | us again.
    """

    REQUESTED = "requested"
    PENDING = "pending"
    PROCESSING = "processing"
    SUCCESS = "success"
    ERROR = "error"


class Sector(Enum):
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
    ONLINE = "Online"
    INSTORE = "Instore"
    PHONE = "Phone"
