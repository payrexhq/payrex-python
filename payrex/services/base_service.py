from payrex import HttpClient

class BaseService:
    def __init__(self, client):
        self.client = client

    def request(self, method, object, path, payload=None):
        http_client = HttpClient(
            api_key=self.client.config.api_key,
            base_url=self.client.config.api_base_url
        )

        api_resource = http_client.request(
            method=method,
            params=payload,
            path=path
        )

        return object(api_resource)
