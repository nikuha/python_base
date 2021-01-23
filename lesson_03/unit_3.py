# вариант с тремя аргументами
def my_func(arg_1, arg_2, arg_3):
    """ возвращает сумму наибольших двух элементов из 3-х """
    my_list = (arg_1, arg_2, arg_3)
    return sum(my_list) - min(my_list)


# вариант с любым кол-вом аргументов
def my_func_args(*args):
    """ возвращает сумму наибольших двух элементов из всего кортежа """
    my_list = list(args)
    my_list.sort(reverse=True)
    return my_list[0] + my_list[1]


print(my_func(3, 1, 4))
print(my_func_args(1, 5, 12, 14.5, 0, 3.5))
