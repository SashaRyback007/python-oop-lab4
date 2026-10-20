# Лабораторна робота №4: Професійне ООП та система типів Python

**Предметна область:** Варіант 2 — Система обліку книг (Book Management System)  
**Мова програмування:** Python 3.10+  
**Перевірка типів:** Mypy / Pyright  

---

## 📌 Опис проєкту

Проєкт реалізує типізовану об'єктно-орієнтовану модель предметної області для обліку книг у бібліотечній системі. У моделі розділено відповідальності між domain entities, value objects, abstractions (ABC, Protocol), repositories та application services із дотриманням принципів SOLID та сучасної системи type hints Python.

---

## 🏗 Структура проєкту

```text
лаб4/
├── book_system/
│   └── domain/
│       ├── __init__.py
│       ├── value_objects.py   # PublicationInfo (Immutable Frozen Dataclass)
│       ├── models.py          # Author, Book, EBook, BookCatalog, LibraryRegistry
│       ├── protocols.py       # ABC BookFilterPolicy та Protocol BookExporterProtocol
│       ├── repositories.py    # Generic Repository (Generic[T], TypeVar)
│       └── services.py        # BookSearchService (Application Layer)
├── dto.py                     # BookPayload (TypedDict) та конвертер
├── main.py                    # Демонстраційний сценарій
└── README.md                  # Документація проєкту

Реалізовані поняття та концепції ООП
Domain Entities: Author, Book, EBook, BookCatalog, LibraryRegistry.

Dataclasses & Frozen Value Objects:

@dataclass для Author, LibraryRegistry.

@dataclass(frozen=True, slots=True) для PublicationInfo з перевіркою коректності даних у __post_init__.

Properties: Перевірка та доступ до стану стану книги через @property (is_available).

Inheritance (Наслідування): EBook успадковує Book та розширює його додатковими атрибутами (file_size_mb, download_url).

Composition (Композиція):

Book містить об'єкти Author та PublicationInfo.

BookCatalog та LibraryRegistry агрегують колекції книг.

Abstract Base Class (ABC): BookFilterPolicy визначає інтерфейс для фільтрації.

Protocol (Structural Typing): BookExporterProtocol описує контракт експортера, ConsoleBookExporter відповідає йому без явного успадкування.

Dunder-методи:

__str__ та __repr__ для текстового представлення.

__len__, __iter__, __contains__ у BookCatalog для інтеграції з кошиком/каталогом.

__eq__ у PublicationInfo.

Generic Classes & TypeVar: GenericInMemoryRepository[T] із TypeVar("T", bound=HasId) забезпечує типізований CRUD-репозиторій.

TypedDict & DTO: BookPayload реалізує чітку структуру для зовнішніх JSON/API-даних.

Dependency Injection & SOLID:

SRP: Розділення бізнес-логіки (services.py), збереження даних (repositories.py) та опису моделей (models.py).

OCP: Способи експорту розширюються через реалізацію BookExporterProtocol.

DIP: Сервіси залежать від абстракцій/протоколів, а не від конкретних реалізацій.

🚀 Запуск проєкту
1. Запуск головного сценарію
У терміналі виконайте команду:

Bash
python main.py
Або запустити як модуль:

Bash
python -m main
🧪 Статична перевірка типів (Mypy)
Для перевірки типу коду встановіть та запустіть mypy:

Bash
pip install mypy
mypy book_system dto.py main.py
Очікуваний результат:

Plaintext
Success: no issues found in source files

Створивши цей файл у проєкті, ви повністю закриєте вимогу до структури та опису лабораторної роботи[cite: 1]