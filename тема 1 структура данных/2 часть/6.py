"""
Дано двузначное число. Вывести вначале его левую цифру (десятки),
а затем — его правую цифру (единицы).
Для нахождения десятков использовать операцию деления нацело,
для нахождения единиц — операцию взятия остатка от деления.
"""

def buks(a: int) -> int:
    L = a // 10
    return int(L)

print(f'Десятки {buks(65)}')

def dollars(a: int) -> int:
    S = a % 10
    return S

print(f'единицы {dollars(65)}')