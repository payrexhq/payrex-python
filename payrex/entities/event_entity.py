# pyright: reportExplicitAny=false
from typing import Any, Literal, TypedDict
from typing_extensions import NotRequired


class EventEntity:
    def __init__(self, api_resource):
        data = api_resource.data

        self.id: str = data.get('id')
        self.data: EventData = data.get('data')
        self.type: EventType = data.get('type')
        self.pending_webhooks: int = data.get('pending_webhooks')
        self.previous_attributes = data.get('previous_attributes')
        self.created_at: int = data.get('created_at')
        self.updated_at: int = data.get('updated_at')


class EventData(TypedDict):
    resource: dict[str, Any]
    previous_attributes: NotRequired[dict[str, Any]]


EventType = Literal[
    'billing_statement.created',
    'billing_statement.updated',
    'billing_statement.deleted',
    'billing_statement.finalized',
    'billing_statement.sent',
    'billing_statement.marked_uncollectible',
    'billing_statement.voided',
    'billing_statement.paid',
    'billing_statement.will_be_due',
    'billing_statement.overdue',
    'billing_statement_line_item.created',
    'billing_statement_line_item.updated',
    'billing_statement_line_item.deleted',
    'checkout_session.expired',
    'payment_intent.awaiting_capture',
    'payment_intent.succeeded',
    'payout.deposited',
    'refund.created',
    'refund.updated',
]
"""
The available types of events that can be subscribed to using webhooks.

API reference: https://docs.payrexhq.com/docs/api/events/event_types
"""
