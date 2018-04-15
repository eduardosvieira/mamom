
from bson.objectid import ObjectId
from mamom import db

class Goal():
    def __init__(self, name="", balance=0, value=0, deadline="", user=None):
        self.name = name
        self.balance = balance
        self.value = value
        self.deadline = deadline
        self.user = user


    def createGoal(self):
        try:
            db.goals.insert({
                "name": self.name,
                "balance": self.balance,
                "value": self.value,
                "deadline": self.deadline,
                "user": self.user
            })

            return True
        except Exception as e:
            return False


    def getAllGoalsByUserId(self, userId):
        try:
            goals = db.goals.find({"user._id": ObjectId(userId)})

            return goals
        except Exception as e:
            return None
