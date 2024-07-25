import json
import requests
import re

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

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        if method.lower() in ['post', 'put', 'delete']:
            data = re.sub(
                r'%5B[\d+]%5D', 
                '%5B%5D',
                urlencode(
                    self._http_build_query(params)
                )
            )
        else:
            data = None

        response = requests.request(method, url, auth=auth, headers=headers, data=data)

        if not response.content:
            raise Exception(response)

        if response.status_code < 200 or response.status_code >= 400:
            self._handle_error(response)

        return ApiResource(response.json())

    def _http_build_query(self, params, parent_key='', sep='&'):
        items = []

        for key, value in params.items():
            new_key = f"{parent_key}[{key}]" if parent_key else key
            if isinstance(value, dict):
                items.extend(self._http_build_query(value, new_key, sep=sep).items())
            elif isinstance(value, list):
                for i, v in enumerate(value):
                    if isinstance(v, dict):
                        items.extend(self._http_build_query(v, f"{new_key}[{i}]", sep=sep).items())
                    else:
                        items.append((f"{new_key}[{i}]", v))
            else:
                items.append((new_key, value))

        return dict(items)

    def _handle_error(self, response):
        try:
            json_response_body = response.json()
        except json.JSONDecodeError:
            raise Exception(response.content)

        if response.status_code == 400:
            raise RequestInvalidException(json_response_body)
        elif response.status_code == 401:
            raise AuthenticationInvalidException(json_response_body)
        elif response.status_code == 404:
            raise ResourceNotFoundException(json_response_body)
        else:
            raise BaseException(json_response_body)
