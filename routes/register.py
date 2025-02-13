from flask import Blueprint, flash, redirect, render_template, url_for
from tables import User, db
from loginforms import RegisterForm
import hashlib

register_blueprint = Blueprint('register', __name__, template_folder='templates')
@register_blueprint.get('/register/')

def get_register():
    form = RegisterForm()
    return render_template('register.html', form=form)

@register_blueprint.post('/register/')
def post_register():
    form = RegisterForm()
    if form.validate():
        # check if there is already a user with this email address
        user = User.query.filter_by(email=form.email.data).first()
        # if the email address is free, create a new user and send to login
        if user is None:
            user = User(
                email=form.email.data, 
                password=form.password.data, 
                username=form.username.data, 
                avatar=hashlib.md5(form.email.data.encode("utf-8")).hexdigest(), # type:ignore
                bio = form.bio.data
            ) 
            db.session.add(user)
            db.session.commit()
            flash("Account created. Please login now.")
            return redirect(url_for('login.get_login'))
        else: # if the user  already exists
            # flash a warning message and redirect to get registration form
            flash('There is already an account with that email address')
            return redirect(url_for('register.get_register'))
    else: # if the form was invalid
        # flash error messages and redirect to get registration form again
        for field, error in form.errors.items():
            flash(f"{field}: {error}")
        return redirect(url_for('register.get_register'))