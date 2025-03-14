"""
Даны три числа. Найти наименьшее из них.
"""
from selectors import SelectSelector


def otricalovo():
    try:
        a = int(input('Введи первое значение: '))
        b = int(input('Введи второе значение: '))
        c = int(input('Введи третье значение: '))
    except ValueError:
        print("нужно вводить ТОЛЬКО целые числа братишка..")
        return
    if (a < b and b < c) or (a < c and c < b):
        print(a)

    elif (b < c and c < a) or (b < a and a < c):
        print(b)

    else:
        (c < a and a < b) or (c < b and b < a)
        print(c)

otricalovo()