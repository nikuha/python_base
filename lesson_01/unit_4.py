input_int = input('Введите целое положительное число: ')

# проверка введенных данных
while (not input_int.isdigit()) or int(input_int) <= 0:
    input_int = input('Неверный формат! Введите целое число больше 0: ')

max_number = 0
for number in input_int:
    if int(number) > max_number:
        max_number = int(number)
    if max_number == 9:
        break

print(f'Самая большая цифра в числе: {max_number}')
