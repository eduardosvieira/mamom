from flask import render_template, request, jsonify

from mamom import app

@app.route("/mamom/investments/", methods=["GET"])
def redirect_investments():
    return render_template("investments/investments.html")
