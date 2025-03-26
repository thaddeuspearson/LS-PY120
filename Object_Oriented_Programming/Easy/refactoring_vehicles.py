"""
Refactor these classes so they all use a common superclass, and inherit
behavior as needed.
"""


class Vehicle:
    def __init__(self, make: str, model: str, wheels: int):
        self.make = make
        self.model = model
        self.wheels = wheels

    @property
    def make(self) -> str:
        return self._make

    @make.setter
    def make(self, make: str):
        self._make = make

    @property
    def model(self) -> str:
        return self._model

    @model.setter
    def model(self, model: str):
        self._model = model

    @property
    def wheels(self) -> int:
        return self._wheels

    @wheels.setter
    def wheels(self, wheels: int):
        self._wheels = wheels

    def info(self):
        return f"{self.make} {self.model}"


class Car(Vehicle):
    def __init__(self, make: str, model: str):
        super().__init__(make, model, wheels=4)


class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str):
        super().__init__(make, model, wheels=2)


class Truck(Vehicle):
    def __init__(self, make: str, model: str, payload: str):
        super().__init__(make, model, wheels=6)
        self.payload = payload

    @property
    def payload(self) -> str:
        return self._payload

    @payload.setter
    def payload(self, payload):
        self._payload = payload
