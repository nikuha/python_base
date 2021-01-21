my_list = [5, 2, 2, 1]

print('Список ', my_list)

while True:
    element = input('Введите новый элемент списка: ')
    if element.isdigit() and int(element) >= 0:
        my_list.append(int(element))
        my_list.sort(reverse=True)
        print('Список ', my_list)
    else:
        print('Неверное значение натурального числа!')
