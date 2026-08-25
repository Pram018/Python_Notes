class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.score = 0

    def add_score(self, points):
        self.score += points

terry = Person("Pramodh", "S")
fred = Person("Prathap", "S")

print(terry.first, terry.last)
print(fred.first, fred.last)

print(fred.score)
fred.add_score(10)
print(fred.score)