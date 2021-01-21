input_int = input('Введите целое число: ')

# проверка введенных данных
while (not input_int.isdigit()) or int(input_int) < 0:
    input_int = input('Неверный формат! Введите целое число не меньше 0: ')

result = int(input_int) + int(input_int * 2) + int(input_int * 3)
print(f'Сумма: {result}')
