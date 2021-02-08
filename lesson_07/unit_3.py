class Cell:
    def __init__(self, cell_count):
        assert cell_count >= 0, 'Количество ячеек не должно быть отрицательным'
        self.cell_count = cell_count

    def __add__(self, other):
        return Cell(self.cell_count + other.cell_count)

    def __sub__(self, other):
        assert self.cell_count > other.cell_count, 'Некорректная операция вычитания'
        return Cell(self.cell_count - other.cell_count)

    def __mul__(self, other):
        return Cell(self.cell_count * other.cell_count)

    def __truediv__(self, other):
        assert other.cell_count > 0, 'Некорректная операция деления'
        return Cell(self.cell_count // other.cell_count)

    def __str__(self):
        return f'cells: {self.cell_count}\n{self.make_order()}'

    def make_order(self, in_line=10):
        int_part, rest_part = divmod(self.cell_count, in_line)
        order_list = ['*' * in_line for i in range(int_part)]
        if rest_part:
            order_list.append('*' * rest_part)
        return '\n'.join(order_list)


cell_1 = Cell(23)
print(cell_1)

cell_2 = Cell(12)
print(cell_2)

print(cell_1 + cell_2)

print(cell_1 - cell_2)
# выдаст ошибку
# print((cell_2 - cell_1))

cell_3 = cell_1 * cell_2
print(f'cell_3({cell_3.cell_count})')
print(cell_3.make_order(50))

print(cell_1 / cell_2)
