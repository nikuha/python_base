class Stationery:
    title = ''

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):

    def draw(self):
        print(f'Ручка {self.title} рисует линию')


class Pencil(Stationery):

    def draw(self):
        print(f'Карандаш {self.title} заштриховывает')


class Handle(Stationery):

    def draw(self):
        print(f'Маркер {self.title} обводит')


my_pen = Pen('Parker')
my_pencil = Pencil('Kohinoor')
my_handle = Handle('Touch')

my_pencil.draw()
my_handle.draw()
my_pen.draw()
