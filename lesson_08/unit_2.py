class MyErrorException(Exception):
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f'Вычислить {self.number}/0 невозможно!'


try:
    x = float(input('Делимое: '))
    y = float(input('Делитель: '))
    if y == 0:
        raise MyErrorException(x)
except ValueError:
    print('Неверное число')
except MyErrorException as err:
    print(err)
else:
    print(f'Результат: {x/y}')
