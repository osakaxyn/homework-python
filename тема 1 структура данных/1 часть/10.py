"""
Даны два ненулевых числа.
Найти сумму, разность, произведение и частное их квадратов.
"""

def final(a, b):
    S = a ** 2 + b ** 2
    return S
print(f'сумма {final(5 , 6)}')

def final1(a, b):
    R = a ** 2 - b ** 2
    return R
print(f'Разность {final1( 5 , 6)}')

def final2(a, b):
    U = a ** 2 * b ** 2
    return U
print(f'Частное {final2(5 , 6)}')

def final3(a, b):
    P = a ** 2 / b ** 2
    return P
print(f'Произведение {final3(5 , 6)}')