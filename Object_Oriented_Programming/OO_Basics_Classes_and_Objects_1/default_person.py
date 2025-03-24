"""
Create a class named Person.

When you instantiate a Person object, you should pass in one argument that
contains the person's name.

If no arguments are given, the Person object should be instantiated with a
name of "John Doe".
"""


class Person:

    def __init__(self, name: str = "John Doe"):
        self.name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name


if __name__ == "__main__":
    clark = Person("Clark Kent")
    john = Person()
    assert clark.name == "Clark Kent"
    assert john.name == "John Doe"
