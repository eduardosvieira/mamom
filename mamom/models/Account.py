from bson.objectid import ObjectId

from mamom import db

class Account():
    def __init__(self, id=0, name="", balance=0, user=None):
        self.id = id
        self.name = name
        self.balance = balance
        self.user = user

    def getAccountById(self, accountId):
        try:
            account = db.accounts.find({"_id": ObjectId(accountId)})

            return account
        except Exception as e:
            return None


    def getAllAccountsByUserId(self, userId):
        try:
            accounts = db.accounts.find({"user._id": ObjectId(userId)})

            return accounts
        except Exception as e:
            return None

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
