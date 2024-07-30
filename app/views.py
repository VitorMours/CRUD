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
            flash("You need to login first", category='alert')
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
    
            if User.query.filter_by(email=request.form["email"]).first() is None:
                Log.cadastro_de_usuario(request)

                user = User(
                    name =request.form['name'],
                    email=request.form['email'],
                    password=request.form['password']
                )
                db.session.add(user)
                db.session.commit()
                    
                session['logged_in'] = True
                return redirect(url_for('views.homepage'))
            
            else:
                user = User.query.filter_by(email=request.form['email']).first()

            flash("As credenciais já foram cadastradas no site", category="alert")
            return redirect(url_for('views.index'))
        


@views.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "GET":
        return render_template("login.jinja", form=form)
    
    else:
        if form.validate_on_submit():
            credential = request.form["credential"]
            password = request.form["password"]
            session['logged_in'] = True
            if (user := User.query.filter_by(email=credential).first()) is not None:
                print(user.email)
                print(user.password)
                if user.password == password and user.email == credential:
                    return redirect(url_for("views.homepage"))

                else:
                    flash("Não existe nenhum usuário com essas credenciais", category="info")
                    return redirect(url_for("views.login"))

@views.route("/homepage")
@login_required
def homepage():
    print(session['logged_in'])
    return render_template('homepage.jinja')



@views.route("/tables")
@login_required 
def tables():
    return "Tables"

@views.route("/games")
@login_required
def games():
    return "games"


@views.route("/private_games")
@login_required
def private_games():
    return "private_games"


@views.route("/profile")
@login_required
def profile():
    if request.method == "GET":
        return render_template("profile.jinja")
    

@views.route("/logout")
@login_required
def logout():
    session.pop("logged_in", None)
    return redirect(url_for("views.index"))
    
