# 20 до 240 найти числа, кратные 20 или 21.

print([x for x in range(20, 241) if (not x % 20) or (not x % 21)])
