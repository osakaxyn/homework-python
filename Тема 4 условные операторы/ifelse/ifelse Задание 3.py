"""
Даны два числа. Вывести вначале большее,
а затем меньшее из них.
"""





def otricalovo():
    try:
        a = int(input('Введи первое значение: '))
        b = int(input('Введи второе значение: '))
    except ValueError:
        print("нужно вводить ТОЛЬКО целые числа братишка..")
        return
    if a < b:
        print(b , a)
    else:
        a > b
        print(a , b)

otricalovo()