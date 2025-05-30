from payrex import BaseService
from payrex import PayoutTransactionEntity

class PayoutService(BaseService):
    PATH = 'payouts'

    def __init__(self, client):
        BaseService.__init__(self, client)

    def list_transactions(self, id, payload = {}):
        return self.request(
            method='get',
            object=PayoutTransactionEntity,
            path=f'{self.PATH}/{id}/transactions',
            payload=payload,
            is_list=True
        )