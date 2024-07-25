class MerchantEntity:
    def __init__(self, api_resource):
        data = api_resource.data

        self.id = data.get('id')
        self.connection_type = data.get('connection_type')
        self.livemode = data.get('livemode')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')
