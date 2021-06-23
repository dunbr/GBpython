
class Div:
    def __init__(self, f, s):
        self.f = f
        self.s = s

    def simple_div(self):
        try:
            return self.f / self.s
        except ZeroDivisionError:
            return f'На ноль делить нельзя!'


c = Div(91, 0)
print(c.simple_div())
