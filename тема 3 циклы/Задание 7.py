"""
Создайте список с разными значениями,
пройдитесь по нему в цикле и выведите на экран.
(Сделайте то же самое со словарем и выведите ключ и значение)
"""

# это список
a = ["бойся", 228, "если пудришь носик", 3.14, "Elder RUS", True]

print("АУЕ")
for item in a:
    print(item)



# словарь
b = {
    "Фамилия Имя Отчество?": "Зубенко Михаил Петрович",
    "Кем являешься?": "Вор в законе",
    "Где именно?": "Шумиловский городок",
    "Кличка?": "Мафиозник"
}

print("Воровская Лапа:")
for key, value in b.items():
    print(f"{key}: {value}")