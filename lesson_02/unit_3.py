season_dict = {
    '1': 'зима', '2': 'зима', '12': 'зима',
    '3': 'весна', '4': 'весна', '5': 'весна',
    '6': 'лето', '7': 'лето', '8': 'лето',
    '9': 'осень', '10': 'осень', '11': 'осень',
}
season_list = ['зима', 'весна', 'лето', 'осень']

month = input('Введите номер месяца: ')
while (not month.isdigit()) or int(month) < 1 or int(month) > 12:
    month = input('Введите номер месяца от 1 до 12: ')

# вариант 1
print(season_dict[month])

# вариант 2
month_int = int(month) if int(month) < 12 else 0
print(season_list[month_int//3])
