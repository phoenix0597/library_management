def get_integer_input(prompt: str) -> int:
    """Функция для получения целочисленного ввода от пользователя."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: Введите корректное целое число.")
