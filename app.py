"""Flask app for Cupcakes"""
from flask import Flask, Blueprint
from flask_debugtoolbar import DebugToolbarExtension
from secrets import FLASK_SECRET_KEY
from config import DB_NAME, DB_ECHO

from models import connect_db
from models.user import User

from routes.main import main
from routes.authenticate import authenticate


app = Flask(__name__)

app.config['SECRET_KEY'] = FLASK_SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql:///{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = DB_ECHO
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)

toolbar = DebugToolbarExtension(app)

app.register_blueprint(main, url_prefix='/')
app.register_blueprint(authenticate, url_prefix='/')
