import pytest
from library_app.book import Book
from library_app.config import BOOK_STATUS


def test_book_creation():
    book = Book(1, "Test Book", "Test Author", 2023)
    assert book.id == 1
    assert book.title == "Test Book"
    assert book.author == "Test Author"
    assert book.year == 2023
    assert book.status == BOOK_STATUS[1]


def test_book_str_representation():
    book = Book(1, "Test Book", "Test Author", 2023)
    assert str(book) == "[1] Test Book - Test Author (2023) - в наличии"


def test_change_book_status():
    book = Book(1, "Test Book", "Test Author", 2023)
    book.change_book_status(BOOK_STATUS[2])
    assert book.status == BOOK_STATUS[2]


def test_change_book_status_invalid():
    book = Book(1, "Test Book", "Test Author", 2023)
    with pytest.raises(ValueError):
        book.change_book_status("неверный статус")


def test_change_book_status_same_status():
    book = Book(1, "Test Book", "Test Author", 2023)
    with pytest.raises(ValueError):
        book.change_book_status(BOOK_STATUS[1])
