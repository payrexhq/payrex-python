from typing import TypedDict
from typing_extensions import NotRequired
from payrex import BaseService
from payrex import PaymentEntity

class PaymentService(BaseService):
    PATH = 'payments'

    def __init__(self, client):
        BaseService.__init__(self, client)

    def retrieve(self, id: str) -> PaymentEntity:
        return self.request(
            method='get',
            object=PaymentEntity,
            path=f'{self.PATH}/{id}',
            payload={}
        )

    def update(self, id: str, payload: 'UpdatePaymentParams') -> PaymentEntity:
        return self.request(
            method='put',
            object=PaymentEntity,
            path=f'{self.PATH}/{id}',
            payload=payload
        )


class UpdatePaymentParams(TypedDict):
    description: NotRequired[str]
    metadata: NotRequired[dict[str, str]]
