from datetime import datetime

from flask import (
    Flask,
    render_template,
    url_for,
    flash,
    redirect,
)

from flask_sqlalchemy import SQLAlchemy

from accounts.forms import (
    LoginForm,
    RegisterationForm,
)

# from accounts.models import User, Post


app = Flask(__name__)

app.config['SECRET_KEY'] = 'b83db2fa7f4b761557ce54d0c8c43ca9b784'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_db.db'

db = SQLAlchemy(app)

# posts = [
#     {
#         'title': 'Python3',
#         'author': 'Dilshad',
#         'date': '01 Dec 2019',
#         'content': ' Welcome to Python3'
#     },
#     {
#         'title': 'Django3',
#         'author': 'Azad',
#         'date': '01 Nov 2019',
#         'content': ' Welcome to Django3'
#     },
#     {
#         'title': 'Flask',
#         'author': 'Shvan',
#         'date': '01 Aug 2018',
#         'content': ' Welcome to Flask'
#     }
# ]


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


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', title='Post', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About', posts=posts)


'''
In the register form there is a request when you click on submit
you have to add methods in the rout
'''


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterationForm()
    if form.validate_on_submit():
        flash(
            f'{ form.username.data.upper() } your account successfully created', 'success')
        return redirect(url_for('home'))
    return render_template('account/register_form.html', title='Registeration', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    '''
    In the register form there is a request when you click on submit
    which is means get or post therefore you have to add methods as
    an argument to the route.
    '''
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'dilmac@gmail.com' and form.password.data == 'admin123':
            flash(f'You have been successfully logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalide details. Please check your username and password!', 'danger')
    return render_template('account/login_form.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
