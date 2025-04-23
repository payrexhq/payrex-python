from payrex import BaseService
from payrex import RefundEntity

class RefundService(BaseService):
    PATH = 'refunds'

    def __init__(self, client):
        BaseService.__init__(self, client)

    def create(self, payload):
        return self.request(
            method='post',
            object=RefundEntity,
            path=self.PATH,
            payload=payload
        )

    def update(self, id, payload):
        return self.request(
            method='put',
            object=RefundEntity,
            path=f'{self.PATH}/{id}',
            payload=payload
        )
