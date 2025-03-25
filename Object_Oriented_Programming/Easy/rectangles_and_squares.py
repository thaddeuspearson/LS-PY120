"""
Write a class called Square that inherits from the Rectangle class. The Square
class is used like this:
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


class Square(Rectangle):
    def __init__(self, side: int):
        super().__init__(side, side)


if __name__ == '' "__main__":
    square = Square(5)
    assert square.area == 25
