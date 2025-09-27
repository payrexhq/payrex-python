from typing import Optional
from payrex.common_types import Currency


class CustomerEntity:
    def __init__(self, api_resource):
        data = api_resource.data

        self.id: str = data.get('id')
        self.billing_statement_prefix: str = data.get('billing_statement_prefix')
        self.currency: Currency = data.get('currency')
        self.email: str = data.get('email')
        self.livemode: bool = data.get('livemode')
        self.name: str = data.get('name')
        self.metadata: Optional[dict[str, str]] = data.get('metadata')
        self.next_billing_statement_sequence_number: str = data.get('next_billing_statement_sequence_number')
        self.created_at: int = data.get('created_at')
        self.updated_at: int = data.get('updated_at')
