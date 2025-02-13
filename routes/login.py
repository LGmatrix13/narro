from flask import Blueprint, redirect, render_template, request, url_for, flash, session
from flask_login import login_user
from loginforms import LoginForm
from tables import User

login_blueprint = Blueprint('login', __name__, template_folder='templates')
@login_blueprint.get('/login/')
def get_login():
    form = LoginForm()
    return render_template('login.html', form=form)

@login_blueprint.post('/login/')
def post_login():
    form = LoginForm()
    if form.validate():
        # try to get the user associated with this email address
        user = User.query.filter_by(email=form.email.data).first()
        # if this user exists and the password matches
        if user is not None and user.verify_password(form.password.data):
            # log this user in through the login_manager
            login_user(user, remember=True)
            session["user_id"] = user.id
            print(session["user_id"])
            # redirect the user to the page they wanted or the home page
            return redirect(url_for("account.get_account_posts"))
        else: # if the user does not exist or the password is incorrect
            # flash an error message and redirect to login form
            flash('Invalid email address or password')
            return redirect(url_for('login.get_login'))
    else: # if the form was invalid
        # flash error messages and redirect to get login form again
        for field, error in form.errors.items():
            flash(f"{field}: {error}")
        return redirect(url_for('login.get_login'))
