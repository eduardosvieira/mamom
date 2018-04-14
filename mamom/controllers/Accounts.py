from flask import request, render_template, redirect, session

from mamom import app, db

from mamom.models.Account import Account
from mamom.models.User import User
from mamom.models.Transation import Transation

@app.route("/mamom/accounts/<account_id>/", methods=["GET"])
def get_account(account_id):
    account = Account().getAccountById(account_id)

    transations = Transation().getAllTransationsByAccountId(account_id)

    return render_template("accounts/accounts.html", account=account, transations=transations)


@app.route("/mamom/accounts/", methods=["POST"])
def create_account():
    try:
        name = request.form.get("name")
        balance = float(request.form.get("balance"))
        user = User().getUserById(session["_id"])

        account = Account(name=name, balance=balance, user=user)

        if(account.createAccount()):
            return "OK", 200
        else:
            return "Error", 400
    except Exception as e:
        return "Error", 300
