class SetupIntentEntity:
    def __init__(self, api_resource):
        data = api_resource.data

        self.id = data.get('id')
        self.livemode = data.get('livemode')
        self.client_secret = data.get('client_secret')
        self.next_action = data.get('next_action')
        self.payment_methods = data.get('payment_methods')
        self.return_url = data.get('return_url')
        self.status = data.get('status')
        self.usage = data.get('usage')
        self.customer = data.get('customer')
        self.description = data.get('description')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')