from typing import Generic, TypeVar, Protocol

class HasId(Protocol):
    id: int

T = TypeVar("T", bound=HasId)

class GenericInMemoryRepository(Generic[T]):
    def __init__(self) -> None:
        self._storage: dict[int, T] = {}

    def add(self, item: T) -> None:
        self._storage[item.id] = item

    def get(self, item_id: int) -> T | None:
        return self._storage.get(item_id)

    def get_all(self) -> list[T]:
        return list(self._storage.values())

    def remove(self, item_id: int) -> bool:
        return self._storage.pop(item_id, None) is not None