from flask import Flask 
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField
from wtforms.validators import DataRequired

class SignUpForm(FlaskForm):
       name = StringField("name", validators=[DataRequired()], render_kw={"placeholder":"Your name"})
       email = EmailField("email", validators=[DataRequired()], render_kw={"placeholder":"email"})
       password = PasswordField("password", validators=[DataRequired()], render_kw={"placeholder":"set a password"})
       check_password = PasswordField("check your password", validators=[DataRequired()], render_kw={"placeholder":"type your password again"})

class LoginForm(FlaskForm):
       credential = StringField("credentials", validators=[DataRequired()], render_kw={"placeholder":"Enter your credentials here, nickname or email"})
       password = PasswordField("password", validators=[DataRequired()], render_kw={"placeholder":"Enter your password"})
