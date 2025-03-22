"""
Earlier, we wrote the following class:
"""
from math import sqrt


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)

    def __mul__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        return (self.x * other.x) + (self.y * other.y)

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        return self.x == other.x and self.y == other.y

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        x = repr(self.x)
        y = repr(self.y)
        return f'Vector({x}, {y})'

    @classmethod
    def _validate_input(cls, input: int, input_type: int, prop: str):
        if not isinstance(input, input_type):
            raise TypeError(
                f"property '{prop}' should be a {input_type.__name__}"
            )

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        Vector._validate_input(x, int, "x")
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        Vector._validate_input(y, int, "y")
        self._y = y


"""
Update this class so the following code works as indicated:
"""

v1 = Vector(5, 12)
v2 = Vector(13, -4)
assert v1 + v2 == Vector(18, 8)
assert v1 - v2 == Vector(-8, 16)
assert v1 * v2 == 17
assert abs(v1) == 13.0, abs(v1)
