from numpy import mean

salaries = []

try:
    with open('unit_3.txt') as f:
        for line in f:
            name, salary = line.split(' ')
            salary = int(salary)
            salaries.append(salary)
            if salary < 20000:
                print(f'{name}: {salary}')
except FileNotFoundError:
    print('Не найден файл unit_3.txt')
except ValueError:
    print('Неверные данные')
finally:
    if len(salaries):
        print(f'Средняя зарплата: {mean(salaries)}')
