from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable

class BookFilterPolicy(ABC):
    @abstractmethod
    def is_satisfied(self, year: int, pages: int) -> bool:
        pass

@runtime_checkable
class BookExporterProtocol(Protocol):
    def export(self, data: str) -> None:
        ...