"""
Дана длина ребра куба a.
Найти объем куба V = a^3 и площадь его поверхности S = 6*a^2
"""

def void(a: int | float) -> int | float:
    V = a ** 3
    return V
print(f'Объем куба {void(96)}')

def archive(a: int | float) -> int | float:
    S = 6 * a ** 2
    return S
print(f'Площадь поверхности {archive(96)}')