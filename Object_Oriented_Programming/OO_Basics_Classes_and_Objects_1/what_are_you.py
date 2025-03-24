"""
Using the code from the previous exercise, add a __init__ method that prints
I'm a cat! when a new Cat object is instantiated.
"""
import sys
from io import StringIO


class Cat:

    def __init__(self):
        print("I'm a cat!")


if __name__ == "__main__":
    original_stdout = sys.stdout
    sys.stdout = StringIO()
    kitty = Cat()
    output = sys.stdout.getvalue().strip()
    sys.stdout = original_stdout
    assert str(output) == "I'm a cat!"
