"""
Используя операции индексирования и среза выведите на экран
первый и третий элементы списка [1, 2, 3, 4, 5],
а также срез списка из первых трех элементов.
"""

numbers = [1 , 2 , 3 , 4 , 5]


def fuckingcuming(numbers):
    print(numbers[0], numbers[2])

    print(*numbers[0 : 3])

fuckingcuming(numbers)