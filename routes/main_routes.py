from flask import Blueprint, redirect, render_template, session, flash
from models.user import User
main_routes = Blueprint('main_routes', __name__)


@main_routes.route('')
def show_home_page():
    """Show The Home Page"""
    return redirect('/register')
