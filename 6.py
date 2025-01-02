"""
Даны длины ребер a, b, c прямоугольного параллелепипеда.
Найти его объем V = a·b·c и площадь поверхности S = 2 * (a * b + b * c + a * c)
"""

def bones(a: int | float, b: int | float, c: int | float) -> int | float:
    V = a * b * c
    return V
print(f'Объем {bones(43 , 50 ,36)}')

def meat(a: int | float, b: int | float, c: int | float) -> int | float:
    S = 2 * (a * b + b * c + a * c)
    return S
print(f'Площадь поверхности {meat(43 , 50 , 36)}')