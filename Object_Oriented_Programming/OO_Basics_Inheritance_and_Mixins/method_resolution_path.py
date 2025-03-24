"""
Part One: Using the code below, determine the method resolution order (MRO)
used when accessing the cat1.color property. Only list the classes that are
checked by Python when searching for the color attribute. Do not use the mro
method.

Part Three: Using the code below, determine the method resolution order used
when invoking bird1.color. Only list the classes or mix-ins that Python will
check when searching for the color method. Do not use the mro method.
"""


class FlyingMixin:
    def fly(self):
        return "I'm flying!"


class Animal:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color


class Cat(Animal):
    pass


class Bird(FlyingMixin, Animal):
    pass


if __name__ == "__main__":
    cat1 = Cat('Black')
    cat_mro_names = [cls.__name__ for cls in Cat.mro()]
    assert cat_mro_names == ["Cat", "Animal", "object"]

    bird1 = Bird('Red')
    bird_mro_names = [cls.__name__ for cls in Bird.mro()]
    assert bird_mro_names == ["Bird", "FlyingMixin", "Animal", "object"]
