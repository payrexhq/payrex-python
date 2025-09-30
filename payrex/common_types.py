from typing import Literal, TypedDict
from typing_extensions import NotRequired

PaymentMethod = Literal['card', 'gcash', 'maya', 'qrph']

# Only supported currency for now is PHP
Currency = Literal['PHP']


class PaymentMethodOptions(TypedDict):
    card: 'PaymentMethodCard'


class PaymentMethodCard(TypedDict):
    capture_type: 'CaptureType'
    allowed_bins: NotRequired[list[str]]
    allowed_funding: 'NotRequired[list[AllowedFunding]]'


CaptureType = Literal['automatic', 'manual']
AllowedFunding = Literal['credit', 'debit']
