def check_numbers(a, b):
    """ проверка данных """
    try:
        a = float(a)
        b = int(b)
    except ValueError:
        return False
    if a <= 0 or b >= 0:
        return False
    return True


def my_fuc_1(a, b):
    """ использование оператора ** """
    return 1 / (a ** abs(b))


def my_fuc_2(a, b):
    """ через цикл """
    pow_a = 1
    for i in range(0, abs(b)):
        pow_a *= a
    return 1 / pow_a


x = 8.5  # input('Действительное положительное число: ')
y = -3  # input('Целое отрицательное число: ')

if check_numbers(x, y):
    x = float(x)
    y = int(y)
    print(my_fuc_1(x, y))
    print(my_fuc_2(x, y))
    print(pow(x, y))  # через функцию pow для проверки
else:
    print('Ошибка данных')
