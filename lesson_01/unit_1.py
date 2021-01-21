input_string = input('Введите целое число: ')
print(f'Тип переменной "input_string" - {type(input_string)}', f'значение: {input_string}', sep='\n')

true_integer = int(input_string)
print(f'Тип переменной "true_integer" - {type(true_integer)}', f'значение: {true_integer}', sep='\n')

input_float = float(input_string)
print(f'Тип переменной "input_float" - {type(input_float)}', f'значение: {input_float}', sep='\n')

input_bool = bool(input_string)
print(f'Тип переменной "input_bool" - {type(input_bool)}', f'значение: {input_bool}', sep='\n')
