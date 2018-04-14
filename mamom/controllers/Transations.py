from flask import request
from mamom import app

from mamom.models.Category import Category
from mamom.models.Account import Account
from mamom.models.Transation import Transation


@app.route("/mamom/transations/", methods=["POST"])
def create_transation():
    INCOMES = ["Remuneração", "Rendimento"]
    EXPENSES = ["Transporte", "Lazer", "Alimentação"]


    account_id = request.form.get("accountId")
    account = Account().getAccountById(account_id)

    category_id = request.form.get("categoryId")
    category = Category().getCategoryById(category_id)

    name = request.form.get("name")
    value = float(request.form.get("value"))
    createdAt = request.form.get("createdAt")

    transation = Transation(name=name, value=value, createdAt=createdAt, category=category, account=account)

    if(transation.createTransation()):
        if transation.category["name"] in INCOMES:
            Account().credit(transation=transation)
        else:
            Account().debit(transation=transation)

        return "OK", 200
    else:
        return "Error", 400
