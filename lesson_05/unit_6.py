import re

my_dict = {}

with open('unit_6.txt') as f:
    for i, line in enumerate(f):
        try:
            subject, lessons = line.split(':')
            hours = 0
            for m in re.findall(r'\d+', lessons):
                hours += int(m)
            my_dict[subject] = hours
        except:
            print(f'Неверный формат строки {i}')

print(my_dict)
