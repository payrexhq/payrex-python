from typing import TypedDict
from typing_extensions import NotRequired
from payrex import BaseService
from payrex import PayoutTransactionEntity
from payrex.entities.listing_entity import ListingEntity

class PayoutService(BaseService):
    PATH = 'payouts'

    def __init__(self, client):
        BaseService.__init__(self, client)

    def list_transactions(
        self,
        id: str,
        payload: 'ListPayoutTransactionsPayload' = {}
    ) -> ListingEntity[PayoutTransactionEntity]:
        return self.request(
            method='get',
            object=PayoutTransactionEntity,
            path=f'{self.PATH}/{id}/transactions',
            payload=payload,
            is_list=True
        )


class ListPayoutTransactionsPayload(TypedDict):
    limit: NotRequired[int]
    before: NotRequired[str]
    after: NotRequired[str]
