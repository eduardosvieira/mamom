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

        totalExpenses = Account().getTotalExpenses(transations)
        totalIncomes = Account().getTotalIncomes(transations)
        total = Account().getTotalBalance(accounts)

        sum = 0
        for account in accounts:
            sum += account["balance"]

        total = sum

        return render_template("index.html", accounts=accounts, transations=transations, goals=goals, totalExpenses=totalExpenses, totalIncomes=totalIncomes, total=total)
    else:
        return redirect("/mamom/login/")
