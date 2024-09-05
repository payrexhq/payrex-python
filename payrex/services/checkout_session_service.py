from payrex import BaseService
from payrex import CheckoutSessionEntity

class CheckoutSessionService(BaseService):
    PATH = 'checkout_sessions'

    def __init__(self, client):
        BaseService.__init__(self, client)

    def create(self, payload):
        return self.request(
            method='post',
            object=CheckoutSessionEntity,
            path=self.PATH,
            payload=payload
        )

    def list(self, payload = {}):
        return self.request(
            method='get',
            object=CheckoutSessionEntity,
            path=self.PATH,
            payload=payload,
            is_list=True
        )
    
    def retrieve(self, id):
        return self.request(
            method='get',
            object=CheckoutSessionEntity,
            path=f'{self.PATH}/{id}',
            payload={}
        )

    def expire(self, id):
        return self.request(
            method='post',
            object=CheckoutSessionEntity,
            path=f'{self.PATH}/{id}/expire',
            payload={}
        )
