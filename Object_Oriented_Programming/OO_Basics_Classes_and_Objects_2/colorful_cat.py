"""
Create a class named Cat that prints a greeting when the greet instance method
is invoked. The greeting should include the name and color of the cat. Use a
class constant to define the color.
"""
import sys
from io import StringIO


class Cat:

    COLOR = "Orange"

    def __init__(self, name: str):
        self.name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    def greet(self):
        print(f"Hello! My name is {self.name} and I'm a(n) {Cat.COLOR} cat!")


if __name__ == "__main__":
    original_stdout = sys.stdout
    sys.stdout = StringIO()
    kitty = Cat("Sophie")
    kitty.greet()
    output = sys.stdout.getvalue().strip()
    sys.stdout = original_stdout
    assert output == "Hello! My name is Sophie and I'm a(n) Orange cat!"
