"""
Создайте словарь содержащий данные о человеке.
В качестве строковых ключей используйте его
имя, возраст, пол, рост, вес, размер ноги.
Выведите на экран все данные о человеке по ключам.
Добавьте в словарь ключ и значение размера ноги
Удалите из словаря возраст.
"""


def iam(name, age, sex, rost, ves, legs) -> dict:
    person = {
        'name': name,
        'age': age,
        'sex': sex,
        'rost': rost,
        'ves': ves,
        'legs': legs
    }
    return person

person = iam("Daneel", 25, "man", 180, 54.5, 41.5)

del person['age']

for key in person.keys():
    print(f"{key}: {person[key]}")


