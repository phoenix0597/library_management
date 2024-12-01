from book import Book
from storage import Storage


class Library:
    """
    Класс, представляющий библиотеку книг.

    Attributes:
        books (list[Book]): Список книг в библиотеке.
        storage (Storage): Объект для работы с хранилищем данных.
    """

    def __init__(self, storage: Storage):
        """
        Инициализирует объект библиотеки.

        Загружает книги из хранилища при инициализации.
        """
        self.books: list[Book] = []
        self.storage: Storage = storage
        # Загрузим книги из БД при инициализации библиотеки
        self.load_books()

    # Добавляем метод для загрузки книг из файла
    def load_books(self) -> None:
        """
        Загружает книги из хранилища и сохраняет их в список books.
        """
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

    def add_book(self, title: str, author: str, year: int) -> Book:
        """
        Добавляет новую книгу в библиотеку.

        Аргументы:
            title (str): Название книги.
            author (str): Автор книги.
            year (int): Год издания книги.

        Returns:
            Book: Объект добавленной книги.
        """
        id_ = max([book.id for book in self.books], default=0) + 1
        book = Book(id_, title, author, year)
        self.books.append(book)
        self.storage.save_books(self.books)
        print(f"Книга добавлена: {book}")
        return book

    def remove_book(self, id_: int) -> bool:
        """
        Удаляет книгу из библиотеки по её идентификатору.

        Args:
            id_ (int): Идентификатор книги.

        Returns:
            bool: True, если книга была успешно удалена, иначе вызывает ValueError.

        Вызывает:
            ValueError: Если книга с указанным идентификатором не найдена.
        """
        for book in self.books:
            if book.id == id_:
                self.books.remove(book)
                print("Книга удалена!")
                self.storage.save_books(self.books)
                return True
        raise ValueError("Книга с таким id не найдена!")

    def find_books(self, query: str) -> list[Book]:
        """
        Ищет книги по заданному запросу.

        Args:
            query (str): Строка запроса для поиска по названию, автору или году издания.

        Returns:
            list[Book]: Список книг, соответствующих запросу.
        """
        query = query.lower()
        return [
            book
            for book in self.books
            if query in book.title.lower()
            or query in book.author.lower()
            or query in str(book.year)
        ]

    def find_book_by_id(self, id_: int) -> Book | None:
        """
        Ищет книгу по её идентификатору.

        Args:
            id_ (int): Идентификатор книги.

        Returns:
            Optional[Book]: Объект книги, если найден, иначе None.
        """
        for book in self.books:
            if book.id == id_:
                return book

    def display_books(self) -> None:
        """
        Выводит информацию о всех книгах в библиотеке.
        """
        for book in self.books:
            print(book)

    # для обновления статуса книги в хранилище
    def update_book_status(self, book_id: int, new_status: str) -> bool:
        """
        Обновляет статус книги в хранилище.

        Args:
            book_id (int): Идентификатор книги.
            new_status (str): Новый статус книги.

        Returns:
            bool: True, если статус был успешно обновлен, иначе False.
        """
        book = self.find_book_by_id(book_id)
        if book:
            book.change_book_status(new_status)
            self.storage.update_book(book_id, book.__dict__)
            return True
        return False
