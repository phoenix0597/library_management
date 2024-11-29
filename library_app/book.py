from library_app.config import BOOK_STATUS


class Book:
    def __init__(
        self, id: int, title: str, author: str, year: int, status: str = BOOK_STATUS[1]
    ):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __str__(self):
        return f"[{self.id}] {self.title} - {self.author} ({self.year}) - {self.status}"

    def change_book_status(self, new_status: str):
        status_list = list(BOOK_STATUS.values())
        if not new_status in status_list:
            raise ValueError(
                f"Статус книги должен быть одним из следующих: {", ".join(status_list)}"
            )

        if new_status != self.status:
            self.status = new_status
        else:
            raise ValueError(
                "Для изменения статуса книги введите статус, отличный от прежнего!"
            )

    def update_status_in_storage(self, storage):
        storage.save_books([self])
