from flask import session

from mamom import db

from bson.objectid import ObjectId

from werkzeug.security import generate_password_hash, check_password_hash

class User():
    def __init__(self, id=0, name="", email="", password=""):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    def UserAlreadyExists(self):
        user = db.users.find_one({"email": self.email})

        if user:
            return True
        else:
            return False

    def updateUser(self):
        db.users.update({"_id": ObjectId(self.id)}, {
            "$set": {
                "name": self.name,
                "email": self.email
            }
        })

        return True

    def deleteUser(self):
        try:
            db.users.remove({"_id": ObjectId(self.id)})

            return True
        except:
            return False


    def getUserById(self, userId):
        try:
            user = db.users.find_one({"_id": ObjectId(userId)})

            return user;
        except Exception as e:
            return None


    def login(self):
        try:
            user = db.users.find_one({"email": self.email})

            if user:
                if check_password_hash(user["password"], self.password):
                    session["_id"] = str(user["_id"])
                    return True
            return False
        except Exception as e:
            return False

    def signUp(self):
        try:
            db.users.insert({
                "name": self.name,
                "email": self.email,
                "password": generate_password_hash(self.password)
            })

            return True
        except Exception as e:
            return False
