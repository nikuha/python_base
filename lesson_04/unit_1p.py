# вариант с argparse
# python3 lesson_04/unit_1p.py --hour_salary 100 --hours 200 --bonus 5000
from argparse import ArgumentParser
from unit_1f import salary

parser = ArgumentParser()

parser.add_argument('--hour_salary', type=float)
parser.add_argument('--hours', type=float)
parser.add_argument('--bonus', type=float, default=0)

args = parser.parse_args()

result = salary(args.hour_salary, args.hours, args.bonus)
if result:
    print(f'Зарплата: {result}')
