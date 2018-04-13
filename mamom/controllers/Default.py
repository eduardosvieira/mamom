from flask import session, render_template, redirect

from mamom import app

@app.route("/mamom/", methods=["GET"])
def index():
    if "_id" in session:
        return render_template("index.html")
    else:
        return redirect("/mamom/login/")
