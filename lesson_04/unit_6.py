from itertools import count
from itertools import cycle


def list_with_count_fun(i_from, i_to):
    new_list = []
    for el in count(i_from):
        if el > i_to:
            break
        else:
            new_list.append(el)
    return new_list


def cycle_list(my_list, el_count):
    new_list = []
    for el in cycle(my_list):
        if len(new_list) > el_count:
            break
        else:
            new_list.append(el)
    return new_list


print(list_with_count_fun(13, 27))
print(cycle_list(['шла', 'Маша', 'по', 'шоссе'], 11))
