class String(str):
    def __add__(self, other):
        return String(str(self) + str(other))

    def __sub__(self, other):
        return String(str(self.replace(str(other), '', 1)))


a = String('New')
b = ['s', ' ', 23]
print(a + b)
print(type(a + b))

a = String(55678345672)
b = 7
print(a - b)
print(type(a - b))
