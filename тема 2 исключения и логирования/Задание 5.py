"""
Написать программу на Python
для решения квадратного уравнения ax^2 + bx + c = 0.
Если дискриминант отрицателен, программа должна выдать ошибку
и предложить пользователю попробовать еще раз с другими коэффициентами.
"""
import logging
import math

logging.basicConfig(
    filename='operation.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'  # Указываем кодировку UTF-8
)

def higth_matematika():
    a = float(input("Цифру дай а: "))
    b = float(input("Цифру дай б: "))
    c = float(input("Цифру дай с: "))

    if a == 0:
        message = 'уравнения нэ будэт, а приняла ислам'
        logging.info(message)
        print(message)
        return

    D = b**2 - 4*a*c
    logging.info(f"Дискриминант D = {D}")

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        logging.info(f"Корни уравнения: x1 = {x1}, x2 = {x2}")
        return x1, x2

    elif D == 0:
        x = -b / (2 * a)
        logging.info(f"Один корень: x = {x}")
        return f"Один корень: x = {x}"
    else:
        message = "Бро, попробуй другие циферки написать"
        logging.info(message)
        return message

result = higth_matematika()
print(result)
