"""
Написать программу для нахождения среднего арифметического списка чисел.
Если при вводе списка чисел была допущена ошибка
(например, был передан не список, а строка),
программа должна корректно обработать эту ошибку и выдать соответствующее сообщение.
Информация об ошибках должна быть записана в лог.
"""

import logging

a_logger = logging.getLogger("3")
a_logger.setLevel(logging.INFO)

a_handler = logging.FileHandler(f'{'3'}.log', mode='w')
a_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s, %(message)s")

a_handler.setFormatter(a_formatter)
a_logger.addHandler(a_handler)

a_logger.info(f'Логируется лог для {"3"} скрипта')

print("Введите 2 числа для того чтобы узнать их среднеарифметическое")
check_na_eblana = False

while check_na_eblana == False:

    try:
        a = int(input("a = "))
        b = int(input("b = "))
        c = (a + b) / 2

    except ValueError:
        a_logger.error("Указан неверный тип строки")

    else:
        a_logger.info(f'Среднее арифмитическое = {c}')
        check_na_eblana = True