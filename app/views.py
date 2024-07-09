from flask import Flask, request, jsonify, render_template, Blueprint, flash, redirect, session, g, url_for
from functools import wraps
from .forms import SignUpForm    

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



@views.route("/")
def index():
    return render_template("index.jinja")

@views.route("/signup")
@login_required
def signup():

    form = SignUpForm()

    return render_template("signup.jinja", form=form)

@views.route("/login")
def login():
    return render_template("login.jinja")



