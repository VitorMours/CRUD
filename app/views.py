from flask import Flask, request, jsonify, render_template, Blueprint, flash, redirect, session, g, url_for, current_app
from functools import wraps
from .forms import SignUpForm, LoginForm    
from .models import User, Table, Character, db



views = Blueprint("views", __name__)

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first")
            return redirect( url_for("views.index"))
    return wrap



@views.get("/")
def index():
    return render_template("index.jinja")

@views.route("/signup", methods = ["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        user = User(
                name = request.form['name'],
                email = request.form['email'],
                password = request.form['password'], 
                )

        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for("views.homepage"))

    if request.method == "GET":
        form = SignUpForm()
        return render_template("signup.jinja", form=form)


@views.route("/login")
def login():
    return render_template("login.jinja")





@views.route("/homepage/")
def homepage():
    return "Homepage"

