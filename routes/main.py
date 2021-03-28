from flask import Blueprint, render_template, request

main = Blueprint('main_routes', __name__)


@main.route('')
def show_home_page():
    """Show The Home Page"""
    return render_template('home.html')
