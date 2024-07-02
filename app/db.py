from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from flask import current_app
from .model import User, Base


def create_tables(engine):
    Base.metadata.create_all(engine)



# TODO: Function to receive data, and sendo to the database to save 



# TODO: Function to search for data my an specific parameters 



# TODO: 



# TODO: 



# TODO: 



# TODO: 



# TODO: 



# TODO: 




