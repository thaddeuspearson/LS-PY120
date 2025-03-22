"""
Create a Car class that makes the following code work as indicated.
"""


class Car:

    def __init__(self, name: str, year: int, color: str):
        self.name = name
        self.year = year
        self.color = color

    def __str__(self):
        return f"{self.color.title()} {self.year} {self.name}"

    def __repr__(self):
        return f"Car({repr(self.name)}, {repr(self.year)}, {repr(self.color)})"

    @classmethod
    def _validate_input(cls, input: int | str,
                        input_type: int | str,
                        prop: str):
        if not isinstance(input, input_type):
            raise TypeError(
                f"property '{prop}' must be a {input_type.__name__}"
            )

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        Car._validate_input(name, str, "name")
        self._name = name

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year: int):
        Car._validate_input(year, int, "year")
        self._year = year

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color: str):
        Car._validate_input(color, str, "color")
        self._color = color


if __name__ == "__main__":
    vwbuzz = Car('ID.Buzz', 2024, 'red')
    assert str(vwbuzz) == "Red 2024 ID.Buzz", str(vwbuzz)
    assert repr(vwbuzz) == "Car('ID.Buzz', 2024, 'red')", repr(vwbuzz)
