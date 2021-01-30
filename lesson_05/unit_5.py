from random import randint

my_list = [randint(0, 100) for i in range(15)]
str_list = [str(x) for x in my_list]

with open('unit_5.txt', 'w') as f:
    f.write(' '.join(str_list))

print(f'Сумма: {sum(my_list)}')
