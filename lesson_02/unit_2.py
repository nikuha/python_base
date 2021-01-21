my_list = []
n = ''

while (not n.isdigit()) or int(n) < 1:
    n = input('Введите кол-во элементов: ')

for i in range(0, int(n)):
    my_list.append(input(f'Введите {i+1}-й элемент: '))

print('Список: ', my_list)

for i in range(1, len(my_list), 2):
    my_list[i], my_list[i-1] = my_list[i-1], my_list[i]

print('Новый список: ', my_list)
