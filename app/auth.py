from flask import Flask, render_template, request, Blueprint

auth = Blueprint('auth', __name__)


@auth.route("/")
def login():
    pass