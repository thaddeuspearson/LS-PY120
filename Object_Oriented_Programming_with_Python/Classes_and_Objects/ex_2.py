"""
Using decorators, add getter and setter methods to your Car class so you can
view and change the color of your car. You should also add getter methods that
let you view but not modify the car's model and year. Don't forget to write
some tests.
"""


class Car:

    def __init__(self, model: str, year: str, color: str):
        self._model = model
        self._year = year
        self._color = color
        self.speed = 0
        self.is_on = False

    @property
    def model(self):
        return self._model

    @property
    def year(self):
        return self._year

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    def start_engine(self):
        self.is_on = True
        print("engine started")

    def accelerate(self, speed):
        self.speed += speed

    def brake(self, speed):
        self.speed -= speed

    def current_speed(self):
        print(f"Currently travelling at {self.speed} mph")

    def turn_off(self):
        self.is_on = False
        print("engine stopped")


pinto = Car("Pinto", 1986, "Red")

print(f"My car is a {pinto.model}")
print(f"My car is {pinto.color}")
print(f"My car is {pinto.year}")
pinto.color = "Orange"
print(f" I just painted my car to {pinto.color}")
pinto.year = 1987
