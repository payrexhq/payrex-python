from typing import Any, Literal, Optional, TypedDict
from typing_extensions import NotRequired
from payrex.type_defs import Currency, PaymentMethod


class CheckoutSessionEntity:
    def __init__(self, api_resource):
        data = api_resource.data

        self.id: str = data.get('id')
        self.billing_details_collection: str = data.get('billing_details_collection')
        self.customer_reference_id: Optional[str] = data.get('customer_reference_id')
        self.client_secret: str = data.get('client_secret')
        self.status: Literal["active", "completed", "expired"] = data.get('status')
        self.currency: Currency = data.get('currency')
        self.line_items: list[CheckoutSessionLineItem] = data.get('line_items')
        self.livemode: bool = data.get('livemode')
        self.url: str = data.get('url')
        self.payment_intent: dict[str, Any] = data.get('payment_intent') # TODO: payment_intent type hint
        self.metadata: Optional[dict[str, str]] = data.get('metadata')
        self.success_url: str = data.get('success_url')
        self.cancel_url: str = data.get('cancel_url')
        self.payment_methods: list[PaymentMethod] = data.get('payment_methods')
        self.description: Optional[str] = data.get('description')
        self.submit_type: str = data.get('submit_type')
        self.expires_at: int = data.get('expires_at')
        self.created_at: int = data.get('created_at')
        self.updated_at: int = data.get('updated_at')


class CheckoutSessionLineItem(TypedDict):
    id: str
    resource: Literal["checkout_session_line_item"]
    name: str
    amount: int
    quantity: int
    description: NotRequired[str]
    image: NotRequired[str]
