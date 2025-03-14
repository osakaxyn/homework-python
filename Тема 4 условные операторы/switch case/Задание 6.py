""" Реализуйте программу калькулятор. На вход подается три значения: первое число,
Второе число и операция (*, /, + или -). На выходе должны получить число, после выполнения операции.
"""


def calculate(first_operand, second_operand, operation):
    match operation:
        case '*':
            return first_operand * second_operand
        case '/':
            if second_operand == 0:
                raise ZeroDivisionError("Деление на ноль не допустимо!")
            return first_operand / second_operand
        case '+':
            return first_operand + second_operand
        case '-':
            return first_operand - second_operand
        case _:
            raise ValueError("Некорректная операция! Пожалуйста, используйте одну из операций: *, /, +, -")

try:
    first_number = float(input('Введите первое число: '))
    second_number = float(input('Введите второе число: '))
    operation = input('Введите операцию (*, /, +, -): ')

    result = calculate(first_number, second_number, operation)
    print(f'Результат: {result}')
except ValueError as e:
    print(f'Ошибка: {e}')
except ZeroDivisionError as e:
    print(f'Ошибка: {e}')
