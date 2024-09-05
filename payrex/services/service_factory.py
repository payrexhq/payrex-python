import re

from payrex import BaseService
from payrex import CheckoutSessionService
from payrex import CustomerService
from payrex import BillingStatementService
from payrex import BillingStatementLineItemService
from payrex import PaymentIntentService
from payrex import RefundService
from payrex import WebhookService

class ServiceFactory:
    @staticmethod
    def get(name):
        service_name = ''.join(word.capitalize() for word in name.split('_'))
        service_class = globals().get(service_name + 'Service')

        if not isinstance(service_class, type):
            raise ValueError(f'Unknown service: {name}')

        return service_class

    @staticmethod
    def names():
        return [
            re.sub(r'(?<!^)(?=[A-Z])', '_', c.__name__.split('Service')[0]).lower()

            for c in BaseService.__subclasses__()
        ]
