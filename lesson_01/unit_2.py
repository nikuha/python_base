input_seconds = input('Введите время в секундах: ')

# проверка введенных данных
while (not input_seconds.isdigit()) or int(input_seconds) < 0:
    input_seconds = input('Неверный формат! Введите целое число не меньше 0: ')

seconds = int(input_seconds)

# количество целых часов
hours = seconds // 3600
# остаток от деления в секундах
seconds %= 3600

# количество целых минут
minutes = seconds // 60
# остаток от деления в секундах
seconds %= 60

print('Время {:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds))