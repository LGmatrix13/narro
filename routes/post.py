
from flask import Blueprint, abort, render_template, render_template, session, jsonify

from tables import Post, User, db, Liked
from flask_login import login_required

post_blueprint = Blueprint('post', __name__, template_folder='templates')
@post_blueprint.get("/post/<int:id>/")
def get_post(id: int): 
    post = db.session.query(Post, User).join(User, Post.user_id == User.id).filter(Post.id == id).first()
    if post is None:
        abort(404)
    elif session.get("user_id") is not None:
        like_count = Liked.query.filter_by(post_id = id).count()
        post_liked = bool(db.session.query(Liked).filter_by(post_id=id, user_id=session.get("user_id")).first())
        return render_template('post.html', post=post, post_liked=post_liked, like_count=like_count)
    else:
        like_count = Liked.query.filter_by(post_id = id).count()
        return render_template('post.html', post=post, like_count=like_count)


@post_blueprint.post("/post/<int:id>/")
@login_required
def like_post(id: int):
    post_liked = db.session.query(Liked).filter_by(post_id=id, user_id=session.get("user_id")).first()

    if post_liked is not None:
        db.session.delete(post_liked)
        db.session.commit()
    else:
        db.session.add(Liked(
          user_id = session.get("user_id"),
          post_id = id
        )) # type: ignore
        db.session.commit()

    return jsonify({
        "Success": True
    })
