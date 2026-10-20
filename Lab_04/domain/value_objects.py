from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class PublicationInfo:
    year: int
    pages: int
    publisher: str

    def __post_init__(self) -> None:
        if self.year < 0:
            raise ValueError("Рік видання не може бути від'ємним.")
        if self.pages <= 0:
            raise ValueError("Кількість сторінок повинна бути більшою за 0.")

    def __str__(self) -> str:
        return f"{self.publisher}, {self.year} р. ({self.pages} стор.)"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, PublicationInfo):
            return NotImplemented
        return (
            self.year == other.year
            and self.pages == other.pages
            and self.publisher == other.publisher
        )