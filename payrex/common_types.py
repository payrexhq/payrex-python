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
    allowed_funding: 'list[AllowedFunding]'


CaptureType = Literal['automatic', 'manual']
AllowedFunding = Literal['credit', 'debit']


# This is separately defined from payment_intent_entity.PaymentMethodCard
# to set all items in 'card' as optional, to be used for endpoints
# that expect 'payment_method_options' in the payload
class PaymentMethodOptionsPayload(TypedDict):
    card: 'PaymentMethodCardPayload'


class PaymentMethodCardPayload(TypedDict):
    capture_type: NotRequired[CaptureType]
    allowed_bins: NotRequired[list[str]]
    allowed_funding: NotRequired[list[AllowedFunding]]
