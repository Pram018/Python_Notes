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


class TradeTracker:
    def __init__(self):
        self.trades = []

    def add_trade(self, trade: Trade):
        self.trades.append(trade)

    def get_buy_trades(self):
        buy_trades = []
        for trade in self.trades:
            if trade.is_buy():
                print(f"{trade} is a buy")
                buy_trades.append(trade)
            else:
                print(trade, "is not a buy")
        return buy_trades
    
    def get_average_traded_price(self):
        total = 0
        for trade in self.trades:
            print(f"Price of trade: {trade.price}")
            total += trade.price
        return total / len(self.trades)

tracker = TradeTracker()
tracker.add_trade(Trade(7, 4))
tracker.add_trade(Trade(10, -3))
print(tracker.get_buy_trades())
print(tracker.get_average_traded_price())
print(tracker.trades)