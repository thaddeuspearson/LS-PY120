"""
Update this code so you see the following output when you run the code:

    My cat Cocoa is 3 years old and has black fur.
    My cat Cheddar is 4 years old and has yellow and white fur.
"""


class Pet:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age: str):
        self._age = age


class Cat(Pet):

    def __init__(self, name: str, age: int, color: str):
        super().__init__(name, age)
        self.color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color: str):
        self._color = color

    @property
    def info(self) -> str:
        return str(
            f"My {type(self).__name__.lower()} {self.name} is {self.age} years"
            f" old and has {self.color} fur."
        )


if __name__ == "__main__":
    cocoa = Cat('Cocoa', 3, 'black')
    cheddar = Cat('Cheddar', 4, 'yellow and white')
    assert cocoa.info == "My cat Cocoa is 3 years old and has black fur."
    assert cheddar.info == (
        "My cat Cheddar is 4 years old and has yellow and white fur."
    )
