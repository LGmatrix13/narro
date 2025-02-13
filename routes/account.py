
from flask import Blueprint, render_template, session, flash, redirect, url_for
from flask_login import current_user, login_required, logout_user
from tables import Post, Liked

account_blueprint = Blueprint('account', __name__, template_folder='templates')
@account_blueprint.get("/account/")
@login_required
def get_account_posts():
    posts = Post.query.filter_by(user_id = session["user_id"]).order_by(Post.id.desc()).all()
    # liked_posts = Post.query.join(Liked, Liked.post_id == Post.id).filter_by(user_id = session["user_id"]).order_by(Post.id.desc()).all()
    return render_template('account_posts.html', posts = posts, active = "posts")

@account_blueprint.get('/account/liked-posts')
@login_required
def get_account_liked_posts():
    liked_posts = Post.query.join(Liked, Liked.post_id == Post.id).filter_by(user_id = session["user_id"]).order_by(Post.id.desc()).all()
    return render_template('account_liked_posts.html', liked_posts = liked_posts, active = "liked-posts")

