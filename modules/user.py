from flask import Blueprint, render_template 

user_blueprint = Blueprint("user", __name__)

@user_blueprint.route("/register")
def register():
    return render_template("register.html")


@user_blueprint.route("/login")
def login():
    
    return render_template("login.html")




