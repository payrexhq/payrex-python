class PayoutTransactionEntity:
    def __init__(self, api_resource):
        data = api_resource.data

        self.id = data.get('id')
        self.amount = data.get('amount')
        self.net_amount = data.get('net_amount')
        self.transaction_type = data.get('transaction_type')
        self.transaction_id = data.get('transaction_id')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')
