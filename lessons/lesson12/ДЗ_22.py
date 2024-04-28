from ДЗ_21 import Auto
import time


class Truck(Auto):
    def __init__(self, brand, age, mark, max_load, color=None, weight=None):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        print('Attention')
        super().move()

    def load(self):
        time.sleep(1)
        print('Load')
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand, age, mark, max_speed, color=None, weight=None):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f'Max_speed is {self.max_speed}')


truck_1 = Truck('Scania', 5, 'R450', 40000, 'White', 18000)
truck_2 = Truck('Volvo', 3, 'FL12', 12000, 'Black', 4800)
car_1 = Car('Toyota', 1, 'Corolla', 220, 'Red', 1300)
car_2 = Car('Audi', 8, 'A6', 320)


def test_truck_1():
    truck_1.move()
    truck_1.load()
    truck_1.stop()
    print(f"Truck brand: {truck_1.brand}, max load: {truck_1.max_load}")
    print('-' * 100)


def test_truck_2():
    truck_2.move()
    truck_2.load()
    truck_2.stop()
    print(f"Truck brand: {truck_2.brand}, color: {truck_1.color}")
    print('-' * 100)


def test_car_1():
    car_1.move()
    car_1.stop()
    car_1.birthday()
    print(f"Car brand: {car_1.brand}, mark: {car_1.mark}")
    print('-' * 100)


def test_car_2():
    car_2.move()
    car_2.stop()
    car_2.birthday()
    print(f"Car brand: {car_2.brand}, age: {car_2.age}")
    print('-' * 100)


def test():
    test_truck_1()
    test_truck_2()
    test_car_1()
    test_car_2()


test()
