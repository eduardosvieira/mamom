from bson.objectid import ObjectId

from mamom import db

class Transation():
    def __init__(self, id=0, name="", createdAt="", category=None, account=None, value=0):
        self.id = id
        self.name = name
        self.createdAt = createdAt
        self.category = category
        self.account = account
        self.value = value

    def getAllTransationsByAccountId(self, accountId):
        try:
            transations = db.transations.find({"account._id": ObjectId(accountId)})

            return transations
        except Exception as e:
            return None

    def createTransation(self):
        try:
            db.transations.insert({
                "name": self.name,
                "createdAt": self.createdAt,
                "category": self.category,
                "account": self.account,
                "value": self.value
            })

            return True
        except Exception as e:
            return False
