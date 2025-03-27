"""
Update the Card class so it can be used to determine the lowest ranking and
highest ranking cards in a list of Card objects
"""


class Card:
    """A class representing a common playing card"""

    VALUES = {"Jack": 11, "Queen": 12, "King": 13, "Ace": 14}

    def __init__(self, rank: int | str, suit: str):
        self.rank = rank
        self.suit = suit

    @property
    def value(self) -> int:
        return Card.VALUES.get(self.rank, self.rank)

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"

    def __repr__(self) -> str:
        return f"Card({repr(self.rank)}, {repr(self.suit)})"

    def __gt__(self, other) -> bool:
        return self.value > other.value

    def __lt__(self, other) -> bool:
        return self.value < other.value

    def __eq__(self, other) -> bool:
        return (self.value == other.value) and (self.suit == other.suit)


def tests():
    """Test Cases"""
    cards = [
        Card(2, 'Hearts'),
        Card(10, 'Diamonds'),
        Card('Ace', 'Clubs')
    ]
    assert min(cards) == Card(2, 'Hearts')
    assert max(cards) == Card('Ace', 'Clubs')
    assert str(min(cards)) == "2 of Hearts", str(min(cards))
    assert str(max(cards)) == "Ace of Clubs"

    cards = [
        Card(5, 'Hearts')
    ]
    assert min(cards) == Card(5, 'Hearts')
    assert max(cards) == Card(5, 'Hearts')
    assert str(Card(5, 'Hearts')) == "5 of Hearts"

    cards = [
        Card(4, 'Hearts'),
        Card(4, 'Diamonds'),
        Card(10, 'Clubs')
    ]
    assert min(cards).rank == 4
    assert max(cards) == Card(10, 'Clubs')
    assert str(Card(10, 'Clubs')) == "10 of Clubs"

    cards = [
        Card(7, 'Diamonds'),
        Card('Jack', 'Diamonds'),
        Card('Jack', 'Spades')
    ]
    assert min(cards) == Card(7, 'Diamonds')
    assert max(cards).rank == 'Jack'
    assert str(Card(7, 'Diamonds')) == "7 of Diamonds"

    cards = [
        Card(8, 'Diamonds'),
        Card(8, 'Clubs'),
        Card(8, 'Spades')
    ]
    assert min(cards).rank == 8
    assert max(cards).rank == 8


if __name__ == "__main__":
    tests()
