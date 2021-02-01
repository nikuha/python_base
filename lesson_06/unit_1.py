from time import sleep


class TrafficLight:
    __color = 'red'

    def running(self, cycle_count=1):
        for i in range(0, cycle_count):
            for color, duration in [('red', 7), ('yellow', 2), ('green', 5)]:
                self.__color = color
                self.print_color()
                sleep(duration)

    def print_color(self):
        print(self.__color)


new_traffic = TrafficLight()
new_traffic.running(2)
