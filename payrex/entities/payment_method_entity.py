class PaymentMethodEntity:
    def __init__(self, api_resource):
        data = api_resource.data

        self.id = data.get('id')
        self.resource = data.get('resource')
        self.type = data.get('type')
        self.billing_details = data.get('billing_details')
        self.livemode = data.get('livemode')
        self.metadata = data.get('metadata')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')
