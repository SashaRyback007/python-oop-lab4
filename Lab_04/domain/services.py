from domain.models import Book
from domain.repositories import GenericInMemoryRepository
from domain.protocols import BookExporterProtocol

class ConsoleBookExporter:
    def export(self, data: str) -> None:
        print(f"[EXPORTER OUTPUT]: {data}")


class BookSearchService:
    def __init__(
        self,
        repository: GenericInMemoryRepository[Book],
        exporter: BookExporterProtocol
    ) -> None:
        self._repository = repository
        self._exporter = exporter

    def search_by_title_or_author(self, query: str) -> list[Book]:
        query_lower = query.lower()
        results = [
            book for book in self._repository.get_all()
            if query_lower in book.title.lower() or query_lower in book.author.name.lower()
        ]
        self._exporter.export(f"Знайдено {len(results)} книг за запитом '{query}'.")
        return results

    def filter_by_year(self, year: int) -> list[Book]:
        return [
            book for book in self._repository.get_all()
            if book.pub_info.year == year
        ]

    def get_largest_book(self) -> Book | None:
        books = self._repository.get_all()
        if not books:
            return None
        return max(books, key=lambda book: book.pub_info.pages)