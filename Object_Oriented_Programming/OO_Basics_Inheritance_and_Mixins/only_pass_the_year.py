"""
Using the following code, modify Truck to accept a second argument when
instantiating a new Truck object. Name the parameter bed_type. Ensure that the
Car constructor continues to accept only one argument.
"""


class Vehicle:
    def __init__(self, year):
        self.year = year

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year: int):
        self._year = year


class Truck(Vehicle):
    def __init__(self, year: int, bed_type: str):
        super().__init__(year)
        self.bed_type = bed_type

    @property
    def bed_type(self) -> str:
        return self._bed_type

    @bed_type.setter
    def bed_type(self, bed_type: str):
        self._bed_type = bed_type


class Car(Vehicle):
    pass


if __name__ == "__main__":
    truck1 = Truck(1994, 'Short')
    assert truck1.year == 1994
    assert truck1.bed_type == "Short"

    car1 = Car(2006)
    assert car1.year == 2006
    try:
        car1.bed_type
    except AttributeError:
        print("AttributeError: 'Car' object has no attribute 'bed_type'")
