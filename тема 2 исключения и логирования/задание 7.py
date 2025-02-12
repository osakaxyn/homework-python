"""
Написать программу для нахождения среднего арифметического списка чисел.
Если при вводе списка чисел была допущена ошибка
(например, был передан не список, а строка),
программа должна корректно обработать эту ошибку
и выдать соответствующее сообщение.
Информация об ошибках должна быть записана в лог.
"""



import logging

logging.basicConfig(
    filename='degeneration.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

def rarara(data):

    if not isinstance(data, list):
        raise TypeError("Ожидался список чисел")
    if not all(isinstance(item, (int, float)) for item in data):
        raise ValueError("Список должен содержать только числа")

    return sum(data) / len(data)

def main():
    """Главная функция программы."""
    # Пример ввода данных (можно заменить на пользовательский ввод)
    input_data = input("Введите список чисел, разделённых пробелами: ")

    try:
        # Преобразуем строку ввода в список чисел
        numbers = [float(x) for x in input_data.split()]

        # Вычисляем среднее арифметическое
        average = rarara(numbers)
        print(f"Среднее арифметическое: {average}")

    except (TypeError, ValueError) as e:
        logging.error(f"Ошибка: {e}")
        print("Произошла ошибка: проверьте введённые данные. Подробнее в логах.")

if __name__ == "__main__":
    main()
