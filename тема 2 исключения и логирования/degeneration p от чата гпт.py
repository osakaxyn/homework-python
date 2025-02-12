"""
Написать программу для генерации случайных чисел в заданном диапазоне.
Если пользователь ввел недопустимые границы диапазона (например, меньше нуля),
программа должна вывести ошибку и попросить ввести диапазон заново.
Информация об ошибках должна быть записана в лог.
"""

import logging
import random

logging.basicConfig(
    filename='degeneration.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)


def generate_random_numbers():
    try:
        # Ввод диапазона
        start = float(input("Цифру дай мне (нижняя граница): "))
        stop = float(input("Цифру блядь в терминал мне (верхняя граница): "))

        # Проверка диапазона
        if start < 0 or stop > 100:
            raise ValueError("Диапазон должен быть от 0 до 100.")
        if start > stop:
            raise ValueError("Нижняя граница не может быть больше верхней.")

        # Генерация случайного числа
        random_number = random.uniform(start, stop)
        print(f"Случайное число в диапазоне от {start} до {stop}: {random_number:.2f}")



        logging.info(f"Случайное число сгенерировано: {random_number:.2f} (диапазон: {start} - {stop})")
    except ValueError as e:


        print(f"Ошибка: {e}")
        logging.error(f"Ошибка ввода диапазона: {e}")


# Запуск функции
generate_random_numbers()
