from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import UserMixin
from hashing import UpdatedHasher
from sqlalchemy.orm import relationship



scriptdir = os.path.dirname(os.path.abspath(__file__))
pepfile = os.path.join(scriptdir, "pepper.bin")


db = SQLAlchemy()

with open(pepfile, 'rb') as fin: #TODO Something weird breaks here
  pepper_key = fin.read()

pwd_hasher = UpdatedHasher(pepper_key)

#For the tables when adding database object if you want to ignore it just use '#type: ignore'

class User(UserMixin, db.Model):
    __tablename__ ="User"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Unicode, nullable=False)
    username = db.Column(db.Unicode, nullable=False)
    avatar = db.Column(db.Unicode, nullable=False)
    bio = db.Column(db.Unicode, nullable=True)
    password_hash = db.Column(db.LargeBinary) # hash is a binary attribute

    # make a write-only password property that just updates the stored hash
    @property
    def password(self):
        raise AttributeError("password is a write-only attribute")
    @password.setter
    def password(self, pwd: str) -> None:
        self.password_hash = pwd_hasher.hash(pwd)
    
    # add a verify_password convenience method
    def verify_password(self, pwd: str) -> bool:
        return pwd_hasher.check(pwd, self.password_hash)
    
    def get_id(self):
        return self.id

''' Model definition for posts table
    Primary Key: (Post.id)
'''
class Post(db.Model):
    __tablename__ = "Posts"
    id = db.Column(db.Integer, primary_key=True)
    post_title = db.Column(db.Unicode, nullable=False)
    post_story = db.Column(db.Unicode, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("User.id"))
    user_rel = relationship("User", foreign_keys=[user_id])

''' Model Definition for liked posts table
    Primary Key: (User.id, Post.id)
'''
class Liked(db.Model):
    __tablename__ = "Liked"
    user_id = db.Column(db.Integer, db.ForeignKey("User.id"), primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("Posts.id"), primary_key=True)
    rel1 = relationship("User", foreign_keys=[user_id])
    rel2 = relationship("Post", foreign_keys=[post_id])