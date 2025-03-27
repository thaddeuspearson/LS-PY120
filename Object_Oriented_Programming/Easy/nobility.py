"""
Now that we have a WalkMixin mix-in, we are given a new challenge. Apparently
some of our users are nobility, and the regular way of walking simply isn't
good enough. Nobility struts.

We need a new class Noble that shows the title and name when walk is called.
We also require access to name and title; they are needed for other purposes
that we aren't showing here.
"""
from abc import ABC


class Animal(ABC):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

    def walk(self):
        return f"{self} {self.gait()} forward"


class Person(Animal):
    def __init__(self, name: str):
        super().__init__(name)

    def gait(self):
        return "strolls"


class Cat(Animal):
    def __init__(self, name: str):
        super().__init__(name)

    def gait(self):
        return "saunters"


class Cheetah(Cat):
    def __init__(self, name: str):
        super().__init__(name)

    def gait(self):
        return "runs"


class Noble(Person):
    def __init__(self, name: str, title: str):
        super().__init__(name)
        self.title = title

    def __str__(self):
        return f"{self.title} {self.name}"

    def gait(self):
        return "struts"


if __name__ == "__main__":
    mike = Person("Mike")
    assert mike.walk() == "Mike strolls forward"

    kitty = Cat("Kitty")
    assert kitty.walk() == "Kitty saunters forward"

    flash = Cheetah("Flash")
    assert flash.walk() == "Flash runs forward"

    byron = Noble("Byron", "Lord")
    assert byron.walk() == "Lord Byron struts forward"
    assert byron.name == "Byron"
    assert byron.title == "Lord"
