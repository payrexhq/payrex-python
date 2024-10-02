from payrex import HttpClient
from payrex import ListingEntity
from payrex import ApiResource

class BaseService:
    def __init__(self, client):
        self.client = client

    def request(self, method, object, path, payload=None, is_list=False):
        http_client = HttpClient(
            api_key=self.client.config.api_key,
            base_url=self.client.config.api_base_url
        )

        api_resource = http_client.request(
            method=method,
            params=payload,
            path=path
        )

        if is_list:
            data = [object(ApiResource(data)) for data in api_resource.data['data']]

            return ListingEntity(data, api_resource.data['has_more'])
        elif object is None:
            return None
        else:
            return object(api_resource)
