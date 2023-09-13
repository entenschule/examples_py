class BaseCar:
    def __init__(self, number_of_wheels=3):
        self.number_of_wheels = number_of_wheels

    def increment(self):
        self.number_of_wheels += 1


class Car(BaseCar):
    def __init__(self, number_of_spare_wheels=1):
        BaseCar.__init__(self, 4)
        self.number_of_spare_wheels = number_of_spare_wheels

    def increment(self):
        self.number_of_spare_wheels += 1


car = Car()
assert car.number_of_wheels == 4
assert car.number_of_spare_wheels == 1

car.increment()
assert car.number_of_wheels == 4
assert car.number_of_spare_wheels == 2
