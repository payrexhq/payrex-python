class CustomerEntity:
    def __init__(self, api_resource):
        data = api_resource.data

        self.id = data.get('id')
        self.billing_statement_prefix = data.get('billing_statement_prefix')
        self.currency = data.get('currency')
        self.email = data.get('email')
        self.livemode = data.get('livemode')
        self.name = data.get('name')
        self.metadata = data.get('metadata')
        self.next_billing_statement_sequence_number = data.get('next_billing_statement_sequence_number')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')