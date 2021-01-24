def salary(salary, hours, bonus):
    try:
        salary = float(salary)
        hours = float(hours)
        bonus = float(bonus)
    except ValueError:
        print('Неверные аргументы')
        return None
    return salary * hours + bonus
