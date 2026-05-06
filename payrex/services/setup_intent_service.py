from payrex import BaseService
from payrex import SetupIntentEntity

class SetupIntentService(BaseService):
    PATH = 'setup_intents'

    def __init__(self, client):
        BaseService.__init__(self, client)

    def cancel(self, id):
        return self.request(
            method='post',
            object=SetupIntentEntity,
            path=f'{self.PATH}/{id}/cancel'
        )

    def create(self, payload):
        return self.request(
            method='post',
            object=SetupIntentEntity,
            path=self.PATH,
            payload=payload
        )
    
    def retrieve(self, id):
        return self.request(
            method='get',
            object=SetupIntentEntity,
            path=f'{self.PATH}/{id}',
            payload={}
        )
