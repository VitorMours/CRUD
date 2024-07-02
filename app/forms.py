from flask import Flask 
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField
from wtforms.validators import DataRequired

class SignUpForm(FlaskForm):
       name = StringField("name")
       
       email = EmailField("email", validators=[DataRequired()])

       password = PasswordField("password")


