import json

# вариант с текстовым файлом
my_dict = {}
sum_profit = 0
profit_count = 0

with open('unit_7.txt') as f:
    for i, line in enumerate(f):
        try:
            name, firma, proceed, expense = line.split(' ')
            profit = int(proceed) - int(expense)
            if profit > 0:
                sum_profit += profit
                profit_count += 1
            my_dict[name] = profit
        except:
            print(f'Неверный формат строки {i}')

average_profit = round(sum_profit/profit_count, 1) if profit_count > 0 else 0
res = [my_dict, {'average_profit': average_profit}]
print('DICT:', res, 'JSON:', json.dumps(res), sep='\n')


# вариант с csv файлом
import pandas

my_dict = {}
sum_profit = 0
profit_count = 0

data = pandas.read_csv("unit_7.csv", delimiter=';', names=['name', 'firma', 'proceed', 'expense'])
for i, row in data.iterrows():
    profit = int(row['proceed']) - int(row['expense'])
    if profit > 0:
        sum_profit += profit
        profit_count += 1
    my_dict[row['name']] = profit

average_profit = round(sum_profit/profit_count, 1) if profit_count > 0 else 0
res = [my_dict, {'average_profit': average_profit}]
print('DICT:', res, 'JSON:', json.dumps(res), sep='\n')
