from flask import request, render_template, redirect, session

from mamom import app

from mamom.models.Account import Account

@app.route("/mamom/accounts/", methods=["POST"])
def create_account():
    try:
        name = request.form.get("name")
        balance = float(request.form.get("balance"))
        user = User().getUserById(session["_id"])

        account = Account(name=name, balance=balance, user=user)

        if account.createAccount():
            return "OK", 200
        else:
            return "Error", 400
    except Exception as e:
        return "Error", 400
