from payrex import BaseService
from payrex import BillingStatementLineItemEntity
from payrex import DeletedEntity

class BillingStatementLineItemService(BaseService):
    PATH = 'billing_statement_line_items'

    def __init__(self, client):
        BaseService.__init__(self, client)

    def create(self, payload):
        return self.request(
            method='post',
            object=BillingStatementLineItemEntity,
            path=self.PATH,
            payload=payload
        )

    def retrieve(self, id):
        return self.request(
            method='get',
            object=BillingStatementLineItemEntity,
            path=f'{self.PATH}/{id}',
            payload={}
        )

    def update(self, id, payload):
        return self.request(
            method='put',
            object=BillingStatementLineItemEntity,
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