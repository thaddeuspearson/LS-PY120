"""
Part One: Using the following code, create a Towable mix-in that contains a
method named tow. This method should print I can tow a trailer! when invoked.
The mix-in should be included in the Truck class.

Part Two: Given the following code, create a class named Vehicle that, upon
instantiation, assigns the passed-in argument to self.year. Both Truck and Car
should inherit from Vehicle.
"""


class Vehicle:
    def __init__(self, year: int):
        self.year = year

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, year: int):
        self._year = year


class TowableMixin:
    def tow(self):
        return "I can tow a trailer!"


class Truck(TowableMixin, Vehicle):
    pass


class Car(Vehicle):
    pass


if __name__ == "__main__":
    truck1 = Truck(1994)
    assert truck1.year == 1994
    assert truck1.tow() == "I can tow a trailer!"

    car1 = Car(2006)
    assert car1.year == 2006

    try:
        car1.tow()
    except AttributeError as e:
        print(e)
