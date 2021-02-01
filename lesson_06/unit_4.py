class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def __init__(self, name, color, is_police=False):
        self.name = name
        self.color = color
        self.is_police = is_police

    def show_speed(self):
        print(f'Speed: {self.speed}')

    def go(self):
        self.speed += 20
        print('Go!')
        self.show_speed()

    def stop(self):
        self.speed = 0
        print(f'Stop!')

    def turn(self, direction):
        if self.speed == 0:
            print(f'{self.name} не может повернуть, надо сначала разогнаться!')
        elif direction == 'right':
            print(f'{self.name} повернула направо')
        elif direction == 'left':
            print(f'{self.name} повернула налево')
        else:
            print('Неверное направление')


class TownCar(Car):

    def show_speed(self):
        print(f'Speed: {self.speed}')
        if self.speed > 60:
            print('Превышение скорости!')


class WorkCar(Car):

    def show_speed(self):
        print(f'Speed: {self.speed}')
        if self.speed > 40:
            print('Превышение скорости!')


class PoliceCar(Car):
    is_police = True


class SportCar(Car):
    pass


car_1 = WorkCar('Camry', 'red')
car_1.go()
car_1.turn('right')
car_1.go()
car_1.go()
car_1.stop()

car_2 = PoliceCar('Toyota', 'black')
car_2.turn('left')
car_2.go()
car_2.turn('left')
car_2.go()
car_2.go()
car_2.go()
print(car_2.is_police)
