from bson.objectid import ObjectId

from mamom import db

class Category():
    def __init__(self, id=0, name=""):
        self.id = id
        self.name = name

    def getCategoryById(self, categoryId):
        try:
            category = db.categories.find_one({"_id":ObjectId(categoryId)})

            return category
        except Exception as e:
            return None

    def getAllCategories(self):
        try:
            categories = db.categories.find({})

            return categories
        except Exception as e:
            return None
