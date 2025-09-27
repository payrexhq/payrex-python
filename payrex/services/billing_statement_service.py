from typing import TypedDict
from typing_extensions import NotRequired
from payrex import BaseService
from payrex import BillingStatementEntity
from payrex import DeletedEntity
from payrex.entities.billing_statement_entity import PaymentSettings
from payrex.entities.listing_entity import ListingEntity
from payrex.common_types import Currency

class BillingStatementService(BaseService):
    PATH = 'billing_statements'

    def __init__(self, client):
        BaseService.__init__(self, client)

    def create(self, payload: 'CreateBillingStatementParams') -> BillingStatementEntity:
        return self.request(
            method='post',
            object=BillingStatementEntity,
            path=self.PATH,
            payload=payload
        )

    def retrieve(self, id: str) -> BillingStatementEntity:
        return self.request(
            method='get',
            object=BillingStatementEntity,
            path=f'{self.PATH}/{id}',
            payload={}
        )

    def list(self, payload: 'ListBillingStatementsParams' = {}) -> ListingEntity[BillingStatementEntity]:
        return self.request(
            method='get',
            object=BillingStatementEntity,
            path=self.PATH,
            payload=payload,
            is_list=True
        )

    def update(self, id: str, payload: 'UpdateBillingStatementParams') -> BillingStatementEntity:
        return self.request(
            method='put',
            object=BillingStatementEntity,
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

    def finalize(self, id: str) -> BillingStatementEntity:
        return self.request(
            method='post',
            object=BillingStatementEntity,
            path=f'{self.PATH}/{id}/finalize',
            payload={}
        )

    def send(self, id: str) -> None:
        return self.request(
            method='post',
            object=None,
            path=f'{self.PATH}/{id}/send',
            payload={}
        )

    def void(self, id: str) -> BillingStatementEntity:
        return self.request(
            method='post',
            object=BillingStatementEntity,
            path=f'{self.PATH}/{id}/void',
            payload={}
        )

    def mark_uncollectible(self, id: str):
        return self.request(
            method='post',
            object=BillingStatementEntity,
            path=f'{self.PATH}/{id}/mark_uncollectible',
            payload={}
        )


class CreateBillingStatementParams(TypedDict):
    customer_id: str
    currency: Currency
    description: NotRequired[str]
    billing_details_collection: NotRequired[str]
    payment_settings: PaymentSettings
    metadata: NotRequired[dict[str, str]]


class ListBillingStatementsParams(TypedDict):
    limit: NotRequired[int]
    before: NotRequired[str]
    after: NotRequired[str]


class UpdateBillingStatementParams(TypedDict):
    customer_id: NotRequired[str]
    description: NotRequired[str]
    billing_details_collection: NotRequired[str]
    payment_settings: NotRequired[PaymentSettings]
    metadata: NotRequired[dict[str, str]]
