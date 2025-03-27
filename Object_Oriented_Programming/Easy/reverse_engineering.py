"""
Write a class such that the test cases pass:
"""


class Transform:
    def __init__(self, input_str: str):
        self.input_str = input_str

    @property
    def input_str(self) -> str:
        return self._input_str

    @input_str.setter
    def input_str(self, input_str: str):
        self._input_str = input_str

    def uppercase(self):
        return self.input_str.upper()

    @classmethod
    def lowercase(cls, input_str):
        return input_str.lower()


if __name__ == "__main__":
    my_data = Transform('abc')
    assert my_data.uppercase() == "ABC"
    assert Transform.lowercase('XYZ') == "xyz"
