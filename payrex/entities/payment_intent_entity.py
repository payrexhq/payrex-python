class PaymentIntentEntity:
    def __init__(self, api_resource):
        data = api_resource.data

        self.id = data.get('id')
        self.amount = data.get('amount')
        self.amount_received = data.get('amount_received')
        self.amount_capturable = data.get('amount_capturable')
        self.client_secret = data.get('client_secret')
        self.currency = data.get('currency')
        self.description = data.get('description')
        self.livemode = data.get('livemode')
        self.metadata = data.get('metadata')
        self.latest_payment = data.get('latest_payment')
        self.payment_method_id = data.get('payment_method_id')
        self.payment_methods = data.get('payment_methods')
        self.payment_method_options = data.get('payment_method_options')
        self.status = data.get('status')
        self.next_action = data.get('next_action')
        self.return_url = data.get('return_url')
        self.capture_before_at = data.get('capture_before_at')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')
