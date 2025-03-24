"""
Using the following code, add a method named identify that returns the calling
object.
"""


class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def identify(self):
        return self


if __name__ == "__main__":
    kitty = Cat('Sophie')
    id_str = f"<__main__.Cat object at {hex(id(kitty))}>"
    assert str(kitty.identify()) == id_str, kitty.identify()
