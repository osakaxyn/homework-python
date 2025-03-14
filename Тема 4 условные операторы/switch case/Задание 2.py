"""
Дан номер месяца — целое число в диапазоне 1–12
(1 — январь, 2 — февраль и т. д.).
Определить количество дней в этом месяце для невисокосного года.
"""

def months():
        try:
            a = int(input('Введи номер месяца: '))
        except ValueError:
            print("нужно вводить ТОЛЬКО целые числа братишка..")
        match a:
            case 1:
                return ("Январь - 31 день")
            case 2:
                return ("Февраль - 28 дней")
            case 3:
                return ("Март - 31 день")
            case 4:
                return ("Апрель - 30 дней")
            case 5:
                return ("Май - 31 день")
            case 6:
                return ("Июнь - 30 день")
            case 7:
                return ("Июль - 31 день")
            case 8:
                return ("Август - 31 день")
            case 9:
                return ("Сентябрь - 30 день")
            case 10:
                return ("Октябрь - 31 день")
            case 11:
                return ("Ноябрь - 30 день")
            case 12:
                return ("Декабрь - 31 день")
            case other:
                return ("Дальше месяцев нет")

print(months())