"""
Найти длину окружности L и площадь круга S заданного радиуса R
"""

π=3.14

def note(R: int | float) -> int | float:
    L = 2 * π * R
    return L
print(f'Длина окружности {note(5)}')

def death(R: int | float) -> int |float:
    S = π * R ** 2
    return S
print(F'Площадь круга {death(5)}')