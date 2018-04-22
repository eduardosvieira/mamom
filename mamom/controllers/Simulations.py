from flask import render_template

from mamom import app

@app.route("/mamom/simulations/", methods=["GET"])
def redirect_simulations():
    return render_template("simulations/simulations.html")
