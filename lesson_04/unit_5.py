# произведение всех четных чисел от 100 до 1000
from functools import reduce

my_list = [x for x in range(100, 1001) if (not x % 2)]
result = reduce(lambda x, y: x * y, my_list)

print(my_list)
print(result)
