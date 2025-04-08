from payrex import BaseService
from payrex import CustomerSessionEntity

class CustomerSessionService(BaseService):
    PATH = 'customer_sessions'

    def __init__(self, client):
        BaseService.__init__(self, client)

    def create(self, payload):
        return self.request(
            method='post',
            object=CustomerSessionEntity,
            path=self.PATH,
            payload=payload
        )

    def retrieve(self, id):
        return self.request(
            method='get',
            object=CustomerSessionEntity,
            path=f'{self.PATH}/{id}',
            payload={}
        )
