"""
Part One: Change the following code so that creating a new Truck automatically
calls start_engine.

Part Two: Given the following code, modify Truck.start_engine by appending
'Drive fast, please!' to the return value of Vehicle.start_engine. The 'fast'
in 'Drive fast, please!' should be taken from the value of the speed argument.
"""
import sys
from io import StringIO


class Vehicle:
    def __init__(self, year: int):
        self.year = year

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year: int):
        self._year = year

    def start_engine(self, speed: str):
        print(f'Ready to go! Drive {speed}, please!')


class Truck(Vehicle):

    def __init__(self, year: int):
        super().__init__(year)
        self.start_engine("fast")


if __name__ == "__main__":
    original_stdout = sys.stdout
    sys.stdout = StringIO()
    truck1 = Truck(1994)
    output = sys.stdout.getvalue().strip()
    sys.stdout = original_stdout
    assert output == "Ready to go! Drive fast, please!"
    assert truck1.year == 1994
