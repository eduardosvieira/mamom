from flask import session, render_template, redirect

from mamom import app

from mamom.models.Account import Account
from mamom.models.Transation import Transation
from mamom.models.Goal import Goal


@app.route("/mamom/", methods=["GET"])
def index():
    if "_id" in session:
        accounts = Account().getAllAccountsByUserId(session["_id"])
        transations = Transation().getAllTransationsByUserId(session["_id"])
        goals = Goal().getAllGoalsByUserId(session["_id"])

        return render_template("index.html", accounts=accounts, transations=transations, goals=goals)
    else:
        return redirect("/mamom/login/")
