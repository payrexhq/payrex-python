class PayoutEntity:
    def __init__(self, api_resource):
        data = api_resource.data

        self.id = data.get('id')
        self.amount = data.get('amount')
        self.destination = data.get('destination')
        self.livemode = data.get('livemode')
        self.net_amount = data.get('net_amount')
        self.status = data.get('status')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')
