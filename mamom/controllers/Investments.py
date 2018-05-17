from flask import render_template, request, jsonify, session, redirect

from mamom import app

@app.route("/mamom/investments/", methods=["GET"])
def redirect_investments():
    if "_id" in session:
        return render_template("investments/investments.html")

    return redirect("/mamom/login/")
