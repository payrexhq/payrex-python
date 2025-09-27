import json
import hashlib
import hmac
from typing import TypedDict
from typing_extensions import NotRequired

from payrex import BaseService
from payrex import WebhookEntity
from payrex import DeletedEntity
from payrex import ValueUnexpectedException
from payrex import SignatureInvalidException
from payrex import ApiResource
from payrex import EventEntity
from payrex.entities.event_entity import EventType
from payrex.entities.listing_entity import ListingEntity

class WebhookService(BaseService):
    PATH = 'webhooks'

    def __init__(self, client):
        BaseService.__init__(self, client)

    def create(self, payload: 'CreateWebhookParams') -> WebhookEntity:
        return self.request(
            method='post',
            object=WebhookEntity,
            path=self.PATH,
            payload=payload
        )

    def update(self, id: str, payload: 'UpdateWebhookParams') -> WebhookEntity:
        return self.request(
            method='put',
            object=WebhookEntity,
            path=f'{self.PATH}/{id}',
            payload=payload
        )

    def list(self, payload: 'ListWebhooksParams' = {}) -> ListingEntity[WebhookEntity]:
        return self.request(
            method='get',
            object=WebhookEntity,
            path=self.PATH,
            payload=payload,
            is_list=True
        )

    def retrieve(self, id: str) -> WebhookEntity:
        return self.request(
            method='get',
            object=WebhookEntity,
            path=f'{self.PATH}/{id}',
            payload={}
        )

    def enable(self, id: str) -> WebhookEntity:
        return self.request(
            method='post',
            object=WebhookEntity,
            path=f'{self.PATH}/{id}/enable',
            payload={}
        )

    def disable(self, id: str) -> WebhookEntity:
        return self.request(
            method='post',
            object=WebhookEntity,
            path=f'{self.PATH}/{id}/disable',
            payload={}
        )

    def delete(self, id: str) -> DeletedEntity:
        return self.request(
            method='delete',
            object=DeletedEntity,
            path=f'{self.PATH}/{id}',
            payload={}
        )

    def parse_event(self, payload: str, signature_header: str, webhook_secret_key: str) -> EventEntity:
        if not isinstance(signature_header, str):
            raise ValueUnexpectedException('The signature must be a string.')

        signature_array = signature_header.split(',')

        if len(signature_array) < 3:
            raise ValueUnexpectedException(f'The format of signature {signature_header} is invalid.')

        timestamp = signature_array[0].split('=')[1]
        test_mode_signature = signature_array[1].split('=')[1]
        live_mode_signature = signature_array[2].split('=')[1]

        comparison_signature = live_mode_signature or test_mode_signature

        computed_hash = hmac.new(webhook_secret_key.encode(), f'{timestamp}.{payload}'.encode(), hashlib.sha256).hexdigest()

        if computed_hash != comparison_signature:
            raise SignatureInvalidException('The signature is invalid.')

        api_resource = ApiResource(json.loads(payload))

        return EventEntity(api_resource)


class CreateWebhookParams(TypedDict):
    url: str
    description: NotRequired[str]
    events: list[EventType]


class UpdateWebhookParams(TypedDict):
    url: NotRequired[str]
    description: NotRequired[str]
    events: NotRequired[list[EventType]]


class ListWebhooksParams(TypedDict):
    limit: NotRequired[int]
    before: NotRequired[str]
    after: NotRequired[str]
    url: NotRequired[str]
    description: NotRequired[str]
