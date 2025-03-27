"""
Create a class, PokerHand, that takes 5 cards from a Deck of Cards and
evaluates those cards as a poker hand.
"""
from deck_of_cards import Deck
from highest_and_lowest_ranking_cards import Card


class PokerHand:
    def __init__(self, deck: Deck = Deck()):
        self.cards = [deck.draw() for _ in range(5)]
        self.rank_counts = self._get_rank_counts()

    def print(self):
        for card in self.cards:
            print(card)

    def _get_rank_counts(self):
        rank_counts = {}

        for card in self.cards:
            rank_counts[card.rank] = rank_counts.get(card.rank, 0) + 1
        return rank_counts

    def evaluate(self):
        if self._is_royal_flush():
            return "Royal flush"
        elif self._is_straight_flush():
            return "Straight flush"
        elif self._is_four_of_a_kind():
            return "Four of a kind"
        elif self._is_full_house():
            return "Full house"
        elif self._is_flush():
            return "Flush"
        elif self._is_straight():
            return "Straight"
        elif self._is_three_of_a_kind():
            return "Three of a kind"
        elif self._is_two_pair():
            return "Two pair"
        elif self._is_pair():
            return "Pair"
        else:
            return "High card"

    def _is_royal_flush(self):
        return (
            self._is_flush() and
            sorted([card.value for card in self.cards]) == [10, 11, 12, 13, 14]
        )

    def _is_straight_flush(self):
        return self._is_flush() and self._is_straight()

    def _is_four_of_a_kind(self):
        return 4 in self.rank_counts.values()

    def _is_full_house(self):
        return (
            (list(self.rank_counts.values())).count(2) == 1 and
            (list(self.rank_counts.values())).count(3) == 1
        )

    def _is_flush(self):
        return len(set(card.suit for card in self.cards)) == 1

    def _is_straight(self):
        sorted_hand = sorted([card.value for card in self.cards])
        return sorted_hand == list(range(sorted_hand[0], sorted_hand[-1]+1))

    def _is_three_of_a_kind(self):
        return (list(self.rank_counts.values())).count(3) == 1

    def _is_two_pair(self):
        return (list(self.rank_counts.values())).count(2) == 2

    def _is_pair(self):
        return (list(self.rank_counts.values())).count(2) == 1


hand = PokerHand(Deck())
hand.print()
print(hand.evaluate())
print()


class TestDeck(Deck):
    def __init__(self, cards):
        self.cards = cards


hand = PokerHand(
    TestDeck(
        [
            Card("Ace", "Hearts"),
            Card("Queen", "Hearts"),
            Card("King", "Hearts"),
            Card("Jack", "Hearts"),
            Card(10, "Hearts"),
        ]
    )
)
assert hand.evaluate() == "Royal flush", "Test Royal Flush Failed"

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Clubs"),
            Card("Queen", "Clubs"),
            Card(10, "Clubs"),
            Card("Jack", "Clubs"),
        ]
    )
)
assert hand.evaluate() == "Straight flush", "Test: Straight Flush Failed"

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
assert hand.evaluate() == "Four of a kind", "Test: Four-of-a-Kind Failed"

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
assert hand.evaluate() == "Full house", "Test: Full House Failed"

hand = PokerHand(
    TestDeck(
        [
            Card(10, "Hearts"),
            Card("Ace", "Hearts"),
            Card(2, "Hearts"),
            Card("King", "Hearts"),
            Card(3, "Hearts"),
        ]
    )
)
assert hand.evaluate() == "Flush", "Test: Flush Failed"

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Diamonds"),
            Card(10, "Clubs"),
            Card(7, "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
assert hand.evaluate() == "Straight", "Test: 1 Straight Failed"

hand = PokerHand(
    TestDeck(
        [
            Card("Queen", "Clubs"),
            Card("King", "Diamonds"),
            Card(10, "Clubs"),
            Card("Ace", "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
assert hand.evaluate() == "Straight", "Test: 2 Straight Failed"

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(6, "Diamonds"),
        ]
    )
)
assert hand.evaluate() == "Three of a kind", "Test: Three-of-a-Kind Failed"

hand = PokerHand(
    TestDeck(
        [
            Card(9, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(8, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
assert hand.evaluate() == "Two pair", "Test: Two Pair Failed"

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
assert hand.evaluate() == "Pair", "Test: Pair Failed"

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card("King", "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
assert hand.evaluate() == "High card", "Test: High Card Failed"
