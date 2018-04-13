from flask import session

from mamom import db

from werkzeug.security import generate_password_hash, check_password_hash

class User():
    def __init__(self, id=0, name="", email="", password=""):
        self.id = id
        self.name = name
        self.email = email
        self.password = password


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
