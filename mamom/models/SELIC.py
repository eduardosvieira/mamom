from mamom.models.Investment import Investment

class SELIC():
    def __init__(self, value=0, name=""):
        self.value = value
        self.name = name
        self.rate = 0.065

    def calculate(self):
        return self.value + self.value * self.rate
