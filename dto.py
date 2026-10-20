from typing import TypedDict
from domain.models import Book, Author
from domain.value_objects import PublicationInfo

class BookPayload(TypedDict):
    id: int
    title: str
    author_id: int
    author_name: str
    author_country: str
    year: int
    pages: int
    publisher: str

def book_from_payload(payload: BookPayload) -> Book:
    author = Author(
        id=payload["author_id"],
        name=payload["author_name"],
        country=payload["author_country"]
    )
    pub_info = PublicationInfo(
        year=payload["year"],
        pages=payload["pages"],
        publisher=payload["publisher"]
    )
    return Book(
        book_id=payload["id"],
        title=payload["title"],
        author=author,
        pub_info=pub_info
    )