from functools import reduce


def fact(n):
    for el in range(1, n + 1):
        numbers = [x for x in range(1, el + 1)]
        yield reduce(lambda x, y: x * y, numbers)


n = 5
for el in fact(n):
    print(el)
