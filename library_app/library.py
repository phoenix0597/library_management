from library_app.book import Book
from library_app.config import DATABASE_FILE_PATH
from library_app.storage import Storage


class Library:
    def __init__(self):
        self.books = []
        self.storage = Storage(DATABASE_FILE_PATH)
        # Загрузим книги из БД при инициализации библиотеки
        self.load_books()

    # Добавляем метод для загрузки книг из файла
    def load_books(self):
        books_data = self.storage.load_books()
        self.books = [
            Book(
                id=book_data["id"],
                title=book_data["title"],
                author=book_data["author"],
                year=book_data["year"],
                status=book_data["status"],
            )
            for book_data in books_data
        ]

    def add_book(self, title, author, year):
        id_ = max([book.id for book in self.books], default=0) + 1
        book = Book(id_, title, author, year)
        self.books.append(book)
        self.storage.save_books(self.books)
        return book

    def remove_book(self, id_):
        for book in self.books:
            if book.id == id_:
                self.books.remove(book)
                print("Книга удалена!")
                self.storage.save_books(self.books)
                return True
        raise ValueError("Книга с таким id не найдена!")

    def find_books(self, query: str):
        query = query.lower()
        return [
            book
            for book in self.books
            if query in book.title.lower()
            or query in book.author.lower()
            or query in str(book.year)
        ]

    def find_book_by_id(self, id_):
        for book in self.books:
            if book.id == id_:
                return book

    def display_books(self):
        for book in self.books:
            print(book)

    # для обновления статуса книги в хранилище
    def update_book_status(self, book_id, new_status):
        book = self.find_book_by_id(book_id)
        if book:
            book.change_book_status(new_status)
            self.storage.update_book(book_id, book.__dict__)
            return True
        return False
