class Car:
    FUEL_TYPES = ['petrol', 'diesel', 'electric', 'hybrid']
    COLORS = []
    NUMBER_OF_CARS = 0

    def __init__(self, model, year, color, fuel_type):
        self.model = model
        self.year = year
        self.color = color
        self.fuel_type = Car.is_valid_fuel_type(fuel_type)
        self.number = Car.NUMBER_OF_CARS + 1
        Car.NUMBER_OF_CARS += 1

        if color not in Car.COLORS:
            Car.COLORS.append(color)

    def __str__(self):
        return f"Model: {self.model}, year: {self.year}, color: {self.color}, fuel_type: {self.fuel_type}"

    @staticmethod
    def is_valid_fuel_type(fuel_type):
        return fuel_type if fuel_type in Car.FUEL_TYPES else Car.FUEL_TYPES[0]

    @property
    def numbers(self):
        return f"{self.number} from {Car.NUMBER_OF_CARS}"

    @classmethod
    def get_used_colors(cls):
        return len(cls.COLORS)

    @classmethod
    def get_number_of_cars(cls):
        return cls.NUMBER_OF_CARS


my_car = Car('Audi', 2003, 'yellow', 'diesel')
my_car_2 = Car('Zaz', 2020, 'black', 'hybrid')
my_car_3 = Car('BMW', 2023, 'black', 'electric')
my_car_4 = Car('Mercedes', 2012, 'green', 'k')

print('COLORS:', Car.get_used_colors())
print('NUMBER_OF_CARS:', Car.get_number_of_cars())

for item in (my_car, my_car_2, my_car_3, my_car_4):
    print('item:', item)
    print('numbers:', item.numbers)
