
class Player():
    """Base class for a RPS player"""

    MOVES = ("Rock", "Paper", "Scissors")

    def __init__(self):
        self.move = None

    @property
    def move(self):
        return self._move

    @move.setter
    def move(self, move: str):
        self._move = move


class Human(Player):
    """Human subclass for a RPS player"""

    def __init__(self):
        super().__init__()

    def choose(self):
        pass


class Computer(Player):
    """Computer subclass for a RPS player"""

    def __init__(self):
        super().__init__()

    def choose(self):
        pass


class RockPaperScissorsGame():
    """Driver class for a game of Rock Paper Scissors"""

    def __init__(self):
        self.player_1 = Human()
        self.player_2 = Computer()

    def play(self):
        pass
