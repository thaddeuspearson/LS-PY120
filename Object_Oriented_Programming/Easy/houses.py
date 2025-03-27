"""
Modify the House class so the program work as shown.
"""


class House:
    def __init__(self, price):
        self._price = price

    def __gt__(self, other):
        return self.price > other.price

    def __lt__(self, other):
        return self.price < other.price

    def __eq__(self, other):
        return self.price == other.price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value


if __name__ == "__main__":
    home1 = House(100000)
    home2 = House(150000)
    assert home1 < home2, "Home 1 is cheaper"
    assert home2 > home1, "Home 2 is more expensive"
