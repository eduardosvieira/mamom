from flask import render_template, request, jsonify

from mamom import app

from mamom.models.Savings import Savings
from mamom.models.SELIC import SELIC

@app.route("/mamom/investments/", methods=["GET"])
def redirect_investments():
    return render_template("investments/investments.html")


@app.route("/mamom/investments/", methods=["POST"])
def invest():
    value = float(request.form.get("value"))

    investments = []

    savings = Savings(value=value, name="Cardeneta de Poupança")
    selic = SELIC(value=value, name="Tesouro SELIC")

    investments.append({"name": savings.name, "value": savings.calculate() })
    investments.append({"name": selic.name, "value": selic.calculate() })

    return jsonify(investments)
