from flask import Flask, jsonify, request, Blueprint
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists
from .model import Base 
from .views import views
from .auth import auth
from .db import create_tables
    
def create_database(app):
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    
    with engine.connect() as connection:
        pass

    return engine

def run_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'cuscuz com ovo' 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.sqlite3'

    # Registering Blueprints
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
        

    # Extra configurations
    db = create_database(app)
    
    create_tables(db)



    app.run(debug=True)

