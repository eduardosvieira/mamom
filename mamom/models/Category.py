from mamom import db

class Category():
    def __init__(self, id=0, name=""):
        self.id = id
        self.name = name

    def getAllCategories(self):
        try:
            categories = db.categories.find({})

            return categories
        except Exception as e:
            return None
