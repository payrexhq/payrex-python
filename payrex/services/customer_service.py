from typing import TypedDict
from typing_extensions import NotRequired
from payrex import BaseService
from payrex import CustomerEntity
from payrex import DeletedEntity
from payrex.entities.listing_entity import ListingEntity
from payrex.type_defs import Currency

class CustomerService(BaseService):
    PATH = 'customers'

    def __init__(self, client):
        BaseService.__init__(self, client)

    def create(self, payload: 'CreateCustomerParams') -> CustomerEntity:
        return self.request(
            method='post',
            object=CustomerEntity,
            path=self.PATH,
            payload=payload
        )

    def retrieve(self, id: str) -> CustomerEntity:
        return self.request(
            method='get',
            object=CustomerEntity,
            path=f'{self.PATH}/{id}',
            payload={}
        )

    def list(self, payload: 'ListCustomersParams' = {}) -> ListingEntity[CustomerEntity]:
        return self.request(
            method='get',
            object=CustomerEntity,
            path=self.PATH,
            payload=payload,
            is_list=True
        )

    def update(self, id: str, payload: 'UpdateCustomerParams') -> CustomerEntity:
        return self.request(
            method='put',
            object=CustomerEntity,
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


class CreateCustomerParams(TypedDict):
    currency: Currency
    name: str
    email: str
    billing_statement_prefix: NotRequired[str]
    next_billing_statement_sequence_number: NotRequired[str]
    metadata: NotRequired[dict[str, str]]


class ListCustomersParams(TypedDict):
    limit: NotRequired[int]
    before: NotRequired[str]
    after: NotRequired[str]
    email: NotRequired[str]
    name: NotRequired[str]
    metadata: NotRequired[dict[str, str]]


class UpdateCustomerParams(TypedDict):
    currency: NotRequired[Currency]
    name: NotRequired[str]
    email: NotRequired[str]
    billing_statement_prefix: NotRequired[str]
    next_billing_statement_sequence_number: NotRequired[str]
    metadata: NotRequired[dict[str, str]]
