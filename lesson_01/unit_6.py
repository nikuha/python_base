from math import log


def float_request(request_string):
    response = ''
    while type(response) != float or response <= 0:
        response = input(request_string)
        try:
            response = float(response)
        except ValueError:
            continue
    return response


start_distance = float_request('Начальный пробег: ')
goal_distance = float_request('Конечная цель пробега: ')
achievement = 0.1

if start_distance > goal_distance:
    print('Некорректные данные')
    exit()

# вариант 1 если нужен вывод ежедневного прогресса
day = 1
current_distance = start_distance
while goal_distance > current_distance:
    current_distance += current_distance * achievement
    day += 1
    # вывод текущих достижений
    # print(current_distance)
else:
    print(f'Результат достигнут на {day}-й день')

# вариант 2 математический если нужен только результат
# k = achievement + 1 = 1.1
# start_distance * (k ** day) >= goal_distance
day = log(goal_distance/start_distance, achievement + 1) + 1
if int(day) != day:
    day = int(day + 1)
print(f'Результат достигнут на {day}-й день')

