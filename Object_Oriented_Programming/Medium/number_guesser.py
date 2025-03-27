"""
Create an object-oriented number guessing class for numbers in the range 1 to
100, with a limit of 7 guesses per game. Note that a game object should start
a new game with a new number to guess with each call to play.
"""
from random import randint


class GuessingGame:
    def __init__(self, start: int = 1, end: int = 100):
        self.number = randint(start, end)
        self.start = start
        self.end = end
        self.num_guesses = 7

    def play(self):
        winner = False

        while not winner and self.num_guesses:
            print(self._num_remaining_guesses())
            guess = self.get_valid_guess()
            winner = self.process_guess(guess)
            self.num_guesses -= 1

        if winner:
            print("\nYou won!")
        else:
            print("\nYou have no more guesses. You lost!")

    def get_valid_guess(self):
        guess = input(self._guess_prompt())

        while not self._validate_guess(guess):
            guess = input(f"Invalid Guess. {self._guess_prompt()}")
        return guess

    def process_guess(self, guess):
        guess = int(guess)

        if guess == self.number:
            print("\nThat's the Number!")
            return True
        if guess > self.number:
            high_or_low = "high"
        else:
            high_or_low = "low"

        print(f"Your guess is too {high_or_low}.\n")
        return False

    def _validate_guess(self, guess: int):
        return self.start <= int(guess) <= self.end

    def _num_remaining_guesses(self):
        return f"You have {self.num_guesses} guesses remaining."

    def _guess_prompt(self):
        return f"Enter a number between {self.start} and {self.end}: "


if __name__ == "__main__":
    game = GuessingGame()
    game.play()
