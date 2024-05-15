from payrex import BaseService
from payrex import PaymentMethodEntity

class PaymentMethodService(BaseService):
    PATH = 'payment_methods'

    def __init__(self, client):
        BaseService.__init__(self, client)

    def create(self, payload):
        return self.request(
            method='post',
            object=PaymentMethodEntity,
            path=self.PATH,
            payload=payload
        )
