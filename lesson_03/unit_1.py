def division(arg_1, arg_2):
    try:
        arg_1 = float(arg_1)
        arg_2 = float(arg_2)
    except ValueError:
        return {'error': 'Неверный формат данных'}
    if arg_2 == 0:
        return {'error': 'Деление на ноль'}
    return {'result': arg_1/arg_2}


div = division(input('Делимое: '), input('Делитель: '))
if 'error' in div:
    print(f'Ошибка: {div["error"]}')
else:
    print(f'Результат: {div["result"]}')
