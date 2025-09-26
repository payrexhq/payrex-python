from typing import Final


class Config:
    API_BASE_URL: Final[str] = 'https://api.payrexhq.com'

    def __init__(self, api_key: str):
        self.api_base_url: str = self.API_BASE_URL
        self.api_key: str = api_key
