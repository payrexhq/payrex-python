from typing import Literal, Optional

from payrex.entities.event_entity import EventType


class WebhookEntity:
    def __init__(self, api_resource):
        data = api_resource.data

        self.id: str = data.get('id')
        self.secret_key: str = data.get('secret_key')
        self.status: Literal['enabled', 'disabled'] = data.get('status')
        self.description: Optional[str] = data.get('description')
        self.livemode: bool = data.get('livemode')
        self.url: str = data.get('url')
        self.events: list[EventType] = data.get('events')
        self.created_at: int = data.get('created_at')
        self.updated_at: int = data.get('updated_at')
