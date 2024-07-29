from flask import Flask, request, jsonify, render_template, Blueprint, flash, redirect, session, g, url_for, current_app
from sqlalchemy.sql import exists
from .models import User, Table, Character, db
from .forms import SignUpForm, LoginForm    
from functools import wraps
import logging
from datetime import datetime, date, time
from .utils import Log
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
        
        # TODO: fazer com que envie uma mensagem dizendo que o osuuário ja existe
        #flash("Esse usuário ja existe dentro da base de dados")
        #return redirect(url_for('views.index'))    
        if form.validate_on_submit():
            if User.query.filter_by(email=request.form["email"]).first() is None:
                Log.cadastro_de_usuario(request)

                user = User(
                    name =request.form['name'],
                    email=request.form['email'],
                    password=request.form['password']
                )
                db.session.add(user)
                db.session.commit()


                return redirect(url_for('views.homepage'))
            
            else:
                user = User.query.filter_by(email=request.form['email']).first()

            flash("As credenciais já foram cadastradas no site")
            return redirect(url_for('views.index'))
        


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


@views.route("/profile/")
def profile():
    if request.method == "GET":
        return render_template("profile.jinja")
    

@views.route("/logout")
def logout():
    return "logout"
    
