from flask import session, render_template, redirect

from mamom import app

@app.route("/mamom/", methods=["GET"])
def index():
    return render_template("index.html")
