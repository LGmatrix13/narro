from flask import Blueprint, render_template, redirect, url_for
from tables import Post, User, db
import random

feed_blueprint = Blueprint('feed', __name__, template_folder='templates')
@feed_blueprint.get("/")
def get_feed(): 
    posts = db.session.query(Post, User).join(User, Post.user_id == User.id).order_by(Post.id.desc()).limit(15).all()
    return render_template('feed.html', posts = posts)

@feed_blueprint.get("/lucky/")
def get_lucky():
    posts = Post.query.all()
    if len(posts) > 0:
        random_post = random.choice(posts)
        return redirect(location=f"/post/{random_post.id}")
    else:
        return redirect(url_for("feed.get_feed"))

