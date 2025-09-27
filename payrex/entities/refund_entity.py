from typing import Literal, Optional

from payrex.type_defs import Currency

class RefundEntity:
    def __init__(self, api_resource):
        data = api_resource.data

        self.id: str = data.get('id')
        self.amount: int = data.get('amount')
        self.currency: Currency = data.get('currency')
        self.livemode: bool = data.get('livemode')
        self.status: Literal["succeeded", "failed", "pending"] = data.get('status')
        self.description: Optional[str] = data.get('description')
        self.reason: RefundReason = data.get('reason')
        self.remarks: Optional[str] = data.get('remarks')
        self.payment_id: str = data.get('payment_id')
        self.metadata: Optional[dict[str, str]] = data.get('metadata')
        self.created_at: int = data.get('created_at')
        self.updated_at: int = data.get('updated_at')


RefundReason = Literal[
    "fraudulent",
    "requested_by_customer",
    "product_out_of_stock",
    "service_not_provided",
    "product_was_damaged",
    "service_misaligned",
    "wrong_product_received",
    "others",
]
