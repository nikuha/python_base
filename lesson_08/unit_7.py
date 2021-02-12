class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.b == 0:
            return str(self.a)
        op = '+' if self.b >= 0 else '-'
        return f'{self.a} {op} {abs(self.b)}i'

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        a = self.a * other.a - self.b * other.b
        b = self.a * other.b + self.b * other.a
        return ComplexNumber(a, b)


complex_1 = ComplexNumber(12, -3)
complex_2 = ComplexNumber(-1, 5)

print(complex_1)
print(complex_2)
print(complex_1 + complex_2)
print(complex_1 * complex_2)
