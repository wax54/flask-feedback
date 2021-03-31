"""forms involving the Pet Class"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, URL, optional, NumberRange, Email

class UserRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])
    email = StringField('Email', validators=[ Email('Must Be a Valid Email')])
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])


class UserLoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])
