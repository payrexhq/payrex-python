from typing import Literal, Optional, TypedDict
from payrex.common_types import Currency, PaymentMethod


class PaymentEntity:
    def __init__(self, api_resource):
        data = api_resource.data

        self.id: str = data.get('id')
        self.amount: int = data.get('amount')
        self.amount_refunded: int = data.get('amount_refunded')
        self.billing: Billing = data.get('billing')
        self.currency: Currency = data.get('currency')
        self.description: Optional[str] = data.get('description')
        self.fee: int = data.get('fee')
        self.livemode: bool = data.get('livemode')
        self.metadata: Optional[dict[str, str]] = data.get('metadata')
        self.net_amount: int = data.get('net_amount')
        self.payment_intent_id: str = data.get('payment_intent_id')
        self.status: Literal["paid", "failed"] = data.get('status')
        self.customer = data.get('customer') # TODO: customer resource type hint
        self.payment_method: PaymentMethodDict = data.get('payment_method')
        self.refunded: bool = data.get('refunded')
        self.created_at: int = data.get('created_at')
        self.updated_at: int = data.get('updated_at')


class Billing(TypedDict):
    name: str
    email: str
    phone: Optional[str]
    address: 'Address'


class Address(TypedDict):
    line1: str
    line2: Optional[str]
    city: str
    state: str
    postal_code: str
    country: str


class PaymentMethodDict(TypedDict):
    type: PaymentMethod
