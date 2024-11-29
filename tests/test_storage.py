from library_app.config import BOOK_STATUS
from library_app.storage import Storage
from library_app.book import Book


def test_save_and_load_books(tmpdir):
    filename = tmpdir.join("test_library.json")
    storage = Storage(filename)

    books = [
        Book(1, "Test Book 1", "Test Author 1", 2023),
        Book(2, "Test Book 2", "Test Author 2", 2023),
    ]

    storage.save_books(books)
    loaded_books = storage.load_books()

    assert len(loaded_books) == 2
    assert loaded_books[0]["title"] == "Test Book 1"
    assert loaded_books[1]["title"] == "Test Book 2"


def test_update_book(tmpdir):
    filename = tmpdir.join("test_library.json")
    storage = Storage(filename)

    books = [
        Book(1, "Test Book 1", "Test Author 1", 2023),
        Book(2, "Test Book 2", "Test Author 2", 2023),
    ]

    storage.save_books(books)

    updated_book = Book(1, "Updated Book 1", "Updated Author 1", 2023, BOOK_STATUS[2])
    storage.update_book(1, updated_book.__dict__)

    loaded_books = storage.load_books()
    assert loaded_books[0]["title"] == "Updated Book 1"
    assert loaded_books[0]["author"] == "Updated Author 1"
    assert loaded_books[0]["status"] == BOOK_STATUS[2]
