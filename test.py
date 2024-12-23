from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, color, model):
        self.color = color
        self.model = model
        self.speed = 0

    def accelerate(self, amount):
        self.speed += amount
        print(f"The car accelerates by {
              amount} mph. Current speed: {self.speed} mph")

    def brake(self, amount):
        self.speed -= amount
        print(f"The car slows down by {
              amount} mph. Current speed: {self.speed} mph")

    @abstractmethod
    def start_engine(self):
        pass


class GasolineCar(Car):
    def start_engine(self):
        print("Starting gasoline engine...")


class ElectricCar(Car):
    def __init__(self, color, model, battery_capacity):
        super().__init__(color, model)
        self.battery_capacity = battery_capacity

    def start_engine(self):
        print("Starting electric motor...")

    def charge(self):
        print("The car is charging.")


# 객체 생성 및 사용
my_gasoline_car = GasolineCar("Red", "Sedan")
my_gasoline_car.start_engine()
my_gasoline_car.accelerate(30)
my_gasoline_car.brake(10)

my_electric_car = ElectricCar("Blue", "SUV", 100)
my_electric_car.start_engine()
my_electric_car.accelerate(40)
my_electric_car.charge()
