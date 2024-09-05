import json
import hashlib
import hmac

from payrex import BaseService
from payrex import WebhookEntity
from payrex import DeletedEntity
from payrex import ValueUnexpectedException
from payrex import SignatureInvalidException
from payrex import ApiResource
from payrex import EventEntity

class WebhookService(BaseService):
    PATH = 'webhooks'

    def __init__(self, client):
        BaseService.__init__(self, client)

    def create(self, payload):
        return self.request(
            method='post',
            object=WebhookEntity,
            path=self.PATH,
            payload=payload
        )

    def update(self, id, payload):
        return self.request(
            method='put',
            object=WebhookEntity,
            path=f'{self.PATH}/{id}',
            payload=payload
        )

    def list(self, payload = {}):
        return self.request(
            method='get',
            object=WebhookEntity,
            path=self.PATH,
            payload=payload,
            is_list=True
        )

    def retrieve(self, id):
        return self.request(
            method='get',
            object=WebhookEntity,
            path=f'{self.PATH}/{id}',
            payload={}
        )

    def enable(self, id):
        return self.request(
            method='post',
            object=WebhookEntity,
            path=f'{self.PATH}/{id}/enable',
            payload={}
        )

    def disable(self, id):
        return self.request(
            method='post',
            object=WebhookEntity,
            path=f'{self.PATH}/{id}/disable',
            payload={}
        )

    def delete(self, id):
        return self.request(
            method='delete',
            object=DeletedEntity,
            path=f'{self.PATH}/{id}',
            payload={}
        )

    def parse_event(self, payload, signature_header, webhook_secret_key):
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
