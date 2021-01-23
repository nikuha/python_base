my_list = [
    {'name': 'Иванов', 'rating': 7},
    {'name': 'Петров', 'rating': 5},
    {'name': 'Сидоров', 'rating': 2},
]


def print_my_list(my_list):
    for item in my_list:
        print(f'{item["name"]}: {item["rating"]}')


print_my_list(my_list)

while True:
    name = input('Введите имя: ')
    rating = input('Введите рейтинг: ')
    if rating.isdigit() and int(rating) >= 0:
        my_list.append({'name': name, 'rating': int(rating)})
        my_list = sorted(my_list, key=lambda x: x['rating'], reverse=True)
        print_my_list(my_list)
    else:
        print('Неверное значение натурального числа!')
