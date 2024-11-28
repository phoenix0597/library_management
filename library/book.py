from library.config import BOOK_STATUS


class Book:
    def __init__(self, id: int, title: str, author: str, year: int, status: str):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __str__(self):
        return f"[{self.id}] {self.title} - {self.author} ({self.year}) - {self.status}"

    def change_status(self, new_status: str):
        if not new_status in list(BOOK_STATUS.values()):
            raise ValueError("Недопустимый статус книги!")

        if new_status != self.status:
            self.status = new_status
        else:
            raise ValueError(
                "Для изменения статуса книги введите статус, отличный от прежнего!"
            )
