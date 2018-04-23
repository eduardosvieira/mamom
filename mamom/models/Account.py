from bson.objectid import ObjectId

from mamom import db

class Account():
    def __init__(self, id=0, name="", balance=0, user=None):
        self.id = id
        self.name = name
        self.balance = balance
        self.user = user

    def getTotalBalance(self, accounts):
        sum = 0
        for account in accounts:
            sum += account["balance"]

        return sum


    def getTotalExpenses(self, transations=None):
        try:
            sum = 0

            for transation in transations:
                if transation["value"] < 0:
                    sum += transation["value"]

            return sum
        except:
            return 0

    def getTotalIncomes(self, transations=None):
        try:
            sum = 0

            for transation in transations:
                if transation["value"] > 0:
                    sum += transation["value"]

            return sum
        except:
            return 0

    def deleteAccount(self):
        try:
            db.accounts.remove({"_id": ObjectId(self.id)})

            return True
        except:
            return False

    def updateAccount(self):
        try:
            db.accounts.update({"_id": ObjectId(self.id)}, {"$set": {"name": self.name}})

            return True
        except:
            return False

    def credit(self, transation=None):
        try:
            db.accounts.update({"_id": ObjectId(transation.account["_id"])},
            {"$inc": {"balance": transation.value}})

            return True
        except Exception as e:
            return False

    def debit(self, transation=None):
        try:
            db.accounts.update({"_id": ObjectId(transation.account["_id"])},
            {"$inc": {"balance": -transation.value}})

            return True
        except Exception as e:
            return False

    def getAccountById(self, accountId):
        try:
            account = db.accounts.find_one({"_id": ObjectId(accountId)})

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
