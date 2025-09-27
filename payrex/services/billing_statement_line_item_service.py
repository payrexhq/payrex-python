from typing import TypedDict
from typing_extensions import NotRequired
from payrex import BaseService
from payrex import BillingStatementLineItemEntity
from payrex import DeletedEntity

class BillingStatementLineItemService(BaseService):
    PATH = 'billing_statement_line_items'

    def __init__(self, client):
        BaseService.__init__(self, client)

    def create(self, payload: 'CreateBillingStatementLineItemParams') -> BillingStatementLineItemEntity:
        return self.request(
            method='post',
            object=BillingStatementLineItemEntity,
            path=self.PATH,
            payload=payload
        )

    def retrieve(self, id: str) -> BillingStatementLineItemEntity:
        return self.request(
            method='get',
            object=BillingStatementLineItemEntity,
            path=f'{self.PATH}/{id}',
            payload={}
        )

    def update(self, id: str, payload: 'UpdateBillingStatementLineItemParams') -> BillingStatementLineItemEntity:
        return self.request(
            method='put',
            object=BillingStatementLineItemEntity,
            path=f'{self.PATH}/{id}',
            payload=payload
        )

    def delete(self, id: str) -> DeletedEntity:
        return self.request(
            method='delete',
            object=DeletedEntity,
            path=f'{self.PATH}/{id}',
            payload={}
        )


class CreateBillingStatementLineItemParams(TypedDict):
    billing_statement_id: str
    description: str
    unit_price: int
    quantity: int


class UpdateBillingStatementLineItemParams(TypedDict):
    description: NotRequired[str]
    unit_price: NotRequired[int]
    quantity: NotRequired[int]
