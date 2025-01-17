"""
Дан диаметр окружности d. Найти ее длину L = π·d, π = 3.14, d - диаметр.
"""

π = 3.14

def shar(d: int | float) -> int | float:
    L = π * d
    return L
print(f'Длина равна {shar(6.25)}')