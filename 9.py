"""
Даны два неотрицательных числа a и b.
Найти их среднее геометрическое,
т. е. квадратный корень из их произведения: (a * b) * 1/2
"""

def sosik(a: int | float , b: int | float) -> int | float:
    Mg = (a * b) * 0.5
    return Mg
print(f'среднее геометрическое {sosik(66 , 75)}')