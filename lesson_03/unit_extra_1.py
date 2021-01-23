goods = [
    {'name': 'Монитор', 'price': 150, 'amount': 5},
    {'name': 'Мышка', 'price': 5, 'amount': 6},
    {'name': 'Клавиатура', 'price': 20, 'amount': 2}
]

# вариант через лямбда функцию оказался довольно громоздким и плохо читаемым
euro_to_rub_lambda = lambda d: {x[0]: (x[1] * 90 if x[0] == 'price' else x[1]) for x in d.items()}
goods_rub = [euro_to_rub_lambda(item) for item in goods]
print(goods_rub)

# самый логичным кажется вариант не с лямбда, а с простой функцией
def euro_to_rub(item):
    item_new = item.copy()
    item_new['price'] *= 90
    return item_new

goods_rub = list(map(euro_to_rub, goods))
print(goods_rub)


