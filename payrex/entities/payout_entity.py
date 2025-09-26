from typing import Literal, TypedDict


class PayoutEntity:
    def __init__(self, api_resource):
        data = api_resource.data

        self.id: str = data.get('id')
        self.amount: int = data.get('amount')
        self.destination: PayoutDestination = data.get('destination')
        self.livemode: bool = data.get('livemode')
        self.net_amount: int = data.get('net_amount')
        self.status: PayoutStatus = data.get('status')
        self.created_at: int = data.get('created_at')
        self.updated_at: int = data.get('updated_at')


class PayoutDestination(TypedDict):
    account_name: str
    account_number: str
    bank_name: str


PayoutStatus = Literal[
    "pending",
    "in_transit",
    "failed",
    "successful",
]
