from flask import Blueprint, redirect, render_template, session, flash
from models.user import User
user_routes = Blueprint("user_routes", __name__)


@user_routes.route('/<username>/delete', methods=["POST"])
def delete_user(username):
    """
    Remove the user from the database and make sure to also 
    delete all of their feedback. Clear any user information 
    in the session and redirect to / . Make sure that only the 
    user who is logged in can successfully delete their account
    """
    if 'user' in session:
        if session['user'] == username:
            User.get(username).delete()
            session.pop('user', None)
            return redirect('/')

    flash("Don't Mess Around Bub.")
    return redirect('/')
