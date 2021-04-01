"""Flask app for Cupcakes"""
from flask import Flask, Blueprint
from flask_debugtoolbar import DebugToolbarExtension
from secrets import FLASK_SECRET_KEY
from config import DB_NAME, DB_ECHO

from models import connect_db

from routes.main_routes import main_routes
from routes.authenticate_routes import authenticate_routes
from routes.user_routes import user_routes
from routes.feedback_routes import feedback_routes

app = Flask(__name__)

app.config['SECRET_KEY'] = FLASK_SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql:///{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = DB_ECHO
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)

toolbar = DebugToolbarExtension(app)

app.register_blueprint(main_routes, url_prefix='/')
app.register_blueprint(authenticate_routes, url_prefix='/')
app.register_blueprint(user_routes, url_prefix='/users')
app.register_blueprint(feedback_routes, url_prefix='/')
