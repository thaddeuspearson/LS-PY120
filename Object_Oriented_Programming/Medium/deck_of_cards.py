"""
Using the Card class from the previous exercise, create a Deck class that
contains all of the standard 52 playing cards.

The Deck class should provide a draw method to deal one card. The Deck should
be shuffled when it is initialized. If no more cards remain when draw is
called, the method should generate a new set of 52 shuffled cards, then deal
one card from the new cards.
"""
from random import shuffle
from highest_and_lowest_ranking_cards import Card


class Deck:
    """A class representation of a standard deck of playing cards"""

    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

    def __init__(self):
        self.cards = self._reset()

    def _reset(self):
        """Resets the deck and shuffles it"""
        cards = [
            Card(rank, suit) for rank in Deck.RANKS for suit in Deck.SUITS
        ]
        shuffle(cards)
        return cards

    def draw(self) -> Card:
        """Draws a card from the deck, resets the deck if it is empty"""
        if not self.cards:
            self.cards = self._reset()
        return self.cards.pop()


def tests():
    """Test Cases"""
    deck = Deck()
    drawn = []

    for _ in range(52):
        drawn.append(deck.draw())

    count_rank_5 = sum(1 for card in drawn if card.rank == 5)
    count_hearts = sum(1 for card in drawn if card.suit == 'Hearts')

    assert count_rank_5 == 4
    assert count_hearts == 13

    drawn2 = []
    for _ in range(52):
        drawn2.append(deck.draw())

    assert drawn != drawn2


if __name__ == "__main__":
    tests()
