class PaymentEntity:
    def __init__(self, api_resource):
        data = api_resource.data

        self.id = data.get('id')
        self.amount = data.get('amount')
        self.amount_refunded = data.get('amount_refunded')
        self.billing = data.get('billing')
        self.currency = data.get('currency')
        self.description = data.get('description')
        self.fee = data.get('fee')
        self.livemode = data.get('livemode')
        self.metadata = data.get('metadata')
        self.net_amount = data.get('net_amount')
        self.payment_intent_id = data.get('payment_intent_id')
        self.status = data.get('status')
        self.customer = data.get('customer')
        self.payment_method = data.get('payment_method')
        self.refunded = data.get('refunded')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')
