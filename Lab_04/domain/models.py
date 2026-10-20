from dataclasses import dataclass
from domain.value_objects import PublicationInfo

@dataclass
class Author:
    id: int
    name: str
    country: str

    def __str__(self) -> str:
        return f"{self.name} ({self.country})"


class Book:
    def __init__(self, book_id: int, title: str, author: Author, pub_info: PublicationInfo) -> None:
        self.id = book_id
        self.title = title
        self.author = author          # Composition
        self.pub_info = pub_info      # Composition
        self._is_available: bool = True

    @property
    def is_available(self) -> bool:
        return self._is_available

    @is_available.setter
    def is_available(self, status: bool) -> None:
        self._is_available = status

    def __str__(self) -> str:
        return f"Книга '{self.title}' — {self.author} [{self.pub_info}]"

    def __repr__(self) -> str:
        return f"Book(id={self.id!r}, title={self.title!r}, pages={self.pub_info.pages!r})"


# Inheritance
class EBook(Book):
    def __init__(
        self,
        book_id: int,
        title: str,
        author: Author,
        pub_info: PublicationInfo,
        file_size_mb: float,
        download_url: str
    ) -> None:
        super().__init__(book_id, title, author, pub_info)
        self.file_size_mb = file_size_mb
        self.download_url = download_url

    def __str__(self) -> str:
        return f"Електронна {super().__str__()} | Розмір: {self.file_size_mb} MB"


class BookCatalog:
    def __init__(self) -> None:
        self._books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self._books.append(book)

    def __len__(self) -> int:
        return len(self._books)

    def __iter__(self):
        return iter(self._books)

    def __contains__(self, book_id: int) -> bool:
        return any(b.id == book_id for b in self._books)


@dataclass
class LibraryRegistry:
    name: str
    catalog: BookCatalog