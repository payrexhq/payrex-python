from typing import Literal, TypedDict
from typing_extensions import NotRequired
from payrex import BaseService
from payrex import PaymentIntentEntity
from payrex.common_types import Currency, PaymentMethod, PaymentMethodOptionsPayload

class PaymentIntentService(BaseService):
    PATH = 'payment_intents'

    def __init__(self, client):
        BaseService.__init__(self, client)

    def cancel(self, id: str) -> PaymentIntentEntity:
        return self.request(
            method='post',
            object=PaymentIntentEntity,
            path=f'{self.PATH}/{id}/cancel'
        )

    def capture(self, id: str, payload: 'CapturePaymentIntentPayload') -> PaymentIntentEntity:
        return self.request(
            method='post',
            object=PaymentIntentEntity,
            path=f'{self.PATH}/{id}/capture',
            payload=payload
        )

    def create(self, payload: 'CreatePaymentIntentPayload') -> PaymentIntentEntity:
        return self.request(
            method='post',
            object=PaymentIntentEntity,
            path=self.PATH,
            payload=payload
        )

    def retrieve(self, id: str) -> PaymentIntentEntity:
        return self.request(
            method='get',
            object=PaymentIntentEntity,
            path=f'{self.PATH}/{id}',
            payload={}
        )


class CapturePaymentIntentPayload(TypedDict):
    amount: int


class CreatePaymentIntentPayload(TypedDict):
    amount: int
    payment_methods: list[PaymentMethod]
    currency: Currency
    description: NotRequired[str]
    payment_method_options: NotRequired[PaymentMethodOptionsPayload]
    statement_descriptor: NotRequired[str]
    metadata: NotRequired[dict[str, str]]
