"""
Create a Car class that meets these requirements:

Each Car object should have a model, model year, and color provided at
instantiation time. You should have an instance variable that keeps track of
the current speed. Initialize it to 0 when you instantiate a new car. Create
instance methods that let you turn the engine on, accelerate, brake, and turn
the engine off. Each method should display an appropriate message. Create a
method that prints a message about the car's current speed. Write some code to
test the methods.
"""


class Car:

    def __init__(self, model: str, year: str, color: str):
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0
        self.is_on = False

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
pinto.start_engine()
pinto.accelerate(15)
pinto.current_speed()
pinto.brake(15)
pinto.turn_off()
