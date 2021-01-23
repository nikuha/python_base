def check_input_string(input_str):
    global my_list
    if input_str == '':
        return True
    for s in str_input.split(' '):
        try:
            f = float(s)
        except ValueError:
            return False
        my_list.append(f)
    return True


print('Введите строку чисел, разделенных пробелом.',
      'Чтобы продолжить вводить числа - Enter',
      'Чтобы завершить программу, нажмите любой символ.', sep='\n')
my_list = []
str_input = input(': ')
while check_input_string(str_input):
    print(f'Текущая сумма: {round(sum(my_list), 2)}')
    str_input = input(': ')
else:
    print(my_list)
    print(f'Общая сумма: {round(sum(my_list), 2)}')