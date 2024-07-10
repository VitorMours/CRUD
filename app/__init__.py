from flask import Flask, jsonify, request, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .views import views
from .auth import auth
#from .utils import create_tables

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'cuscuz com ovo' 

    # Registering Blueprints
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
        
    return app


if __name__ == "__init__":
    app = create_app()
    app.run()
