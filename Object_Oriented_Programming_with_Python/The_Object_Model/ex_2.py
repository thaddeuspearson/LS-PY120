"""
Given an instance of a Foo object, show two ways to print I am a Foo object
without hardcoding the word Foo.
"""


class Foo:
    pass


foo = Foo()
print(f"I am a {type(foo).__name__} object")
print(f"I am a {foo.__class__.__name__} object")
