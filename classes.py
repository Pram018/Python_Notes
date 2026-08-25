class Person:
    def __init__(self, first: str, last: str):
        self.first = first
        self.last = last
        self.score = 0

    def add_score(self, points: int):
        self.score += points

    # In __repr__ method we are expecting to always return a str
    def __repr__(self) -> str:
        return self.first + " " + self.last


terry = Person("Pramodh", "S")
fred = Person("Prathap", "S")

print(terry.first, terry.last)
print(fred.first, fred.last)

print(fred.score)
fred.add_score(10)
print(fred.score)

print(terry)