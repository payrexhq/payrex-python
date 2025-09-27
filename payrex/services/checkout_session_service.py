from typing import Final, TypedDict
from typing_extensions import NotRequired
from payrex import BaseService
from payrex import CheckoutSessionEntity
from payrex.entities.listing_entity import ListingEntity
from payrex.common_types import Currency, PaymentMethod, PaymentMethodOptionsPayload

class CheckoutSessionService(BaseService):
    PATH: Final = 'checkout_sessions'

    def __init__(self, client):
        BaseService.__init__(self, client)

    def create(self, payload: 'CreateCheckoutSessionPayload') -> CheckoutSessionEntity:
        return self.request(
            method='post',
            object=CheckoutSessionEntity,
            path=self.PATH,
            payload=payload
        )

    def list(self, payload: 'ListCheckoutSessionsPayload' = {}) -> ListingEntity[CheckoutSessionEntity]:
        return self.request(
            method='get',
            object=CheckoutSessionEntity,
            path=self.PATH,
            payload=payload,
            is_list=True
        )

    def retrieve(self, id: str) -> CheckoutSessionEntity:
        return self.request(
            method='get',
            object=CheckoutSessionEntity,
            path=f'{self.PATH}/{id}',
            payload={}
        )

    def expire(self, id: str) -> CheckoutSessionEntity:
        return self.request(
            method='post',
            object=CheckoutSessionEntity,
            path=f'{self.PATH}/{id}/expire',
            payload={}
        )


class CreateCheckoutSessionPayload(TypedDict):
    customer_reference_id: NotRequired[str]
    currency: Currency
    line_items: 'list[NewLineItemPayload]'
    metadata: NotRequired[dict[str, str]]
    success_url: str
    cancel_url: str
    expires_at: NotRequired[int]
    payment_methods: list[PaymentMethod]
    billing_details_collection: NotRequired[str]
    description: NotRequired[str]
    submit_type: NotRequired[str]
    payment_method_options: NotRequired[PaymentMethodOptionsPayload]



class NewLineItemPayload(TypedDict):
    name: str
    amount: int
    quantity: int
    description: NotRequired[str]
    image: NotRequired[str]


class ListCheckoutSessionsPayload(TypedDict):
    # TODO: add parameters when API reference for 'GET /checkout_sessions'
    # is implemented
    pass
