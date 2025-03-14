"""
Даны три целых числа.
Найти количество положительных чисел в исходном наборе.
"""

def otricalovo():
    try:
        a = int(input('Введи первое значение: '))
        b = int(input('Введи второе значение: '))
        c = int(input('Введи третье значение: '))
    except ValueError:
        print("нужно вводить ТОЛЬКО целые числа братишка..")
        return

    if a > 0 and b > 0 and c > 0:
        print("Количество положительных чисел: 3")
    elif (a > 0 and b > 0 and c <= 0) or (a > 0 and b <= 0 and c > 0) or (a <= 0 and b > 0 and c > 0):
        print("Количество положительных чисел: 2")
    elif (a > 0 and b <= 0 and c <= 0) or (a <= 0 and b > 0 and c <= 0) or (a <= 0 and b <= 0 and c > 0):
        print("Количество положительных чисел: 1")
    else:
        print("Ни одно из значений не является положительным :(")

otricalovo()