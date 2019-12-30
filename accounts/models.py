from datetime import datetime
from ..pro import db


class User(db.Model):
    '''
    lazy argument used to load the data from sql alchemy database
    argument use for another field in post model
    '''
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    image = db.Column(db.String(22), nullable=False, default='default.jpg')
    password = db.Column(db.String(40), nullable=False)
    post = db.relastionship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image}')"


class Post(db.Model):
    '''
    we have to add user_if there is a relationships
    user and post model.
    '''
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(90), nullable=False)
    content = db.Column(db.Text, nullable=False, default='default.jpg')
    photo = db.Column(db.String(42), nullable=False, default='default.jpg')
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.Foreignkey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.title}', '{self.date}', '{self.photo}')"
