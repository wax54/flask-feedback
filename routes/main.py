from flask import Blueprint, redirect, render_template, session, flash
from models.user import User
main = Blueprint('main_routes', __name__)


@main.route('')
def show_home_page():
    """Show The Home Page"""
    return redirect('/register')
