from payrex import Error

class BaseException(Exception):
    def __init__(self, response):
        self.errors: list[Error] = [Error(error) for error in response.get('errors', [])]
