class Auto:
    def __init__(self, brand, age, mark, color=None, weight=None):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self):
        print('Move')

    def birthday(self):
        self.age += 1

    def stop(self):
        print('Stop')
