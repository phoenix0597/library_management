from library_app.config import BOOK_STATUS
from library_app.storage import Storage


class Book:
    """
    Класс, представляющий книгу в библиотеке.
    """

    def __init__(
        self, id: int, title: str, author: str, year: int, status: str = BOOK_STATUS[1]
    ):
        """
        Конструктор класса Book. Инициализирует объект книги с заданными параметрами.

        :param id: Уникальный идентификатор книги.
        :param title: Название книги.
        :param author: Автор книги.
        :param year: Год издания книги.
        :param status: Статус книги. По умолчанию используется второй статус из BOOK_STATUS.
        """
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта книги.

        :return: Строка, содержащая идентификатор, название, автора, год издания и статус книги.
        """
        return f"[{self.id}] {self.title} - {self.author} ({self.year}) - {self.status}"

    def change_book_status(self, new_status: str) -> None:
        """
        Изменяет статус книги на новый, если он допустим и отличается от текущего.

        :param new_status: Новый статус книги.
        :raises ValueError: Если новый статус недопустим или совпадает с текущим.
        """
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

    def update_status_in_storage(self, storage: Storage) -> None:
        """
        Обновляет статус книги в хранилище.

        :param storage: Объект хранилища, который содержит метод save_books.
        """
        storage.save_books([self])
