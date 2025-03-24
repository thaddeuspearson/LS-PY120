"""
Using the following code, add an instance method named rename that renames
kitty when invoked.
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

    def rename(self, new_name: str):
        self.name = new_name


if __name__ == "__main__":
    kitty = Cat('Sophie')
    assert kitty.name == "Sophie"
    kitty.rename('Chloe')
    assert kitty.name == "Chloe"
