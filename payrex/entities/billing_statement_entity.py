from typing import Any, Literal, Optional, TypedDict
from payrex.common_types import Currency, PaymentMethod


class BillingStatementEntity:
    def __init__(self, api_resource):
        data = api_resource.data

        self.id: str = data.get('id')
        self.billing_details_collection: str = data.get('billing_details_collection')
        self.billing_statement_merchant_name: Optional[str] = data.get('billing_statement_merchant_name')
        self.billing_statement_number: Optional[str] = data.get('billing_statement_number')
        self.billing_statement_url: str = data.get('billing_statement_url')
        self.customer_reference_id = data.get('customer_reference_id') # TODO: rename to customer_id
        self.client_secret = data.get('client_secret')
        self.status: Literal[
            "open",
            "draft",
            "paid",
            "void",
            "uncollectible"
        ] = data.get('status')
        self.currency: Currency = data.get('currency')
        self.line_items: 'list[BillingStatementLineItem]' = data.get('line_items')
        self.livemode: bool = data.get('livemode')
        self.payment_intent: Optional[dict[str, Any]] = data.get('payment_intent') # TODO: payment intent type hint
        self.metadata: Optional[dict[str, str]] = data.get('metadata')
        self.success_url = data.get('success_url')
        self.cancel_url = data.get('cancel_url')
        self.payment_methods = data.get('payment_methods')
        self.setup_future_usage = data.get('setup_future_usage')
        self.statement_descriptor: Optional[str] = data.get('statement_descriptor')
        self.description: Optional[str] = data.get('description')
        self.submit_type = data.get('submit_type')
        self.expires_at = data.get('expires_at')
        self.created_at: int = data.get('created_at')
        self.updated_at: int = data.get('updated_at')


class PaymentSettings(TypedDict):
    payment_methods: list[PaymentMethod]


class BillingStatementLineItem(TypedDict):
    id: str
    resource: Literal["billing_statement_line_item"]
    description: str
    unit_price: int
    quantity: int
