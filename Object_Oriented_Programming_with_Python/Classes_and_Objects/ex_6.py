"""
Going back to your solution to exercise 1, refactor the code to replace any
methods that can be converted to static methods.
"""


class Car:

    def __init__(self, model: str, year: str, color: str):
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0

    @staticmethod
    def start_engine():
        print("engine started")

    @staticmethod
    def turn_off(self):
        print("engine stopped")

    def accelerate(self, speed):
        self.speed += speed

    def brake(self, speed):
        self.speed -= speed

    def current_speed(self):
        print(f"Currently travelling at {self.speed} mph")


pinto = Car("Pinto", 1986, "Red")
