"""
Напишите функцию,
которая выводит последовательность чисел Фибоначчи в заданном диапазоне,
границы диапазона и стартовая пара чисел
передаются в качестве аргументов в функцию.
"""


def pidarasisuki():
    a, b = first, second
    while a <= upper:
        if a >= lower:
            print(a, end=" ")
        a, b = b, a + b
    print()


try:
    lower = int(input("Введите нижнюю границу диапазона: "))
    upper = int(input("Введите верхнюю границу диапазона: "))
    first = int(input("Введите первое число последовательности: "))
    second = int(input("Введите второе число последовательности: "))

    print(f"Числа Фибоначчи в диапазоне от {lower} до {upper}:")
    pidarasisuki()
except ValueError:
    print("Ошибка ввода. Пожалуйста, вводите целые числа.")