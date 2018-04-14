from flask import request
from mamom import app

from mamom.models.Goal import Goal

@app.route("/mamom/goals/", methods=["POST"])
def create_goal():
    name = request.form.get("name")
    balance = request.form.get("balance")

    goal = Goal(name=name, balance=balance)

    if(goal.createGoal()):
        return "OK", 200
    else:
        return "Error", 400
