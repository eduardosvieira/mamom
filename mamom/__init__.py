from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

app.config["SECRET_KEY"] = "jkjaks7iwiou98w71w797"

client = MongoClient("mongodb://localhost:27017/")

db = client.mamomdb


from mamom.controllers import Default
from mamom.controllers import Users
