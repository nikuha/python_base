from random import randint

random_list = [randint(0, 100) for i in range(10)]
result_list = []

for k, el in enumerate(random_list):
    if k > 0 and el > random_list[k - 1]:
        result_list.append(el)

print(random_list)
print(result_list)
