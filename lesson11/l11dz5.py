
class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.b > 0:
            return f'{self.a}+{self.b}i'
        elif self.b < 0:
            return f'{self.a}{self.b}i'

    def __add__(self, other):
        z = self.a + other.a
        x = self.b + other.b
        if self.b > 0:
            return f'{z}+{x}i'
        elif self.b < 0:
            return f'{z}{x}i'

    def __mul__(self, other):
        z = (self.a * other.a) - (self.b * other.b)
        x = (self.b * other.a) + (self.a * other.b)
        if self.b > 0:
            return f'{z}+{x}i'
        elif self.b < 0:
            return f'{z}{x}i'



c_1 = Complex(2, 7)
c_2 = Complex(3, 5)
print(c_1)
print(c_2)
print(c_1 + c_2)
print(c_1 * c_2)
