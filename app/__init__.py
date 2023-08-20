from flask import Flask, jsonify, request, Blueprint
from .views import views
from .auth import auth


def run_app():
    app = Flask(__name__)
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    app.run(debug=True)

