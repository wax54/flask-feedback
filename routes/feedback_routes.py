from flask import Blueprint, redirect, render_template, session, flash, request
from models.user import User
from models.feedback import Feedback

from forms.feedback_forms import FeedbackForm

feedback_routes = Blueprint("feedback_routes", __name__)


@feedback_routes.route('users/<username>/feedback/add', methods=["POST", "GET"])
def add_feedback(username):
    """
    GET /users/<username>/feedback/add
    Display a form to add feedback Make sure that only the
        user who is logged in can see this form

    POST /users/<username>/feedback/add
    Add a new piece of feedback and redirect
        to /users/<username> — Make sure that only
        the user who is logged in can successfully add feedback
    """
    curr_username = session.get('user')
    if curr_username:
        if curr_username == username:
            form = FeedbackForm()
            if form.validate_on_submit():
                title = form.title.data
                content = form.content.data
                comment = Feedback(title=title, content=content, username=username)
                comment.update_db()
                return redirect(f'/users/{username}')
            else:
                return render_template('add_feedback_form.html', form=form)
        else:
            flash("Eyes on Your own Profile", "warning")
            return redirect(f'/users/{curr_username}')
    else:
        flash("Please Log In", "danger")
        return redirect('/')


@feedback_routes.route('/feedback/<int:feedback_id>/update', methods=["POST", "GET"])
def handle_feedback_update(feedback_id):
    """
    GET /feedback/<feedback-id>/update
    Display a form to edit feedback — **Make sure that only the user who has written that feedback can see this form **
    POST /feedback/<feedback-id>/update
    Update a specific piece of feedback and redirect to /users/<username> — Make sure that only the user who has written that feedback can update it
    """
    curr_username = session.get('user')
    #someone is logged in
    if curr_username:
        #get the comment from the db
        comment = Feedback.get(feedback_id)
        #if the loggged in user is the same as the comment writer, then you can continue
        if curr_username == comment.username:
            #Most Common Path
            form = FeedbackForm(obj=comment)
            if form.validate_on_submit():
                comment.update_from_serial(request.form)
                return redirect(f'/users/{curr_username}')
            else:
                return render_template('edit_feedback_form.html', form=form)
        #outlier path
        else:
            flash('Eyes on your own work!', 'warning')
            return redirect(f'/users/{curr_username}')
    #outlier path
    else:
        flash('Please Log in')
        return redirect('/')


@feedback_routes.route('/feedback/<int:feedback_id>/delete', methods=["POST"])
def delete_feedback(feedback_id):
    """POST /feedback/<feedback-id>/delete
    Delete a specific piece of feedback and redirect to /users/<username> — 
    Make sure that only the user who has written that feedback can delete it
    """
    curr_username = session.get('user')
    if curr_username:
        comment = Feedback.get(feedback_id)
        if curr_username == comment.username:
            comment.delete()
            return redirect(f'/users/{curr_username}')
        else:
            return f"401! You're not authorized to do that {curr_username}!", 401
    else:
        flash("Log In Please.")
        return redirect('/')


def get_feedback_info(form):
    """Returns a dict containing all the feedback related 
        info from the form and remove all empty fields"""
    d = {
        "title": form.get('title'),
        "content": form.get('content'),
        "username": form.get('username')
    }
    # get rid of any NULL values
    return {k:  v for k,  v in d.items() if v}
