from payrex import BaseService
from payrex import PaymentIntentEntity

class PaymentIntentService(BaseService):
    PATH = 'payment_intents'

    def __init__(self, client):
        BaseService.__init__(self, client)
    
    def retrieve(self, id):
        return self.request(
            method='get',
            object=PaymentIntentEntity,
            path=f'{self.PATH}/{id}',
            payload={}
        )
