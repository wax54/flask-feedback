from flask import Blueprint, redirect, render_template, request, session, flash
from models.user import User, InputNotUniqueError
from forms.user_forms import UserRegistrationForm, UserLoginForm
authenticate = Blueprint('authenticate_routes', __name__)


@authenticate.route('register', methods=["GET", "POST"])
def show_home_page():
    """Show The Registration Page"""
    form = UserRegistrationForm()
    if form.validate_on_submit():
        try:
            user_info = get_user_credentials(request.form)
            new_user = User.register(**user_info)
            session['user'] = new_user.username
            flash("New Account Made! ", "success")
            return redirect(f'/users/{new_user.username}')
        except InputNotUniqueError as e:
            for err in e.errors:
                field = getattr(form, err)
                field.errors.append(f'This {err} is already in use!')
            return render_template('registration.html', form=form)
        except:
            flash("Something Weird happened...")
            return render_template('registration.html', form=form)

    else:
        return render_template('registration.html', form=form)



@authenticate.route('login', methods=["GET",  "POST"])
def show_login_page():
    form = UserLoginForm()
    if form.validate_on_submit():
        u_info = get_user_credentials(request.form)
        user = User.authenticate(**u_info)
        if user:
            session['user'] = user.username
            return redirect(f'/users/{user.username}')
        else:
            form.username.errors.append("EMAIL/PASSWORD INCORRECT")
            flash("Login failed!")
            return render_template('login.html', form=form)
    else:
        return render_template('login.html', form=form)


@authenticate.route('logout', methods=["GET",  "POST"])
def logout_user():
    session.pop('user', None)
    return redirect('/')

def get_user_credentials(form):
    """Returns a dict containing all the user related info from the form remove all empty fields"""
    d = {"username": form.get('username'),
         "password": form.get('password'),
         "email": form.get('email'),
         "first_name": form.get('first_name'),
         "last_name": form.get('last_name')
         }
    # get rid of any NULL values
    return {k:  v for k,  v in d.items() if v}
