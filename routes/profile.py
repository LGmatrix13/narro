
from flask import Blueprint, render_template, redirect, url_for, abort
from flask_login import current_user
from tables import Post, User, db

profile_blueprint = Blueprint('profile', __name__, template_folder='templates')
@profile_blueprint.get("/profile/<int:id>/")
def get_profile(id: int):
    user = User.query.get(id)
    posts = Post.query.filter_by(user_id=id).all()

    if user == current_user:
        return redirect(url_for("account.get_account"))
    elif user is None:
        abort(code=404) 
    else:
        return render_template('profile.html', user=user, posts=posts)




    

