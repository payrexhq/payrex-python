class DeletedEntity:
    def __init__(self, api_resource):
        data = api_resource.data

        self.id: str = data.get('id')
        self.deleted: bool = data.get('deleted')
