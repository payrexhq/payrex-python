from typing import TypedDict
from typing_extensions import NotRequired
from payrex import BaseService
from payrex import RefundEntity
from payrex.entities.refund_entity import RefundReason
from payrex.common_types import Currency

class RefundService(BaseService):
    PATH = 'refunds'

    def __init__(self, client):
        BaseService.__init__(self, client)

    def create(self, payload: 'CreateRefundParams') -> RefundEntity:
        return self.request(
            method='post',
            object=RefundEntity,
            path=self.PATH,
            payload=payload
        )

    def update(self, id: str, payload: 'UpdateRefundParams') -> RefundEntity:
        return self.request(
            method='put',
            object=RefundEntity,
            path=f'{self.PATH}/{id}',
            payload=payload
        )


class CreateRefundParams(TypedDict):
    amount: int
    currency: Currency
    description: NotRequired[str]
    payment_id: str
    remarks: NotRequired[str]
    reason: RefundReason
    metadata: NotRequired[dict[str, str]]


class UpdateRefundParams(TypedDict):
    metadata: NotRequired[dict[str, str]]
