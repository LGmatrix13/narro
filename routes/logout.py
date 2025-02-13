from flask import Blueprint, redirect, url_for, flash, session
from flask_login import logout_user


logout_blueprint = Blueprint('logout', __name__, template_folder='templates')
@logout_blueprint.get('/logout/')
def get_logout():
    if session.get('user_id') is not None:
        del session["user_id"]
        
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('login.get_login'))