from datetime import datetime
from tryflask import db, login_manager
"""Import user mixin to help us we following:
is_authenticate, is_active, is_annoumouse, get_id"""
from flask_login import UserMixin


## create decorator to hel on the login route
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    '''
    lazy argument used to load the data from sql alchemy database
    argument use for another field in post model
    '''
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    image = db.Column(db.String(22), nullable=False, default='default.jpg')
    password = db.Column(db.String(40), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image}')"


class Post(db.Model):
    '''
    we have to add user_if there is a relationships
    user and post model.
    '''
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(90), nullable=False)
    content = db.Column(db.Text, nullable=False)
    photo = db.Column(db.String(42), nullable=False, default='default.jpg')
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.title}', '{self.date}', '{self.photo}')"
