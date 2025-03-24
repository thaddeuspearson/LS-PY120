"""
Using the code from the previous exercise, add a parameter to __init__ that
provides a name for the Cat object. Use an instance variable to print a
greeting with the provided name.
"""

import sys
from io import StringIO


class Cat:

    def __init__(self, name: str):
        self.name = name
        self.greet()

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    def greet(self):
        print(f"Hello! My name is {self.name}!")


if __name__ == "__main__":
    original_stdout = sys.stdout
    sys.stdout = StringIO()
    kitty = Cat("Sophie")
    output = sys.stdout.getvalue().strip()
    sys.stdout = original_stdout
    assert str(output) == "Hello! My name is Sophie!"
