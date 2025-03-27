"""
Part One:
Implement a Wallet class that represents a wallet with a certain amount of
money. You want to be able to combine (add) two wallets together to get a new
wallet with the combined total amount from both wallets.

Part Two:
Modify the code so that when we print the merged_wallet we receive a message
"Wallet with $80."
"""


class Wallet:
    def __init__(self, amount: int):
        self.amount = amount

    def __add__(self, other):
        if not isinstance(other, Wallet):
            return NotImplemented
        return Wallet(self.amount + other.amount)

    def __iadd__(self, other):
        self.amount += other
        return self

    def __str__(self):
        return f"Wallet with ${self.amount}"


if __name__ == "__main__":
    wallet1 = Wallet(50)
    wallet2 = Wallet(30)
    merged_wallet = wallet1 + wallet2
    assert merged_wallet.amount == 80
    assert str(merged_wallet) == f"Wallet with ${merged_wallet.amount}"
