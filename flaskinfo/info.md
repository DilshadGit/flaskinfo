## create modles file for the class and move all classes to this models inside accounts
## when I run the process again can't import db from pro.py because when import the 
	classes the class imported before Initialize database and the both classes created
	after database initializes before so the import will faild
	from accounts.models import User, Post

## we have to change this line below:
	from pro import db to from __main__ import db
	and have to move below this line in pro.py
	# Initialize database

## first create another folder named the same name of the project (flaskinfo)
	and create another file named __.init__.py in side new flaskinfo folder

## we will move all the files and folders into flaskinfo folder has been created
	
## move all import from pro file until initialize database to __init__.py file

## Next we create another file route.py and move all @app.route() codes there 

## Next change pro.py to run.py and add from flaskinfo import app on the top
	if __name__ == '__main__' and rest will stay in run file

## Next import following:
	from datetime import datetime

	from flask import (
	    render_template,
	    url_for,
	    flash,
	    redirect,
	)
	from flaskinfo.accounts.forms import LoginForm, RegisterationForm 
	from flaskinfo.accounts.models import User, Post
	into routes.py

## Next remove the above codes from run.py except from flask import Flask

## Next in the routes files need to import app like below

## Next in the __init__.py need to import routse after Initialzation database
	from flaskinfo import routes

## The last thing we will import db from flaskinfo to the models and change the 
	from __main__ import db to the from flaskinfo import db

## Next go back to pythone shell
	(flaskinfoenv) raffi@raffi-VB:~/Devel/flaskinfo$ python3
	Python 3.7.5 (default, Nov  7 2019, 10:50:52) 
	[GCC 8.3.0] on linux
	Type "help", "copyright", "credits" or "license" for more information.
	>>> from flaskinfo import db
	/home/raffi/.virtualenvs/flaskinfoenv/lib/python3.7/site-packages/flask_sqlalchemy/__init__.py:835: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
	  'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
	>>> from flaskinfo.accounts.models import User, Post
	>>> db.create_all()
	>>> User.query.all()
	[]
	>>> Post.query.all()
	[]
### This below 

## sudo apt-get install tree change the design like below:

flaskinfo$ tree
.
├── flaskinfo
│   ├── accounts
│   │   ├── forms.py
│   │   ├── models.py
│   │   └── __pycache__
│   │       ├── forms.cpython-37.pyc
│   │       └── models.cpython-37.pyc
│   ├── flask_db.db
│   ├── info.md
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   └── routes.cpython-37.pyc
│   ├── required
│   │   ├── requirements.txt
│   │   └── tree.md
│   ├── routes.py
│   ├── static
│   │   ├── css
│   │   │   ├── album.css
│   │   │   └── bootstrap.min.css
│   │   ├── images
│   │   └── js
│   │       └── bootstrap.bundle.min.js
│   ├── templates
│   │   ├── about.html
│   │   ├── auth
│   │   │   ├── login_form.html
│   │   │   └── register_form.html
│   │   ├── base.html
│   │   ├── footer.html
│   │   ├── header.html
│   │   ├── index.html
│   │   ├── messages.html
│   │   └── navbar.html
│   └── tests
├── __pycache__
│   └── pro.cpython-37.pyc
├── README.md
└── run.py

## After added to the branch:
	modified:   .gitignore
	modified:   README.md
	new file:   flaskinfo/__init__.py
	renamed:    accounts/forms.py -> flaskinfo/accounts/forms.py
	renamed:    accounts/models.py -> flaskinfo/accounts/models.py
	renamed:    flask_db.db -> flaskinfo/flask_db.db
	new file:   flaskinfo/info.md
	renamed:    required/requirements.txt -> flaskinfo/required/requirements.txt
	renamed:    required/tree.md -> flaskinfo/required/tree.md
	new file:   flaskinfo/routes.py
	renamed:    static/css/album.css -> flaskinfo/static/css/album.css
	renamed:    static/css/bootstrap.min.css -> flaskinfo/static/css/bootstrap.min.css
	renamed:    static/js/bootstrap.bundle.min.js -> flaskinfo/static/js/bootstrap.bundle.min.js
	renamed:    templates/about.html -> flaskinfo/templates/about.html
	renamed:    templates/auth/login_form.html -> flaskinfo/templates/auth/login_form.html
	renamed:    templates/auth/register_form.html -> flaskinfo/templates/auth/register_form.html
	renamed:    templates/base.html -> flaskinfo/templates/base.html
	renamed:    templates/footer.html -> flaskinfo/templates/footer.html
	renamed:    templates/header.html -> flaskinfo/templates/header.html
	renamed:    templates/index.html -> flaskinfo/templates/index.html
	renamed:    templates/messages.html -> flaskinfo/templates/messages.html
	renamed:    templates/navbar.html -> flaskinfo/templates/navbar.html
	deleted:    info.md
	deleted:    pro.py
	new file:   run.py

## for scure password we need to install flask-bcrypt than go to python shell
	flaskinfo$ python
	Python 3.7.5 (default, Nov  7 2019, 10:50:52) 
	[GCC 8.3.0] on linux
	Type "help", "copyright", "credits" or "license" for more information.
	>>> from flask_bcrypt import Bcrypt
	>>> bcrypy = Bcrypt()
	>>> bcrypt.generate_password_hash('admin123')
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	NameError: name 'bcrypt' is not defined
	>>> bcrypt = Bcrypt()
	>>> bcrypt.generate_password_hash('admin123')
	b'$2b$12$618OQ/qKlgrMIK68sm4JU.Ce84WflOp37kBugsarbcMBlpZ4XPS8y'
	>>> bcrypt.generate_password_hash('admin123')
	b'$2b$12$y6GJ5xpeEYmYXr3PfNAnROhJYOUwPtfUQdIaZYpqUdxpC22Sn.rda'
	>>> bcrypt.generate_password_hash('admin123').decode('utf-8')
	'$2b$12$3ExfH2hKolzUXIgemX6v/uDLWzbQDS.gRWWWhYLt9Du8kI3AKn4sm'
	>>> bcrypt.generate_password_hash('admin123').decode('utf-8')
	'$2b$12$oZTPayXIoWqMtXxDOLYaz.urHGQVPh5GcLrges08PkyOFaOb8FJie'
	>>> bcrypt.generate_password_hash('admin123').decode('utf-8')
	'$2b$12$V/LBIxF6CVz0KxcgQgUOeeGiKztB5s7v0NEo51frRqGvEZfZhpm0m'
	>>> hashed_password = bcrypt.generate_password_hash('admin123').decode('utf-8')
	>>> hashed_password
	'$2b$12$76jK62c5BJ/1Wrse94R7qOFHKj5gRMaLk8oqai9xanMIWnWE8lirW'
	>>> 
	>>> hashed_password
	'$2b$12$76jK62c5BJ/1Wrse94R7qOFHKj5gRMaLk8oqai9xanMIWnWE8lirW'

## We check the password hashed
	>>> bcrypt.check_password_hash(hashed_password, 'password')
	False
	>>> bcrypt.check_password_hash(hashed_password, 'admin123')
	True
	>>> 

## After new user registered check if is saved in db login to shell again:
	/flaskinfo$ python
	Python 3.7.5 (default, Nov  7 2019, 10:50:52) 
	[GCC 8.3.0] on linux
	Type "help", "copyright", "credits" or "license" for more information.
	>>> from flaskinfo import db
	/home/raffi/.virtualenvs/flaskinfoenv/lib/python3.7/site-packages/flask_sqlalchemy/__init__.py:835: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
	  'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '


	>>> from flaskinfo.accounts.models import User
	>>> user = User.query.first()
	>>> user
	User('dilshad', 'dilshad@gmail.com', 'default.jpg')
	>>> users = User.query.all()
	>>> users
	[User('dilshad', 'dilshad@gmail.com', 'default.jpg'), User('hello', 'hello@gmail.com', 'default.jpg')]
	>>> user.password
	'$2b$12$8.MMceoyvP/A9YtYR0Ps..5eegyVKyrNuRPy4an6AZ8vwg2wBmWG.'
	>>> user.password
	'$2b$12$8.MMceoyvP/A9YtYR0Ps..5eegyVKyrNuRPy4an6AZ8vwg2wBmWG.'
	>>> 

## for check user login page or form need install flask_login
	import from flask_login import LoginManager in the __init__


