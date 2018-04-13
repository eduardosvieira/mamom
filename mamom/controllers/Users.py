from flask import session, render_template, redirect, request

from mamom import app

from mamom.models.User import User

@app.route("/mamom/login/", methods=["GET"])
def index_login():
    if "_id" in session:
        return redirect("/mamom/")
    else:
        return render_template("login/login.html")


@app.route("/mamom/login/", methods=["POST"])
def login():
    try:
        email = request.form.get("email")
        password = request.form.get("password")

        user = User(email=email, password=password)

        if user.login():
            return redirect("/mamom/")
        else:
            return render_template("login/login.html", error="Usuário ou senha estão incorretos!")

    except Exception as e:
        return "Error", 400



@app.route("/mamom/signup/", methods=["GET"])
def index_signup():
    if "_id" in session:
        return redirect("/mamom/")
    else:
        return render_template("signup/signup.html")


@app.route("/mamom/signup/", methods=["POST"])
def signup():
    try:
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        user = User(name=name, email=email, password=password)

        user.signUp()

        return redirect("/mamom/login/")
    except Exception as e:
        return "Error", 400
