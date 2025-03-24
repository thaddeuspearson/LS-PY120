"""
Create a class named Cat for which calling Cat.generic_greeting prints:
"Hello! I'm a cat!" >
"""
import sys
from io import StringIO


class Cat:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @classmethod
    def generic_greeting(cls):
        print("Hello! I'm a cat!")

    def personal_greeting(self):
        print(f"Hello! My name is {self.name}!")


if __name__ == "__main__":
    original_stdout = sys.stdout
    sys.stdout = StringIO()
    Cat.generic_greeting()
    output = sys.stdout.getvalue().strip()
    assert str(output) == "Hello! I'm a cat!"

    sys.stdout.seek(0)
    sys.stdout.truncate(0)

    kitty = Cat("Sophie")
    kitty.personal_greeting()
    output = sys.stdout.getvalue().strip()
    sys.stdout = original_stdout
    assert output == "Hello! My name is Sophie!"
