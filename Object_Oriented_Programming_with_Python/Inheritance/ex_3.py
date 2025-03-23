"""
Create a mix-in for the Car and Truck classes from the previous exercise that
lets you operate the turn signals: signal left, signal right, and signal off.
Use the following code to test your code.
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
    car1 = Car()
    truck1 = Truck()
    boat1 = Boat()

    assert car1.signal_left() == "Signalling left"
    assert truck1.signal_right() == "Signalling right"
    assert car1.signal_off() == "Signal is now off"
    assert truck1.signal_off() == "Signal is now off"

    boat1.signal_left()
    # AttributeError: 'Boat' object has no attribute
    # 'signal_left'
