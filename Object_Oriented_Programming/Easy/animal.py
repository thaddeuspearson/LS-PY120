"""
Given the following Animal class, create two more classes, Cat and Dog, that
inherit from it:
"""


class Animal:
    def __init__(self, name: str, age: int,
                 legs: int, species: str, status: str):
        self.name = name
        self.age = age
        self.legs = legs
        self.species = species
        self.status = status

    def introduce(self):
        return (f"Hello, my name is {self.name} and I am "
                f"{self.age} years old and {self.status}.")

    def speak(self):
        pass


class Cat(Animal):
    def __init__(self, name: str, age: int, status: str):
        super().__init__(name, age, 4, "Cat", status)

    def speak(self):
        return "Meow meow!"

    def introduce(self):
        return f"{super().introduce()} {self.speak()}"


class Dog(Animal):
    def __init__(self, name: str, age: int, status: str, owner: str):
        super().__init__(name, age, 4, "Dog", status)
        self.owner = owner

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        self._owner = owner

    def speak(self):
        return "Woof! Woof!"

    def introduce(self):
        return f"{super().introduce()} {self.speak()}"

    def greet_owner(self):
        return f"Hi {self.owner}! {self.speak()}"


if __name__ == "__main__":
    cat = Cat("Pepe", 4, "happy")
    expected = (
        "Hello, my name is Pepe and I am 4 years old and happy. Meow meow!"
    )
    assert cat.introduce() == expected

    dog = Dog("Bobo", 9, "hungry", "Daddy")
    expected = (
        "Hello, my name is Bobo and I am 9 years old and hungry. Woof! Woof!"
    )
    assert dog.introduce() == expected
    assert dog.greet_owner() == "Hi Daddy! Woof! Woof!"
