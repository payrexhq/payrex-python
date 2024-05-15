from payrex import Config
from payrex import ServiceFactory

class Client:
    def __init__(self, api_key):
        self.config = Config(api_key)
        self._initialize_services()

    def _initialize_services(self):
        for name in ServiceFactory.names():
            service = ServiceFactory.get(name)
            setattr(self, f'{name}s', service(self))
