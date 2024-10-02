from payrex import BaseService
from payrex import BillingStatementEntity
from payrex import DeletedEntity

class BillingStatementService(BaseService):
    PATH = 'billing_statements'

    def __init__(self, client):
        BaseService.__init__(self, client)

    def create(self, payload):
        return self.request(
            method='post',
            object=BillingStatementEntity,
            path=self.PATH,
            payload=payload
        )

    def retrieve(self, id):
        return self.request(
            method='get',
            object=BillingStatementEntity,
            path=f'{self.PATH}/{id}',
            payload={}
        )

    def list(self, payload = {}):
        return self.request(
            method='get',
            object=BillingStatementEntity,
            path=self.PATH,
            payload=payload,
            is_list=True
        )

    def update(self, id, payload):
        return self.request(
            method='put',
            object=BillingStatementEntity,
            path=f'{self.PATH}/{id}',
            payload=payload
        )

    def delete(self, id):
        return self.request(
            method='delete',
            object=DeletedEntity,
            path=f'{self.PATH}/{id}',
            payload={}
        )

    def finalize(self, id):
        return self.request(
            method='post',
            object=BillingStatementEntity,
            path=f'{self.PATH}/{id}/finalize',
            payload={}
        )

    def send(self, id):
        return self.request(
            method='post',
            object=None,
            path=f'{self.PATH}/{id}/send',
            payload={}
        )

    def void(self, id):
        return self.request(
            method='post',
            object=BillingStatementEntity,
            path=f'{self.PATH}/{id}/void',
            payload={}
        )

    def mark_uncollectible(self, id):
        return self.request(
            method='post',
            object=BillingStatementEntity,
            path=f'{self.PATH}/{id}/mark_uncollectible',
            payload={}
        )