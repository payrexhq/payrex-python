class Error:
    def __init__(self, error):
        self.code: str = error.get('code')
        self.detail: str = error.get('detail')
        self.parameter: str = error.get('parameter')
