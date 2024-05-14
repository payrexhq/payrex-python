class Config:
    API_BASE_URL = 'https://api.payrexhq.com'

    def __init__(self, api_key):
        self.api_base_url = self.API_BASE_URL
        self.api_key = api_key
