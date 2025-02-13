"""
INSTALLING REQUIRED PACKAGES
Run the following command to install all required packages.
python -m pip install --upgrade pip flask-login
"""

###############################################################################
# Imports
###############################################################################
from __future__ import annotations
import os
from flask import Flask
from flask_login import LoginManager
from tables import User, db
from routes.login import login_blueprint
from routes.feed import feed_blueprint
from routes.logout import logout_blueprint
from routes.profile import profile_blueprint
from routes.register import register_blueprint
from routes.story import story_blueprint
from routes.post import post_blueprint
from routes.account import account_blueprint
###############################################################################
# Basic Configuration
###############################################################################

# Identify necessary files
scriptdir = os.path.dirname(os.path.abspath(__file__))
dbfile = os.path.join(scriptdir, "db.sqlite3")

# Configure the Flask Application
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SECRET_KEY'] = 'hereisamaybeslightlybetterkey?'
app.secret_key = 'hereisamaybeslightlybetterkey?'
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{dbfile}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
# Prepare and connect the LoginManager to this app
login_manager = LoginManager()
login_manager.init_app(app)
# function name of the route that has the login form (so it can redirect users)
login_manager.login_view = 'login.get_login' # type: ignore

# function that takes a user id
@login_manager.user_loader
def load_user(id: int) -> User:
    return User.query.get(int(id)) # type: ignore


with app.app_context():
    db.drop_all()
    db.create_all() 


#register blueprints for all route handlers
app.register_blueprint(login_blueprint)
app.register_blueprint(register_blueprint)
app.register_blueprint(feed_blueprint)
app.register_blueprint(logout_blueprint)
app.register_blueprint(profile_blueprint)
app.register_blueprint(story_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(account_blueprint)
