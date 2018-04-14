
from mamom import db

class Account():
    def __init__(self, id=0, name="", balance=0, user=None):
        self.id = id
        self.name = name
        self.balance = balance
        self.user = user

    def createAccount(self):
        try:
            db.accounts.insert({
                "name": self.name,
                "balance": self.balance,
                "user": self.user
            })

            return True
        except Exception as e:
            return False
