"""
Part One: Using the following code, create a Towable mix-in that contains a
method named tow. This method should print I can tow a trailer! when invoked.
The mix-in should be included in the Truck class.

"""


class TowableMixin:
    def tow(self):
        return "I can tow a trailer!"


class Truck(TowableMixin):
    pass


class Car:
    pass


if __name__ == "__main__":
    truck1 = Truck()
    assert truck1.tow() == "I can tow a trailer!"

    car1 = Car()
    try:
        car1.tow()
    except AttributeError as e:
        print(e)
