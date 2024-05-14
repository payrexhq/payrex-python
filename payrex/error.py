class Error:
    def __init__(self, error):
        self.code = error.get('code')
        self.detail = error.get('detail')
        self.parameter = error.get('parameter')
