"""
Add a method to the Car class that lets you spray paint the car a specific
color. Don't use a setter method for this. Instead, create a method whose name
accurately describes what it does. Don't forget to test your code.
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

    def spray_paint(self, color):
        self.color = color
        print(f"Just spray painted the car to {self.color}")

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


pinto = Car("Pinto", 1986, "Orange")

print(f"My car is a {pinto.model}")
print(f"My car is {pinto.color}")
print(f"My car is {pinto.year}")
print(f"My car was {pinto.color}")
pinto.spray_paint("Blue")
