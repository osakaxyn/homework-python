




def translate_color(color):
    color_dict = {
        'red': 'красный',
        'green': 'зелёный',
        'blue': 'синий',
        'yellow': 'жёлтый',
        'black': 'чёрный',
        'white': 'белый',
        'orange': 'оранжевый',
        'purple': 'пурпурный',
        'pink': 'розовый',
        'brown': 'коричневый',
        'gray': 'серый'
    }


    if not color:
        raise ValueError('Ошибка: Введено пустое значение. Пожалуйста, введите название цвета.')


    result = color_dict.get(color.lower())

    if result is None:
        raise KeyError(f'Ошибка: Цвет "{color}" не найден в словаре.')

    return result


try:
    color = input('Введите цвет на английском: ')
    print(f'Перевод: {translate_color(color)}')
except ValueError as e:
    print(e)
except KeyError as e:
    print(e)
