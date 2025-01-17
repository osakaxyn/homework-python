"""
Даны два числа a и b. Найти их среднее арифметическое: (a + b)/2
"""

def arif(a: int | float , b: int | float) -> int | float:
    Sa = (a + b) / 2
    return Sa
print(f'Среднее арифметическое {arif(36 , 44.7)}')