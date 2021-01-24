# вариант с sys
# python3 lesson_04/unit_1s.py 100 50 300
from sys import argv
from unit_1f import salary

if len(argv) < 4:
    print('Недостаточно аргументов')
    quit()

script_name, hour_salary, hours, bonus = argv

result = salary(hour_salary, hours, bonus)
if result:
    print(f'Зарплата: {result}')
