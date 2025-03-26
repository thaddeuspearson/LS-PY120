"""
Write the classes and methods that will be necessary to make this code run and
log the expected output:
"""
import sys
from io import StringIO


class Pet:
    def __init__(self, pet_type: str, name: str):
        self.pet_type = pet_type
        self.name = name

    @property
    def pet_type(self) -> str:
        return self._pet_type

    @pet_type.setter
    def pet_type(self, pet_type: str):
        self._pet_type = pet_type

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name


class Owner:
    def __init__(self, name: str):
        self.name = name
        self.pets = []

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def pets(self) -> list:
        return self._pets

    @pets.setter
    def pets(self, pets: list):
        self._pets = pets

    def number_of_pets(self) -> int:
        return len(self.pets)


class Shelter:
    def __init__(self):
        self.owners = []

    def adopt(self, owner: Owner, pet: Pet):
        if owner not in self.owners:
            self.owners.append(owner)
        owner.pets.append(pet)

    def print_adoptions(self):
        for owner in self.owners:
            print(f"{owner.name} has adopted the following pets:")

            for pet in owner.pets:
                print(f"a {pet.pet_type} named {pet.name}")
            print()


def pet_shelter():
    cocoa = Pet('cat', 'Cocoa')
    cheddar = Pet('cat', 'Cheddar')
    darwin = Pet('bearded dragon', 'Darwin')
    kennedy = Pet('dog', 'Kennedy')
    sweetie = Pet('parakeet', 'Sweetie Pie')
    molly = Pet('dog', 'Molly')
    chester = Pet('fish', 'Chester')

    phanson = Owner('P Hanson')
    bholmes = Owner('B Holmes')

    shelter = Shelter()
    shelter.adopt(phanson, cocoa)
    shelter.adopt(phanson, cheddar)
    shelter.adopt(phanson, darwin)
    shelter.adopt(bholmes, molly)
    shelter.adopt(bholmes, sweetie)
    shelter.adopt(bholmes, kennedy)
    shelter.adopt(bholmes, chester)

    return shelter


if __name__ == "__main__":
    shelter = pet_shelter()
    original_stdout = sys.stdout
    sys.stdout = StringIO()
    shelter.print_adoptions()
    output = sys.stdout.getvalue().strip()
    sys.stdout = original_stdout

    assert output == (
        "P Hanson has adopted the following pets:\n"
        "a cat named Cocoa\n"
        "a cat named Cheddar\n"
        "a bearded dragon named Darwin\n"
        "\n"
        "B Holmes has adopted the following pets:\n"
        "a dog named Molly\n"
        "a parakeet named Sweetie Pie\n"
        "a dog named Kennedy\n"
        "a fish named Chester"
    )
    phanson = shelter.owners[0]
    assert f"{phanson.name} has {phanson.number_of_pets()} adopted pets."

    bholmes = shelter.owners[1]
    assert f"{bholmes.name} has {bholmes.number_of_pets()} adopted pets."
