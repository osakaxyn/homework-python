"""
Напишите функцию,
которая выводит из заданного диапозона чисел выодит только четные числа.
Вам понадобиться цикл for, конструкция range.
"""

def chetko_chechetka():
    for i in range(4, 100):
        if i % 2 == 0:
            print(i)



chetko_chechetka()