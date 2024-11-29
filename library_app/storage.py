import json
import os


class Storage:
    def __init__(self, filename):
        self.filename = filename

    def save_books(self, books: list):
        data = [book.__dict__ for book in books]
        # print("Данные для сохранения:", data)
        with open(self.filename, "w", encoding="utf-8") as lib_file:
            json.dump(data, lib_file, indent=4, ensure_ascii=False)

    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                # print("Данные для загрузки:", data)
                return data
        return []

    # обновление данных конкретной книги в файле БД
    def update_book(self, book_id, updated_book_data):
        books_data = self.load_books()
        for i, book_data in enumerate(books_data):
            if book_data["id"] == book_id:
                books_data[i] = updated_book_data
                break
        with open(self.filename, "w", encoding="utf-8") as lib_file:
            json.dump(books_data, lib_file, indent=4, ensure_ascii=False)
