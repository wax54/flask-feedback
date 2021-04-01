from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired


class FeedbackForm(FlaskForm):
    title = StringField('title', validators=[InputRequired()])
    content = StringField('content', validators=[InputRequired()])
