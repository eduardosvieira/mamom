from flask import jsonify
from mamom import app

from mamom.models.Category import Category

@app.route("/mamom/categories/", methods=["GET"])
def get_all_categories():
    try:
        result = Category().getAllCategories()

        categories = []
        for c in result:
            categories.append({"name": c["name"], "_id": str(c["_id"])})

        return jsonify(categories)
    except Exception as e:
        return "Error", 400
