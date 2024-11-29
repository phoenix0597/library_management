import json
import os

from library_app.book import Book


class Storage:
    """
    Класс для работы с хранилищем книг в формате JSON.

    Attributes:
        filename (str): Имя файла, в котором хранятся данные о книгах.
    """

    def __init__(self, filename: str):
        """
        Инициализация объекта Storage.

        Args:
            filename (str): Имя файла для хранения данных о книгах.
        """
        self.filename = filename

    def save_books(self, books: list[Book]) -> None:
        """
        Сохраняет список книг в файл.

        Args:
            books (List[Any]): Список объектов книг, которые будут сохранены.

        Returns:
            None
        """
        data = [book.__dict__ for book in books]
        # print("Данные для сохранения:", data)
        with open(self.filename, "w", encoding="utf-8") as lib_file:
            json.dump(data, lib_file, indent=4, ensure_ascii=False)

    def load_books(self) -> list[Book]:
        """
        Загружает список книг из файла.

        Returns:
            List[Book]: Список словарей с данными о книгах.
        """

        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                # print("Данные для загрузки:", data)
                return data
        return []

    # обновление данных конкретной книги в файле БД
    def update_book(self, book_id: int, updated_book_data: dict[str, any]) -> None:
        """
        Обновляет данные конкретной книги в файле.

        Args:
            book_id (int): ID книги, которую нужно обновить.
            updated_book_data (dict[str, Any]): Новые данные для книги.

        Returns:
            None
        """
        books_data = self.load_books()
        for i, book_data in enumerate(books_data):
            if book_data["id"] == book_id:
                books_data[i] = updated_book_data
                break
        with open(self.filename, "w", encoding="utf-8") as lib_file:
            json.dump(books_data, lib_file, indent=4, ensure_ascii=False)
