from mamom.models.Investment import Investment

class Savings():
    def __init__(self, value=0, name=""):
        self.value = value
        self.name = name
        self.rate = 0.05

    def calculate(self):
        return self.value + self.value * self.rate
