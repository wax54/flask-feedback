from flask import Blueprint, redirect, render_template, request
from models.user import User
from forms.user_forms import UserRegistrationForm
authenticate = Blueprint('authenticate_routes', __name__)


@authenticate.route('register', methods=["GET", "POST"])
def show_home_page():
    """Show The Registration Page"""
    form = UserRegistrationForm()
    if form.validate_on_submit():
        new_user = User()
        if new_user.update_from_serial(request.form):
            return redirect('/secret')
    return render_template('registration.html', form=form)
#TODO
#if username or email are not unique, convey to user the error


@authenticate.route('secret', methods=["GET"])
def show_secret_page():
    return "hello"
