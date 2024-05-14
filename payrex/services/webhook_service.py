from payrex import BaseService
from payrex import WebhookEntity

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

    def list(self, payload):
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
            object=WebhookEntity,
            path=f'{self.PATH}/{id}',
            payload={}
        )
