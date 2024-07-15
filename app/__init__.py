from flask import Flask, jsonify, request, Blueprint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists
from flask_migrate import Migrate
from .views import views
from .auth import auth
from .models import db, migrate, User, Table, Character
#from .utils import create_tables
import logging

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'cuscuz com ovo' 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rune_tables.sqlite3'
    
    # Setting the application logging handler 
    app.logger.setLevel(logging.INFO)
    handler = logging.FileHandler('logger.log')
    app.logger.addHandler(handler)


    # Registering Blueprints
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    # Extensions
    db.init_app(app)
    migrate.init_app(app, db)


    with app.app_context():
        db.create_all()


    return app

if __name__ == "__init__":
    app = create_app()
    app.run()
