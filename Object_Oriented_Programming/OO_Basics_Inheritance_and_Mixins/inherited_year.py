"""
Using the following code, create two classes -- Truck and Car -- that both
inherit from Vehicle.
"""


class Vehicle:
    def __init__(self, year: int):
        self._year = year

    @property
    def year(self) -> int:
        return self._year


class Truck(Vehicle):
    def __init__(self, year: int):
        super().__init__(year)


class Car(Vehicle):
    def __init__(self, year: int):
        super().__init__(year)


if __name__ == "__main__":
    truck1 = Truck(1994)
    assert truck1.year == 1994

    car1 = Car(2006)
    assert car1.year == 2006
