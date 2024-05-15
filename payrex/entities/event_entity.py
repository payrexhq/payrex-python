class EventEntity:
    def __init__(self, api_resource):
        data = api_resource.data

        self.id = data.get('id')
        self.data = data.get('data')
        self.type = data.get('type')
        self.pending_webhooks = data.get('pending_webhooks')
        self.previous_attributes = data.get('previous_attributes')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')
