from flask import render_template

from mamom import app

@app.route("/mamom/investments/", methods=["GET"])
def redirect_investments():
    return render_template("investments/investments.html")
