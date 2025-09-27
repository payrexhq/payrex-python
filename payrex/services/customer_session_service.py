from typing import Final, TypedDict
from payrex import BaseService
from payrex import CustomerSessionEntity

class CustomerSessionService(BaseService):
    PATH: Final = 'customer_sessions'

    def __init__(self, client):
        BaseService.__init__(self, client)

    def create(self, payload: 'CreateCustomerSessionPayload') -> CustomerSessionEntity:
        return self.request(
            method='post',
            object=CustomerSessionEntity,
            path=self.PATH,
            payload=payload
        )

    def retrieve(self, id: str) -> CustomerSessionEntity:
        return self.request(
            method='get',
            object=CustomerSessionEntity,
            path=f'{self.PATH}/{id}',
            payload={}
        )


class CreateCustomerSessionPayload(TypedDict):
    # TODO: add additional keys when API reference for 'POST /customer_sessions'
    # is implemented
    customer_id: str
