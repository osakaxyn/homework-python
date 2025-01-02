"""
Даны стороны прямоугольника a и b.
Найти его площадь S = a * b и периметр P = 2 * (a + b)
"""

def gelenjik(a: int | float, b: int | float) -> int | float:
    S = a * b
    return S
print(gelenjik(5.5 , 4.5))

def gelenjik2(a: int | float, b: int | float) -> int | float:
    P = 2 * (a + b)
    return P
print(gelenjik2( 5.5 ,  4.5))