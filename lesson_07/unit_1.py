class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = 0
        # проверяем, все ли строки одинаковой длины, если нет - выдаем ошибку
        for i, line in enumerate(self.data):
            if i > 0:
                assert self.cols == len(line), 'Неверный размер матрицы'
            self.cols = len(line)

    def __str__(self):
        matrix_lines = []
        for line in self.data:
            format_line = ['{:8d}'.format(el) for el in line]
            matrix_lines.append(''.join(format_line))
        return '\n'.join(matrix_lines)

    def __add__(self, other):
        new_matrix = []
        max_row_count = max(self.rows, other.rows)
        max_col_count = max(self.cols, other.cols)
        # проходим по максимальным размерам матриц
        for i in range(max_row_count):
            new_line = []
            for j in range(max_col_count):
                new_el = 0
                # прибавляем элементы, если они существуют
                if self.rows > i and self.cols > j:
                    new_el += self.data[i][j]
                if other.rows > i and other.cols > j:
                    new_el += other.data[i][j]
                new_line.append(new_el)
            new_matrix.append(new_line)

        return Matrix(new_matrix)


matrix_1 = Matrix([[23, 45, 67], [23, 11, 55], [22,78, 99]])
print(matrix_1, '\n')

matrix_2 = Matrix([[677, 14], [11, 0], [56, 987], [133, 500]])
print(matrix_2, '\n')

matrix_3 = matrix_1 + matrix_2
print(matrix_3)

