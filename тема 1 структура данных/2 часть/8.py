"""
Дано двузначное число.
Вывести число, полученное при перестановке цифр исходного числа.
"""

def sos(a: int) -> int:
    F = a // 10
    U = a % 10
    R = (U * 10) + F
    return R

print(f'Перевернутое число {sos(65)}')