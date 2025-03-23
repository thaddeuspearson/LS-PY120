"""
Print the method resolution order for cars, trucks, boats, and vehicles as
defined in the previous exercise.
"""


class SignalMixin:

    @staticmethod
    def signal_left():
        return "Signalling left"

    @staticmethod
    def signal_right():
        return "Signalling right"

    @staticmethod
    def signal_off():
        return "Signal is now off"


class Vehicle:

    _num_vehicles = 0

    def __init__(self):
        Vehicle._num_vehicles += 1

    @classmethod
    def vehicles(cls):
        return Vehicle._num_vehicles


class Car(SignalMixin, Vehicle):

    def __init__(self):
        super().__init__()


class Truck(SignalMixin, Vehicle):

    def __init__(self):
        super().__init__()


class Boat(Vehicle):

    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    print(Car.mro())
    print(Truck.mro())
    print(Boat.mro())
    print(Vehicle.mro())
