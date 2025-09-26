from typing import Generic, TypeVar

T = TypeVar("T")

class ListingEntity(Generic[T]):
    def __init__(self, data: list[T], has_more: bool):
        self.data: list[T] = data
        self.has_more: bool = has_more
