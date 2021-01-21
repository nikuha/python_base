proceeds = ''
while type(proceeds) != float or proceeds < 0:
    proceeds = input('Введите размер выручки: ')
    try:
        proceeds = float(proceeds)
    except ValueError:
        continue

expenses = ''
while type(expenses) != float or expenses < 0:
    expenses = input('Введите размер издержек: ')
    try:
        expenses = float(expenses)
    except ValueError:
        continue

if proceeds == expenses:
    print('Рентабельность 0')
elif proceeds < expenses:
    print(f'Убыток: {expenses - proceeds}')
else:
    employees = input('Введите количество сотрудников: ')
    while (not employees.isdigit()) or int(employees) < 1:
        employees = input('Введите целое число больше 0: ')

    profit = proceeds - expenses
    print(f'Ваша прибыль: {profit}')

    employees_profit = round(profit/int(employees), 1)
    print(f'В расчете на сотрудника: {employees_profit}')

    profitability = round(profit/proceeds, 1) * 100
    print(f'Рентабельность: {profitability}%')
