from payrex import BaseService
from payrex import MerchantEntity

class MerchantService(BaseService):
    PATH = 'merchants'

    def __init__(self, client):
        BaseService.__init__(self, client)

    def create(self, payload):
        return self.request(
            method='post',
            object=MerchantEntity,
            path=self.PATH,
            payload=payload
        )
