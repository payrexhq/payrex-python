class BillingStatementLineItemEntity:
    def __init__(self, api_resource):
        data = api_resource.data

        self.id: str = data.get('id')
        self.unit_price: int = data.get('unit_price')
        self.quantity: int = data.get('quantity')
        self.billing_statement_id: str = data.get('billing_statement_id')
        self.description: str = data.get('description')
        self.livemode: bool = data.get('livemode')
        self.created_at: int = data.get('created_at')
        self.updated_at: int = data.get('updated_at')
