import math


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point(x={self.x}, y={self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def distance_from_origin(self):
        return math.hypot(self.x, self.y)


class Circle(Point):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def __str__(self):
        return f'Circle(x={self.x}, y={self.y}, radius={self.radius})'

    def __add__(self, other):
        return Circle(self.x + other.x, self.y + other.y, self.radius + other.radius)

    def __eq__(self, other):
        return self.radius == other.radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def __sub__(self, other):
        if (abs(self.radius) - abs(other.radius)) == 0:
            return Point(self.x - other.x, self.y - other.y)
        else:
            return Circle(self.x - other.x, self.y - other.y, abs(self.radius) - abs(other.radius))


a = Circle(0, 1, 3)
b = Circle(2, 2, 3)
c = b - a
print(c)
print(a - Circle(1, 3, 2))
