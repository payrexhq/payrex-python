class BillingStatementLineItemEntity:
    def __init__(self, api_resource):
        data = api_resource.data

        self.id = data.get('id')
        self.unit_price = data.get('unit_price')
        self.quantity = data.get('quantity')
        self.billing_statement_id = data.get('billing_statement_id')
        self.description = data.get('description')
        self.livemode = data.get('livemode')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')