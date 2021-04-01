from flask import Blueprint, redirect, render_template, session, flash
from models.user import User
main = Blueprint('main_routes', __name__)


@main.route('')
def show_home_page():
    """Show The Home Page"""
    return redirect('/register')


@main.route('users/<username>')
def show_user_home_page(username):
    if "user" not in session:
        flash("Please Log In", "warning")
        return redirect('/login')
    else:
        curr_user = session['user']
        if username == curr_user:
            user = User.get(username)
            return render_template('user_profile.html', user=user)
        else:
            flash('Look At Your Own Damn Name!', 'warning')
            return redirect(f'/users/{curr_user}')
