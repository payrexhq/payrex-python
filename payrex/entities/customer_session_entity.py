class CustomerSessionEntity:
    def __init__(self, api_resource):
        data = api_resource.data

        self.id = data.get('id')
        self.customer_id = data.get('customer_id')
        self.client_secret = data.get('client_secret')
        self.livemode = data.get('livemode')
        self.components = data.get('components')
        self.expired = data.get('expired')
        self.expired_at = data.get('expired_at')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')
