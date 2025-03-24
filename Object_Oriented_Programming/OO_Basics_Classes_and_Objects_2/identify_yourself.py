"""
Using the following code, add a method named identify that returns the calling
object.
"""


class Cat:
    def __init__(self, name):
        self._name = name

    def __str__(self) -> str:
        return f"I'm {self.name}!"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def identify(self):
        return f"<__main__.Cat object at {hex(id(kitty))}>"


if __name__ == "__main__":
    kitty = Cat('Sophie')
    id_str = f"<__main__.Cat object at {hex(id(kitty))}>"
    assert kitty.identify() == id_str
    assert str(kitty) == "I'm Sophie!"
