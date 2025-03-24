"""
Create a class named Cat for which calling Cat.generic_greeting prints:
"Hello! I'm a cat!" >
"""
import sys
from io import StringIO


class Cat:

    @classmethod
    def generic_greeting(cls):
        print("Hello! I'm a cat!")


if __name__ == "__main__":
    original_stdout = sys.stdout
    sys.stdout = StringIO()
    Cat.generic_greeting()
    output = sys.stdout.getvalue().strip()
    sys.stdout = original_stdout
    assert output == "Hello! I'm a cat!"
