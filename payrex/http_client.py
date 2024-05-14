import json
import requests

from urllib.parse import urlencode

from payrex import ApiResource
from payrex import BaseException
from payrex import RequestInvalidException
from payrex import AuthenticationInvalidException
from payrex import ResourceNotFoundException

class HttpClient:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url

    def request(self, method, params=None, path=None):
        url = f'{self.base_url}/{path}'

        auth = requests.auth.HTTPBasicAuth(self.api_key, '')

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        if method.lower() in ['post', 'put']:
            data = self._encode_params(params)
        else:
            data = None

        response = requests.request(method, url, auth=auth, headers=headers, data=data)

        if response.status_code != 200:
            self._handle_error(response)

        return ApiResource(response.json())

    def _handle_error(self, response):
        json_response_body = response.json()

        if response.status_code == 400:
            raise RequestInvalidException(json_response_body)
        elif response.status_code == 401:
            raise AuthenticationInvalidException(json_response_body)
        elif response.status_code == 404:
            raise ResourceNotFoundException(json_response_body)
        else:
            raise BaseException(json_response_body)

    def _encode_params(self, params):
        encoded_params = {}
        for key, value in params.items():
            if isinstance(value, list):
                for item in value:
                    encoded_params[f"{key}[]"] = item
            elif isinstance(value, dict):
                for k, v in value.items():
                    encoded_params[f"{key}[{k}]"] = v
            else:
                encoded_params[key] = value

        return urlencode(encoded_params)
