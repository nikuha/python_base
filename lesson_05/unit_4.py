ru_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Five': 'Пять',
           'Six': 'Шесть', 'Seven': 'Семь', 'Eight': 'Восемь', 'Nine': 'Девять', 'Ten': 'Десять'}

new_list = []
try:
    with open('unit_4.txt') as f:
        for line in f:
            word, number = line.split(' — ')
            new_list.append(f'{ru_dict[word]} — {number}')
except FileNotFoundError:
    print('Не найден файл unit_4.txt')
except ValueError:
    print('Неверные данные')

if len(new_list) > 0:
    with open('unit_4n.txt', 'w') as f:
        f.writelines(new_list)
