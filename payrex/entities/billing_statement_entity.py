class BillingStatementEntity:
    def __init__(self, api_resource):
        data = api_resource.data

        self.id = data.get('id')
        self.customer_reference_id = data.get('customer_reference_id')
        self.client_secret = data.get('client_secret')
        self.status = data.get('status')
        self.currency = data.get('currency')
        self.line_items = data.get('line_items')
        self.livemode = data.get('livemode')
        self.url = data.get('url')
        self.payment_intent = data.get('payment_intent')
        self.metadata = data.get('metadata')
        self.success_url = data.get('success_url')
        self.cancel_url = data.get('cancel_url')
        self.payment_methods = data.get('payment_methods')
        self.description = data.get('description')
        self.submit_type = data.get('submit_type')
        self.expires_at = data.get('expires_at')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')