# Консольное приложение для управление книжной библиотекой

Это консольное приложение для управления книжной библиотекой. Оно позволяет добавлять, удалять, искать и изменять статус
книг. Данные хранятся в формате JSON.

## Оглавление

- [Функциональность](#функциональность)
- [Установка](#установка)
- [Использование](#использование)
- [Тестирование](#тестирование)
- [Структура проекта](#структура-проекта)
- [Лицензия](#лицензия)

## Функциональность

- **Добавление книги**: Добавляет новую книгу в библиотеку.
- **Удаление книги**: Удаляет книгу по её идентификатору.
- **Поиск книги**: Ищет книги по названию, автору или году издания (в т.ч. по частичному значению).
- **Просмотр всех книг**: Выводит список всех книг в библиотеке.
- **Изменение статуса книги**: Изменяет статус книги (например, "в наличии" или "выдана").

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone git remote add origin https://github.com/phoenix0597/library_management.git
   ```

2. Перейдите в директорию проекта:
   ```bash
   cd library_management
   ```

3. Установите необходимые зависимости (если есть):
   ```bash
   pip install -r requirements.txt
   ```

## Использование

Для запуска приложения выполните следующую команду:

```bash
python library_app/main.py
```

После запуска приложения вы увидите меню с доступными действиями. Выберите нужное действие, следуя инструкциям на
экране.

## Тестирование

Для запуска тестов используйте следующую команду:

```bash
pytest tests/
```

Тесты охватывают основные функции приложения, включая добавление, удаление, поиск и изменение статуса книг.

## Структура проекта

```
library_app/
│
├── book.py          # Класс Book для представления книги
├── config.py        # Конфигурационные параметры (например, статусы книг)
├── library.json     # Файл для хранения данных библиотеки
├── library.py       # Основной класс Library для управления книгами
├── main.py          # Точка входа в приложение
├── storage.py       # Класс Storage для работы с файловым хранилищем
└── utils.py         # Вспомогательные функции (например, для ввода данных)
│
tests/
│
├── test_library.py  # Тесты для класса Library
├── test_storage.py  # Тесты для класса Storage
└── test_book.py     # Тесты для класса Book
```

## Лицензия

Этот проект лицензирован под [MIT License](LICENSE).