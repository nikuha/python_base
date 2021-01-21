string = input('Введите строку: ')

for word in string.split(' '):
    print('{:.10}'.format(word))
