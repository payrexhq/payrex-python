from typing import Literal, TypedDict


class CustomerSessionEntity:
    def __init__(self, api_resource):
        data = api_resource.data

        self.id: str = data.get('id')
        self.customer_id: str = data.get('customer_id')
        self.client_secret: str = data.get('client_secret')
        self.livemode: bool = data.get('livemode')
        self.components: list[UiComponent] = data.get('components')
        self.expired: bool = data.get('expired')
        self.expired_at: int = data.get('expired_at')
        self.created_at: int = data.get('created_at')
        self.updated_at: int = data.get('updated_at')


class UiComponent(TypedDict):
    component: str
    feature: str
    value: Literal["enabled", "disabled"]
