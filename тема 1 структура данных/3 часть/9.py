"""
Даны два целых числа: A, B. Проверить истинность высказывания:
«Хотя бы одно из чисел A и B нечетное».
"""

def defa(A: int, B: int) -> str:
    if A % 2 or B % 2:
        return f'Хотя бы одно из чисел {A} и {B} нечетное'
    else:
        return f'одно из чисел {A} и {B} четное'

print(defa(35 , 46))