from flask import Flask, request, jsonify, render_template, Blueprint, flash, redirect, session, g, url_for, current_app
from .models import User, Table, Character, db
from .forms import SignUpForm, LoginForm    
from functools import wraps
import logging

views = Blueprint("views", __name__)

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first", 'alert')
            return redirect( url_for("views.index"))
    return wrap



@views.route("/")
def index():
    return render_template("index.jinja")

@views.route("/signup", methods = ["GET", "POST"])
def signup():
    form = SignUpForm()
    if request.method == 'GET':
        return render_template('signup.jinja', form = form)
    elif request.method == "POST":
        if form.validate_on_submit():
            current_app.logger.info(f"Cadastro do usuário com informações:\nName: {request.form['name']}\nEmail: {request.form['email']}")
            return redirect(url_for('views.homepage'))

@views.route("/login")
def login():
    return render_template("login.jinja")


@views.route("/homepage")
def homepage():
    return render_template('homepage.jinja')



@views.route("/tables")
def tables():
    return "Tables"

@views.route("/games")
def games():
    return "games"


@views.route("/private_games")
def private_games():
    return "private_games"


@views.route("/profile")
def profile():
    return "profile"
    

@views.route("/logout")
def logout():
    return "logout"
    