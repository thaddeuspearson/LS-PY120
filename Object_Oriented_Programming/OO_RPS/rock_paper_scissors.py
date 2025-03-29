import random
from time import sleep
from os import system


class Player():
    """Base class for a RPS player"""

    CHOICES = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    def __init__(self):
        self.choice = None

    @property
    def choice(self):
        return self._choice

    @choice.setter
    def choice(self, choice: str):
        self._choice = choice


class Human(Player):
    """Human subclass for a RPS player"""

    def __init__(self):
        super().__init__()

    def pick(self):
        while not self.choice:
            choice = input(
                f"Please choose a valid throw -> "
                f"{str(', '.join(Player.CHOICES))}: "
            ).lower()
            self.choice = choice if choice in Player.CHOICES else None


class Computer(Player):
    """Computer subclass for a RPS player"""

    def __init__(self):
        super().__init__()

    def pick(self):
        self.choice = random.choice(list(Player.CHOICES.keys()))


class RPSAnimation:
    """Displays 2 stick figures playing Rock Paper Scissors"""

    throws = {
        "l_scissors": "8<",
        "r_scissors": ">8",
        "l_paper": "─ ",
        "r_paper": " ─",
        "l_rock": "O ",
        "r_rock": " O"
    }

    def __init__(self, player_choice, computer_choice):
        self.player_throw = RPSAnimation.throws[f"l_{player_choice}"]
        self.computer_throw = RPSAnimation.throws[f"r_{computer_choice}"]

    def _arms_up(self):
        return """
         █▌     ▐█
        ─┼┘     └┼─
        ┌┴┐     ┌┴┐
        ╜ ╙     ╜ ╙
        """

    def _arms_down(self):
        return """
         █▌     ▐█
        ─┼─     ─┼─
        ┌┴┐     ┌┴┐
        ╜ ╙     ╜ ╙
        """

    def _shoot(self):
        return f"""
         █▌     ▐█
        ─┼─{self.player_throw} {self.computer_throw}─┼─
        ┌┴┐     ┌┴┐
        ╜ ╙     ╜ ╙
        """

    def animate(self):
        for _ in range(3):
            system("clear")
            print(self._arms_down())
            sleep(.25)
            system("clear")
            print(self._arms_up())
            sleep(.25)
        system("clear")
        print(self._shoot())
        sleep(.25)


class RockPaperScissorsGame():
    """Driver class for a game of Rock Paper Scissors"""

    def __init__(self):
        self.human = Human()
        self.computer = Computer()
        self.winner = None

    @property
    def winner(self):
        return self._winner

    @winner.setter
    def winner(self, winner: str):
        self._winner = winner

    def play(self):
        """Driver function for gameplay"""
        while True:
            system("clear")
            self._print_welcome()
            self._players_choose()
            animation = RPSAnimation(self.human.choice, self.computer.choice)
            animation.animate()
            self._print_winner()
            if not self._play_again():
                break
        self._print_goodbye()

    def _players_choose(self):
        for player in (self.human, self.computer):
            player.pick()

    def _reset_players(self):
        for player in (self.human, self.computer):
            player.choice = None

    def _determine_winner(self):
        if (self.human.choice, self.computer.choice) in Player.CHOICES.items():
            self.winner = "Human"
        elif self.human.choice == self.computer.choice:
            self.winner = "Tie"
        else:
            self.winner = "Computer"

    def _print_winner(self):
        print(f"\nPlayer picked: {self.human.choice}")
        print(f"Computer picked: {self.computer.choice}")
        self._determine_winner()

        if self.winner == "Human":
            print("\nYou Win!\n")
        elif self.winner == "Computer":
            print("\nSo sorry, you lose.")
        else:
            print("\nIt is a tie.\n")

    def _print_welcome(self):
        print(f"\n O ─ 8<  Welcome to {' '.join(Player.CHOICES)}  >8 ─ O \n")

    def _print_goodbye(self):
        print(f"\nThank you for playing {' '.join(Player.CHOICES)}. Goodbye!")

    def _play_again(self):
        yes_or_no = input("Would you like to play again (yes/no)? ")
        if yes_or_no.lower().startswith("y"):
            self._reset_players()
            return True


if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.play()
