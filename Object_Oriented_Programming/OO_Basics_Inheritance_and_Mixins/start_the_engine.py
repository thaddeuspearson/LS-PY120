"""
Change the following code so that creating a new Truck automatically calls
start_engine.
"""
import sys
from io import StringIO


class Vehicle:
    def __init__(self, year: int):
        self._year = year

    @property
    def year(self):
        return self._year


class Truck(Vehicle):

    def __init__(self, year: int):
        super().__init__(year)
        self.start_engine()

    def start_engine(self):
        print('Ready to go!')


if __name__ == "__main__":
    original_stdout = sys.stdout
    sys.stdout = StringIO()
    truck1 = Truck(1994)
    output = sys.stdout.getvalue().strip()
    sys.stdout = original_stdout
    assert output == "Ready to go!"
    assert truck1.year == 1994
