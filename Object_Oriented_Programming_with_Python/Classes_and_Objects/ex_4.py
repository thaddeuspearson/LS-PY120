"""
Add a class method to your Car class that calculates and prints any car's
average gas mileage (miles per gallon). You can compute the mileage by
dividing the distance traveled (in miles) by the fuel burned (in gallons).
"""


class Car:

    @classmethod
    def gas_milage(cls, miles: int, gallons: int):
        mpg = miles / gallons
        print(f"{mpg} miles per gallon")

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
Car.gas_milage(100, 10)
