from config import BOOK_STATUS, DATABASE_FILE_PATH
from library import Library
from library_app.storage import Storage
from utils import get_integer_input


def main() -> None:
    """
    Основная функция для управления библиотекой через консольное меню.
    """
    storage = Storage(DATABASE_FILE_PATH)
    library = Library(storage)
    while True:
        print("\nБиблиотека")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выход")

        choice: str = input("Выберите действие: ")

        if choice == "1":
            title: str = input("Введите название книги: ")
            author: str = input("Введите автора книги: ")
            year: int = get_integer_input("Введите год издания книги: ")
            library.add_book(title, author, year)
        elif choice == "2":
            # Добавляем цикл для повторного запроса корректного статуса
            while True:
                id_: int = int(input("Введите id книги: "))
                try:
                    library.remove_book(id_)
                    break  # Выходим из цикла, если статус изменен успешно
                except ValueError as e:
                    print(e)  # Выводим сообщение об ошибке и повторяем запрос
        elif choice == "3":
            query = input("Введите запрос: ")
            books = library.find_books(query)
            print("Найденные книги:")
            for book in books:
                print(book)
        elif choice == "4":
            books = library.books
            print("Все книги:")
            for book in books:
                print(book)
        elif choice == "5":
            id_ = get_integer_input("Введите id книги: ")
            # Добавляем цикл для повторного запроса корректного id
            while True:
                if id_ in [book.id for book in library.books]:
                    new_status = input(
                        f"Введите новый статус книги (один из {list(BOOK_STATUS.values())}): "
                    )
                    try:
                        library.update_book_status(id_, new_status)
                        print("Статус книги изменен!")
                        break  # Выходим из цикла, если статус изменен успешно
                    except ValueError as e:
                        print(e)  # Выводим сообщение об ошибке и повторяем запрос
                else:
                    print("Книга с таким id не найдена!")
        elif choice == "6":
            print("До свидания!")
            break
        else:
            print("Неверное действие!")


if __name__ == "__main__":
    main()
