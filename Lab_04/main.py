import sys
from pathlib import Path

# Додаємо папку, де лежить main.py, до шляхів пошуку модулів
sys.path.append(str(Path(__file__).parent.resolve()))

from domain.models import Author, Book, EBook, BookCatalog, LibraryRegistry
from domain.value_objects import PublicationInfo
from domain.repositories import GenericInMemoryRepository
from domain.services import BookSearchService, ConsoleBookExporter
from dto import BookPayload, book_from_payload

def main() -> None:
    print("=== СИСТЕМА ОБЛІКУ КНИГ (ВАРІАНТ 2) ===\n")

    repo = GenericInMemoryRepository[Book]()
    exporter = ConsoleBookExporter()
    service = BookSearchService(repository=repo, exporter=exporter)

    author1 = Author(id=1, name="Тарас Шевченко", country="Україна")
    pub1 = PublicationInfo(year=1840, pages=115, publisher="Друкарня П. А. Куліша")
    book1 = Book(book_id=1, title="Кобзар", author=author1, pub_info=pub1)

    author2 = Author(id=2, name="George Orwell", country="UK")
    pub2 = PublicationInfo(year=1949, pages=328, publisher="Secker & Warburg")
    ebook1 = EBook(
        book_id=2,
        title="1984",
        author=author2,
        pub_info=pub2,
        file_size_mb=1.5,
        download_url="https://library.org/files/1984.epub"
    )

    payload: BookPayload = {
        "id": 3,
        "title": "Майстер і Маргарита",
        "author_id": 3,
        "author_name": "Михайло Булгаков",
        "author_country": "Україна",
        "year": 1967,
        "pages": 480,
        "publisher": "Клуб Сімейного Дозвілля"
    }
    book3 = book_from_payload(payload)

    repo.add(book1)
    repo.add(ebook1)
    repo.add(book3)

    catalog = BookCatalog()
    catalog.add_book(book1)
    catalog.add_book(ebook1)
    catalog.add_book(book3)

    registry = LibraryRegistry(name="Центральна міська бібліотека", catalog=catalog)
    print(f"Зареєстровано у '{registry.name}': {len(registry.catalog)} книг(и).")
    print(f"Чи є книга з ID=2 у каталозі? {2 in registry.catalog}\n")

    print("--- Пошук за автором або назвою ---")
    search_results = service.search_by_title_or_author("Шевченко")
    for b in search_results:
        print(f" -> {b}")

    print("\n--- Фільтрація за роком видання (1949) ---")
    year_results = service.filter_by_year(1949)
    for b in year_results:
        print(f" -> {b}")

    print("\n--- Визначення найбільшої книги за кількістю сторінок ---")
    largest = service.get_largest_book()
    if largest:
        print(f"Найбільша книга: '{largest.title}' ({largest.pub_info.pages} сторінок)")

if __name__ == "__main__":
    main()