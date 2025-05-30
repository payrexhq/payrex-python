from payrex import BaseService
from payrex import PaymentEntity

class PaymentService(BaseService):
    PATH = 'payments'

    def __init__(self, client):
        BaseService.__init__(self, client)

    def retrieve(self, id):
        return self.request(
            method='get',
            object=PaymentEntity,
            path=f'{self.PATH}/{id}',
            payload={}
        )

    def update(self, id, payload):
        return self.request(
            method='put',
            object=PaymentEntity,
            path=f'{self.PATH}/{id}',
            payload=payload
        )