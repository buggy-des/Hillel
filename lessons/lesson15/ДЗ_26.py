class FoundException(Exception):
    pass


class Calculator:
    def __init__(self, a: int | float, b: int | float):
        self.a = a
        self.b = b

    def plus(self):
        return self.a + self.b

    def minus(self):
        return self.a - self.b

    def divide(self):
        try:
            return self.a / self.b
        except ZeroDivisionError:
            return 0

    def multiply(self):
        return self.a * self.b

    def exponentiation(self):
        try:
            if self.b < 0:
                raise FoundException
        except FoundException:
            return self.a ** 0.5
        else:
            return self.a ** self.b

    def root(self):
        return self.a ** (1 / self.b)


example = Calculator(4, -2)

print(example.plus())
print(example.minus())
print(example.divide())
print(example.multiply())
print(example.exponentiation())
print(example.root())
