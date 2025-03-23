"""
Write the code needed to make the following code work as shown:
"""


class Vehicle:

    _num_vehicles = 0

    def __init__(self):
        Vehicle._num_vehicles += 1

    @classmethod
    def vehicles(cls):
        return Vehicle._num_vehicles


class Car(Vehicle):

    def __init__(self):
        super().__init__()


class Truck(Vehicle):

    def __init__(self):
        super().__init__()


class Boat(Vehicle):

    def __init__(self):
        super().__init__()


if __name__ == "__main__":

    assert Car.vehicles() == 0
    car1 = Car()

    assert Car.vehicles() == 1
    car2 = Car()
    car3 = Car()
    car4 = Car()

    assert Car.vehicles() == 4
    truck1 = Truck()
    truck2 = Truck()

    assert Truck.vehicles() == 6

    boat1 = Boat()
    boat2 = Boat()
    assert Boat.vehicles() == 8
