from payrex import BaseService
from payrex import PaymentIntentEntity

class PaymentIntentService(BaseService):
    PATH = 'payment_intents'

    def __init__(self, client):
        BaseService.__init__(self, client)

    def cancel(self, id):
        return self.request(
            method='post',
            object=PaymentIntentEntity,
            path=f'{self.PATH}/{id}/cancel'
        )

    def capture(self, id, payload):
        return self.request(
            method='post',
            object=PaymentIntentEntity,
            path=f'{self.PATH}/{id}/capture',
            payload=payload
        )

    def attach(self, id, payload):
        return self.request(
            method='post',
            object=PaymentIntentEntity,
            path=f'{self.PATH}/{id}/attach',
            payload=payload
        )

    def update(self, id, payload):
        return self.request(
            method='put',
            object=PaymentIntentEntity,
            path=f'{self.PATH}/{id}',
            payload=payload
        )
    
    def create(self, payload):
        return self.request(
            method='post',
            object=PaymentIntentEntity,
            path=self.PATH,
            payload=payload
        )
    
    def retrieve(self, id):
        return self.request(
            method='get',
            object=PaymentIntentEntity,
            path=f'{self.PATH}/{id}',
            payload={}
        )
