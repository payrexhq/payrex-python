import json
import requests

from payrex import ApiResource

class HttpClient:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url

    def request(self, method, params=None, path=None):
        url = f'{self.base_url}/{path}'

        auth = requests.auth.HTTPBasicAuth(self.api_key, '')

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        data = json.dumps(params) if method.lower() in ['post', 'put'] else None

        response = requests.request(method, url, auth=auth, headers=headers, data=data)

        # TODO: Implement error handling

        return ApiResource(response.json())
