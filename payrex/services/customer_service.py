from payrex import BaseService
from payrex import CustomerEntity
from payrex import PaymentMethodEntity
from payrex import DeletedEntity

class CustomerService(BaseService):
    PATH = 'customers'

    def __init__(self, client):
        BaseService.__init__(self, client)

    def create(self, payload):
        return self.request(
            method='post',
            object=CustomerEntity,
            path=self.PATH,
            payload=payload
        )

    def retrieve(self, id):
        return self.request(
            method='get',
            object=CustomerEntity,
            path=f'{self.PATH}/{id}',
            payload={}
        )
    
    def list(self, payload = {}):
        return self.request(
            method='get',
            object=CustomerEntity,
            path=self.PATH,
            payload=payload,
            is_list=True
        )

    def list_payment_methods(self, id, payload = {}):
        return self.request(
            method='get',
            object=PaymentMethodEntity,
            path=f'{self.PATH}/{id}/payment_methods',
            payload=payload,
            is_list=True
        )

    def delete_payment_method(self, id, payload = {}):
        return self.request(
            method='delete',
            object=DeletedEntity,
            path=f'{self.PATH}/{id}/payment_methods/{payload["payment_method_id"]}',
            payload={}
        )

    def update(self, id, payload):
        return self.request(
            method='put',
            object=CustomerEntity,
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