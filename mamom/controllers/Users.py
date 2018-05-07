from flask import session, render_template, redirect, request

from mamom import app

from mamom.models.User import User

@app.route("/mamom/users/", methods=["GET"])
def redirect_to_edit_user():
    user = User().getUserById(session["_id"])

    return render_template("users/users.html", user=user)


@app.route("/mamom/users/<user_id>/", methods=["PUT"])
def update_user(user_id):
    try:
        name = request.form.get("name")
        email = request.form.get("email")

        user = User(id=user_id, name=name, email=email)

        if user.UserAlreadyExists():
            u = user.getUserById(user_id)
            if u["email"] != email:
                return "Este e-mail já está sendo usado por outro usuário!", 400

        user.updateUser()

        return "OK", 200
    except:
        return "Error", 400

@app.route("/mamom/users/", methods=["DELETE"])
def delete_user():
    try:
        user = User(id=session["_id"])

        if user.deleteUser():
            return redirect("/mamom/logout/")
        else:
            return "Error", 400
    except Exception as e:
        return "Error", 400

@app.route("/mamom/logout/", methods=["GET"])
def logout():
    try:
        session.pop("_id", None)

        return redirect("/mamom/login/")
    except Exception as e:
        return "Houve um problema ao realizar logout!", 400

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

        if user.UserAlreadyExists():
            return render_template("signup/signup.html", error="Este e-mail já está sendo usado por outro usuário!")

        user.signUp()

        return redirect("/mamom/login/")
    except Exception as e:
        return "Error", 400
