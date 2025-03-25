"""
Complete this class so that the test cases shown below work as intended. You
are free to add any methods or instance variables you need. However, methods
prefixed with an underscore are intended for internal use and should not be
called externally.

You may assume that the input will always fit in your terminal window.
"""


class Banner:
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "\n".join([self._horizontal_rule(),
                          self._empty_line(),
                          self._message_line(),
                          self._empty_line(),
                          self._horizontal_rule()])

    @property
    def message(self) -> str:
        return self._message

    @message.setter
    def message(self, message: str):
        self._message = message

    def _empty_line(self):
        return f"| {' ' * len(self.message)} |"

    def _horizontal_rule(self):
        return f"+-{'-' * len(self.message)}-+"

    def _message_line(self):
        return f"| {self.message} |"


if __name__ == "__main__":
    banner = Banner('To boldly go where no one has gone before.')
    assert str(banner) == (
        "+--------------------------------------------+\n"
        "|                                            |\n"
        "| To boldly go where no one has gone before. |\n"
        "|                                            |\n"
        "+--------------------------------------------+"
    )

    banner = Banner('')
    assert str(banner) == (
        "+--+\n"
        "|  |\n"
        "|  |\n"
        "|  |\n"
        "+--+"
    )
