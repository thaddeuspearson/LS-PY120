"""
Modify the code by writing one new method to make the test cases pass.
"""


class WalkMixin:
    def walk(self):
        return f"{self.name} {self.gait()} forward"


class Person(WalkMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "strolls"


class Cat(WalkMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "saunters"


class Cheetah(WalkMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "runs"


if __name__ == "__main__":
    mike = Person("Mike")
    assert mike.walk() == "Mike strolls forward"

    kitty = Cat("Kitty")
    assert kitty.walk() == "Kitty saunters forward"

    flash = Cheetah("Flash")
    assert flash.walk() == "Flash runs forward"
