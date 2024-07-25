class WebhookEntity:
    def __init__(self, api_resource):
        data = api_resource.data

        self.id = data.get('id')
        self.secret_key = data.get('secret_key')
        self.status = data.get('status')
        self.description = data.get('description')
        self.livemode = data.get('livemode')
        self.url = data.get('url')
        self.events = data.get('events')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')
