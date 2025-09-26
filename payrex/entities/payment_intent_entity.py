from typing import Literal, TypedDict
from typing_extensions import NotRequired

from payrex.type_defs import Currency, PaymentMethod


class PaymentIntentEntity:
    def __init__(self, api_resource):
        data = api_resource.data

        self.id: str = data.get('id')
        self.amount: int = data.get('amount')
        self.amount_received: int = data.get('amount_received')
        self.amount_capturable: int = data.get('amount_capturable')
        self.client_secret: str = data.get('client_secret')
        self.currency: Currency = data.get('currency')
        self.description: str | None = data.get('description')
        self.livemode: bool = data.get('livemode')
        self.metadata: dict[str, str] | None = data.get('metadata')
        self.latest_payment = data.get('latest_payment')
        self.payment_method_id: str | None = data.get('payment_method_id')
        self.payment_methods: list[PaymentMethod] = data.get('payment_methods')
        self.payment_method_options: PaymentMethodOptions | None = data.get('payment_method_options')
        self.statement_descriptor: str | None = data.get('statement_descriptor')
        self.status: Status = data.get('status')
        self.next_action: NextAction | None = data.get('next_action')
        self.return_url: str = data.get('return_url')
        self.capture_before_at = data.get('capture_before_at')
        self.created_at: int = data.get('created_at')
        self.updated_at: int = data.get('updated_at')


class PaymentMethodOptions(TypedDict):
    card: 'PaymentMethodCard'


class PaymentMethodCard(TypedDict):
    capture_type: NotRequired[Literal['automatic', 'manual']]
    allowed_bins: NotRequired[list[str]]
    allowed_funding: NotRequired[Literal['credit', 'debit']]


Status = Literal[
    'awaiting_payment_method', 'awaiting_next_action', 'processing', 'succeeded'
]


class NextAction(TypedDict):
    type: Literal['redirect']
    redirect_url: str
