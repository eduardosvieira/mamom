from flask import session, render_template, redirect

from mamom import app

from mamom.models.Account import Account

@app.route("/mamom/", methods=["GET"])
def index():
    if "_id" in session:
        accounts = Account().getAllAccountsByUserId(session["_id"])

        return render_template("index.html", accounts=accounts)
    else:
        return redirect("/mamom/login/")
