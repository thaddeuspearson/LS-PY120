"""
Create a Rectangle class whose initializer takes two arguments that represent
the rectangle's width and height, respectively.
"""


class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, width: int):
        self._width = width

    @property
    def length(self) -> int:
        return self._length

    @length.setter
    def length(self, length: int):
        self._length = length

    @property
    def area(self) -> int:
        return self.width * self.height


if __name__ == "__main__":
    rect = Rectangle(4, 5)
    assert rect.width == 4
    assert rect.height == 5
    assert rect.area == 20
