"""
How do we create a class and an object in Python?

Write a program that defines a class and creates two objects from that class.
The class should have at least one instance variable that gets initialized by
the initializer.

What class you create doesn't matter, provided it satisfies the above
requirements.
"""


class Instrument:

    def __init__(self, category: str):
        """Initializes the instance variable cartegory"""
        self.category = category


drums = Instrument("Percussion")
guitar = Instrument("String")
