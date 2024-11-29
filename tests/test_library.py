from library_app.library import Library
from library_app.book import Book
from library_app.config import BOOK_STATUS


def test_add_book(tmpdir):
    filename = tmpdir.join("test_library.json")
    library = Library()
    library.storage.filename = filename

    book = library.add_book("Test Book", "Test Author", 2023)
    assert book.title == "Test Book"
    assert book.author == "Test Author"
    assert book.year == 2023
    assert book.status == BOOK_STATUS[1]

    loaded_books = library.storage.load_books()
    assert len(loaded_books) == 1
    assert loaded_books[0]["title"] == "Test Book"


def test_remove_book(tmpdir):
    filename = tmpdir.join("test_library.json")
    library = Library()
    library.storage.filename = filename

    library.add_book("Test Book", "Test Author", 2023)
    library.remove_book(1)

    loaded_books = library.storage.load_books()
    assert len(loaded_books) == 0


def test_find_books(tmpdir):
    filename = tmpdir.join("test_library.json")
    library = Library()
    library.storage.filename = filename

    library.add_book("Test Book 1", "Test Author 1", 2023)
    library.add_book("Test Book 2", "Test Author 2", 2023)

    found_books = library.find_books("Test Book 1")
    assert len(found_books) == 1
    assert found_books[0].title == "Test Book 1"


def test_update_book_status(tmpdir):
    filename = tmpdir.join("test_library.json")
    library = Library()
    library.storage.filename = filename

    library.add_book("Test Book", "Test Author", 2023)
    library.update_book_status(1, BOOK_STATUS[2])

    loaded_books = library.storage.load_books()
    assert loaded_books[0]["status"] == BOOK_STATUS[2]
