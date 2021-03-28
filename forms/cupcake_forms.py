"""forms involving the Pet Class"""
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, TextAreaField, SelectField, BooleanField
from wtforms.validators import InputRequired, URL, optional, NumberRange


class NewCupcakeForm(FlaskForm):
    flavor = StringField('Flavor', validators=[
        InputRequired(message='Flavor Cannot Be Blank!')])
    size = SelectField('Size', choices=[
        ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')])
    image = StringField('Photo URL', validators=[
        URL(message='Must be a valid URL'), optional()])
    rating = FloatField('Rating', validators=[NumberRange(
        min=0, max=10, message='Rating must be between 0 and 10')])
