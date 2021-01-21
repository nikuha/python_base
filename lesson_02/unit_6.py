params = ('название', 'цена', 'количество', 'ед.')

items = []

data = dict()
for param in params:
    data[param] = set()

i = 0
while i == 0 or input('введите Enter чтобы добавить новый товар или любой символ, чтобы завершить') == '':
    item_dict = dict()
    for param in params:
        item_dict[param] = input(f'{param}: ')
        data[param].add(item_dict[param])
    i += 1
    item = (i, item_dict)
    items.append(item)

print('Все товары:')
for item in items:
    print(item)

print('Аналитика данных:')
print(data)









