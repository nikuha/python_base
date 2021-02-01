class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {'wage': 0, 'bonus': 0}

    def __init__(self, **kwargs):
        for el in ['name', 'surname', 'position']:
            if el in kwargs:
                setattr(self, el, kwargs[el])


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        position_income = {
            'accountant': (50000, 20000),
            'programmer': (80000, 30000)
        }
        if self.position in position_income:
            self._income['wage'], self._income['bonus'] = position_income[self.position]
        else:
            self._income['wage'], self._income['bonus'] = 0, 0
        return self._income['wage'] + self._income['bonus']

    def get_full_info(self):
        return f'Имя: {self.get_full_name()}, Зарплата: {self.get_total_income()}'


worker_1 = Position(name='Иван', surname='Петров', position='accountant')
print(worker_1.get_full_info())

worker_2 = Position(name='Екатерина', position='programmer')
print(worker_2.get_full_info())
