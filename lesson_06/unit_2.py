class Road:
    _length = 0
    _width = 0

    def __init__(self, length, width):
        self._width = width
        self._length = length

    def masse(self):
        return self._width * self._length * 25 * 5


my_road = Road(221, 3)
print(f'Масса асфальта: {my_road.masse()} т')
