class DeletedEntity:
    def __init__(self, api_resource):
        data = api_resource.data

        self.id = data.get('id')
        self.deleted = data.get('deleted')