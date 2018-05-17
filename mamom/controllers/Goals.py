from flask import request, session, render_template
from mamom import app

from bson.objectid import ObjectId

from mamom.models.Goal import Goal
from mamom.models.User import User

@app.route("/mamom/goals/<goal_id>/balance/", methods=["PUT"])
def deposit_value_in_goal(goal_id):
    value = float(request.form.get("value"))

    goal = Goal(id=goal_id, value=value)

    if goal.updateBalance():
        return "OK", 200
    else:
        return "Error", 400

@app.route("/mamom/goals/<goal_id>/", methods=["GET"])
def get_goal(goal_id):
    try:
        goal = Goal().getGoalById(goal_id)

        if goal["user"]["_id"] == session["_id"]:
            return render_template("errors/403.html")
        else:
            return render_template("goals/goals.html", goal=goal)
    except:
        return render_template("errors/403.html")


@app.route("/mamom/goals/<goal_id>/", methods=["DELETE"])
def delete_goal(goal_id):
    try:
        goal = Goal(id=goal_id)

        if goal.deleteGoal():
            return "OK", 200
        else:
            return "Error", 400
    except Exception as e:
        return "Error", 400

@app.route("/mamom/goals/<goal_id>/", methods=["PUT"])
def update_goal(goal_id):
    try:
        name = request.form.get("name")
        value = float(request.form.get("value"))
        deadline = request.form.get("deadline")

        goal = Goal(id=goal_id, value=value, name=name, deadline=deadline)

        if goal.updateGoal():
            return "OK", 200
        else:
            return "Error", 400
    except Exception as e:
        return "Error", 400

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
