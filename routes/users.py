from flask import Blueprint, redirect, render_template, session, flash, Response
from models.user import User
user_routes = Blueprint("user_routes", __name__)


@user_routes.route('')
def show_all_users():
    if "user" not in session:
        flash("Please Log In", "warning")
        return redirect('/login')
    else:
        users = User.get_all()
        return render_template('list_users.html', users=users)


@user_routes.route('/<username>')
def show_user_home_page(username):
    if "user" not in session:
        flash("Please Log In", "warning")
        return redirect('/login')
    else:
        curr_username = session['user']
        user = User.get(username)
        if curr_username == username:
            return render_template('user_profile.html', user=user)
        else:
            return (f'401! You Are Not Authorized To View This Profile! <a href="/users/{curr_username}">Go Home</a> {curr_username}', 401)


@user_routes.route('/<username>/delete', methods=["POST"])
def delete_user(username):
    """
    Remove the user from the database and make sure to also 
    delete all of their feedback. Clear any user information 
    in the session and redirect to / . Make sure that only the 
    user who is logged in can successfully delete their account
    """
    if 'user' not in session:
        flash("Please Log In", "warning")
        return redirect('/')
    else:
        curr_username = session['user']
        if curr_username == username:
            User.get(username).delete()
            session.pop('user', None)
            return redirect('/')
        else:
            flash("Watch It Bub.", "warning")
            return redirect(f'/users/{curr_username}')
