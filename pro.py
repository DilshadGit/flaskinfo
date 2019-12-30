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

from accounts.models import User, Post


app = Flask(__name__)

app.config['SECRET_KEY'] = 'b83db2fa7f4b761557ce54d0c8c43ca9b784'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_db.db'

db = SQLAlchemy(app)

posts = [
    {
        'title': 'Python3',
        'author': 'Dilshad',
        'date': '01 Dec 2019',
        'content': ' Welcome to Python3'
    },
    {
        'title': 'Django3',
        'author': 'Azad',
        'date': '01 Nov 2019',
        'content': ' Welcome to Django3'
    },
    {
        'title': 'Flask',
        'author': 'Shvan',
        'date': '01 Aug 2018',
        'content': ' Welcome to Flask'
    }
]


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
