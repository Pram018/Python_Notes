class Trade:
    def __init__(self, price: int, volume: int):
        self.price = price
        self.volume = volume

    def is_buy(self):
        return self.volume > 0

    def __repr__(self) -> str:
        # return "Teade(" + str(self.volume) + "@ $" + str(self.price) + ")"

        # alternate method using f_strings
        return f"Trade({self.volume} @ ${self.price})"

trade = Trade(price = 4, volume = 2)
print(trade)
