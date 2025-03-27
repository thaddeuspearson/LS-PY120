"""
Part One: Create an object-oriented number guessing class for numbers in the
range 1 to 100, with a limit of 7 guesses per game. Note that a game object
should start a new game with a new number to guess with each call to play.

Part Two: Update your solution to accept a low and high value when you create
a GuessingGame object, and use those values to compute a secret number for the
game. You should also change the number of guesses allowed so the user can
always win if she uses a good strategy.
"""
from random import randint
from math import log2


class GuessingGame:
    """
    An implementation of the classic guess what number I am thinking about.
    Accepts the start and end of the range to guess from and the number of
    guesses given to the user.
    """
    def __init__(self, num_guesses: int = 0, start: int = 1, end: int = 100):
        if start > end:
            start, end = end, start
        if not num_guesses or num_guesses < 1:
            self.num_guesses = int(log2(end - start + 1)) + 1
        else:
            self.num_guesses = num_guesses
        self.number = randint(start, end)
        self.start = start
        self.end = end

    def play(self):
        """Driver code for gameplay"""
        winner = False

        while not winner and self.num_guesses:
            print(self._remaining_guesses_prompt())
            guess = self.get_valid_guess()
            winner = self.process_guess(guess)
            self.num_guesses -= 1

        if winner:
            print("\nYou won!")
        else:
            print("\nYou have no more guesses. You lost!")

    def get_valid_guess(self) -> str:
        """Retrieves valid guess from th user"""
        guess = input(self._guess_prompt())

        while not self._validate_guess(guess):
            guess = input(f"Invalid Guess. {self._guess_prompt()}")
        return guess

    def process_guess(self, guess: str) -> bool:
        """Transforms and Processes the given guess"""
        guess = int(guess)
        if guess == self.number:
            print("\nThat's the Number!")
            return True
        if guess > self.number:
            high_or_low = "high"
        else:
            high_or_low = "low"
        print(f"\nYour guess is too {high_or_low}.\n")
        return False

    def _validate_guess(self, guess: str) -> bool:
        """Validates input given for the guess"""
        try:
            return self.start <= int(guess) <= self.end
        except ValueError:
            return False

    def _remaining_guesses_prompt(self) -> str:
        """Returns the string that displays how many guesses remain"""
        return f"You have {self.num_guesses} guesses remaining."

    def _guess_prompt(self) -> str:
        """Returns the string which prompts the user to enter a guess"""
        return f"Enter a number between {self.start} and {self.end}: "


if __name__ == "__main__":
    game = GuessingGame()
    game.play()
