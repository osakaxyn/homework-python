"""
Дан список [«Ростов», «+», «на», «-», «Дону»].
Исправьте плюс на дефис и выведите название города на экран
использовав доступ к элементам списка по индексам
"""

city = ["Ростов" , "+" , "на" , "-" , "Дону"]

def rostov(city):
    city[1] = "-"
    print(*city[0 : 5])

rostov(city)
