"""
Напишите функцию, которая находит факториалы чисел в заданном диапазоне,
границы диапазона передаются в качестве аргументов в функцию.
"""


def MDK():
    start = int(input("Цифру дай мне: "))
    stop = int(input("Цифру блядь в терминал мне: "))

    if start < 0 or stop > 100:
        raise ValueError("Диапазон должен быть от 0 до 100.")
    if start > stop:
        raise ValueError("Нижняя граница не может быть больше верхней.")
    pr = 1
    for i in range(start, stop):
        pr = pr * i
    print(pr)


MDK()