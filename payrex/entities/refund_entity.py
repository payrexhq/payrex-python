class RefundEntity:
    def __init__(self, api_resource):
        data = api_resource.data

        self.id = data.get('id')
        self.amount = data.get('amount')
        self.currency = data.get('currency')
        self.livemode = data.get('livemode')
        self.status = data.get('status')
        self.description = data.get('description')
        self.reason = data.get('reason')
        self.remarks = data.get('remarks')
        self.payment_id = data.get('payment_id')
        self.metadata = data.get('metadata')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')
