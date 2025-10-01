# pyright: reportUninitializedInstanceVariable=false
from payrex import Config
from payrex import ServiceFactory
from payrex.services.billing_statement_line_item_service import BillingStatementLineItemService
from payrex.services.billing_statement_service import BillingStatementService
from payrex.services.checkout_session_service import CheckoutSessionService
from payrex.services.customer_service import CustomerService
from payrex.services.customer_session_service import CustomerSessionService
from payrex.services.payment_intent_service import PaymentIntentService
from payrex.services.payment_service import PaymentService
from payrex.services.payout_service import PayoutService
from payrex.services.refund_service import RefundService
from payrex.services.webhook_service import WebhookService

class Client:
    # When you create a new Service class, make sure to put the corresponding
    # type hint here
    billing_statement_line_items: BillingStatementLineItemService
    billing_statements: BillingStatementService
    checkout_sessions: CheckoutSessionService
    customer_sessions: CustomerSessionService
    customers: CustomerService
    payment_intents: PaymentIntentService
    payments: PaymentService
    payouts: PayoutService
    refunds: RefundService
    webhooks: WebhookService

    def __init__(self, api_key: str):
        self.config: Config = Config(api_key)
        self._initialize_services()

    def _initialize_services(self):
        for name in ServiceFactory.names():
            service = ServiceFactory.get(name)
            setattr(self, f'{name}s', service(self))
