from flask import request, session
from mamom import app

from mamom.models.Goal import Goal
from mamom.models.User import User

@app.route("/mamom/goals/", methods=["POST"])
def create_goal():
    try:
        name = request.form.get("name")
        value = float(request.form.get("value"))
        deadline = request.form.get("deadline")
        user = User().getUserById(session["_id"])

        goal = Goal(name=name, balance=0, value=value, deadline=deadline, user=user)

        if(goal.createGoal()):
            return "OK", 200
        else:
            return "Error", 400
    except Exception as e:
        return "Error", 400
