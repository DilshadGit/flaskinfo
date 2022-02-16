"""Im port only those object related to route file from flask."""
from flask import (
    render_template,
    url_for,
    flash,
    redirect,
    request
)


from tryflask import app, db, bcrypt
from tryflask.accounts.forms import LoginForm, RegisterationForm
from tryflask.accounts.models import User, Post
# after check the user email and password we need to import 
from flask_login import (
    login_user,
    current_user,
    logout_user,
    login_required)


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


@app.route('/', methods=['GET', 'POST'])
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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data, password=hashed_password)
        # adding to the db
        db.session.add(user)
        db.session.commit()

        flash('You have created an account! Please try to login', 'success')
        return redirect(url_for('login'))
    return render_template('auth/register_form.html', title='Registeration', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    '''
    In the register form there is a request when you click on submit
    which is means get or post therefore you have to add methods as
    an argument to the route.
    '''
    form = LoginForm()
    if form.validate_on_submit():

        # # if form.email.data == 'dilmac@gmail.com' and form.password.data == 'admin123':
        #     flash(f'You have been successfully logged in!', 'success')
        #     return redirect(url_for('home'))
        # else:
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            """We add next when user try to access profile when is logout
            display next in the url and need to define next below."""
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Invalide details. Please check your email and password!', 'danger')
    return render_template('auth/login_form.html', title='Login', form=form)


@app.route('/auth/logout')
def log_out():
    logout_user()
    return redirect(url_for('login'))


@app.route('/auth/profile', methods=['GET'])
@login_required
def profile():
    # user_profile  = User.query.get(id=id)
    return render_template('auth/profile.html', title='Profile')
