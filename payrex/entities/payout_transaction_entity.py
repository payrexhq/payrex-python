from typing import Literal


class PayoutTransactionEntity:
    def __init__(self, api_resource):
        data = api_resource.data

        self.id: str = data.get('id')
        self.amount: int = data.get('amount')
        self.net_amount: int = data.get('net_amount')
        self.transaction_type: Literal["payment", "refund", "adjustment"] = data.get('transaction_type')
        self.transaction_id: str = data.get('transaction_id')
        self.created_at: int = data.get('created_at')
        self.updated_at: int = data.get('updated_at')
