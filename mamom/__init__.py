from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

app.config["SECRET_KEY"] = "jkjaks7iwiou98w71w797"

client = MongoClient("mongodb://localhost:27017/")

db = client.mamomdb


from mamom.controllers import Default
from mamom.controllers import Users

from mamom.models.User import User
from mamom.models.Account import Account
from mamom.models.Transation import Transation
from mamom.models.Category import Category
from mamom.models.Income import Income
