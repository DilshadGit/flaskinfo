# flaskrepo
## To create flask after activation you have run this command

### export FLASK_APP=pro.py

### Import render_template to redirect to the template we want

### Import url_for('Add the name of the method') for changing the page used in anker tags

### To create user login logout and registeration form need to install flask-wtf

### Installed mypy and pylint for codes style or clean codes and mypy to display lib import

### To create secrets key in python login to shell
	import secrets
	secrets.token_hex(15)

### Import flash to check if the form is validate when the user add data in the form.

### Creat database for the application need to install flask-sqlalchemy
#### Saperate class models from main apps to make it more clear


go to python to create shell database

python3
Python 3.7.5 (default, Nov  7 2019, 10:50:52) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from pro import db
/home/raffi/.virtualenvs/flaskinfoenv/lib/python3.7/site-packages/flask_sqlalchemy/__init__.py:835: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
  'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
>>> db.create_all()
>>> from pro import User, Post
>>> user_1 = User(username='dilmac', email='dil@gmail.com', password='admin123')
>>> db.session.add(user_1)
>>> user_2 = User(username='raffi', email='raffi@gmail.com', password='admin123')
>>> db.session.add(user_2)
>>> db.session.commit()
>>> User.query.all()
[User('dilmac', 'dil@gmail.com', 'default.jpg'), User('raffi', 'raffi@gmail.com', 'default.jpg')]
>>> User.query.first()
User('dilmac', 'dil@gmail.com', 'default.jpg')
>>> User.query.filter_by(email='dil@gmail.com').all()
[User('dilmac', 'dil@gmail.com', 'default.jpg')]
>>> User.query.filter_by(username='dilmac').first()
User('dilmac', 'dil@gmail.com', 'default.jpg')
>>> user = User.query.filter_by(username='dilmac').first()
>>> user
User('dilmac', 'dil@gmail.com', 'default.jpg')
>>> user.id
1
>>> user.username
'dilmac'
>>> user = User.query.get(2)
>>> user = User.query.get(1)
>>> user.id
1
>>> user = User.query.get(1)
>>> user
User('dilmac', 'dil@gmail.com', 'default.jpg')
>>> user = User.query.get(2)
>>> user
User('raffi', 'raffi@gmail.com', 'default.jpg')
>>> user.posts
[]


>>> post_1 = Post(title='Python3.7', content='Welcome to python3.7 tutorial for beginner.', user_id=user.id)
>>> post_2 = Post(title='Django framework', content='Welcome to Django3 tutorial for beginner.', user_id=user.id)
>>> post_3 = Post(title='Flask framework', content='Welcome to flask tutorial for beginner.', user_id=user.id)
>>> db.session.add(post_1)
>>> db.session.add(post_2)
>>> db.session.add(post_3)
>>> db.session.commit()
>>> user.posts
[User('Python3.7', '2019-12-30 16:04:45.068444', 'default.jpg'), User('Django framework', '2019-12-30 16:04:45.068996', 'default.jpg'), User('Flask framework', '2019-12-30 16:04:45.069155', 'default.jpg')]
>>> 

>>> for post in user.posts:
...     print(post.title)
...     print(post.content)
... 
Python3.7
Welcome to python3.7 tutorial for beginner.
Django framework
Welcome to Django3 tutorial for beginner.
Flask framework
Welcome to flask tutorial for beginner.
>>> post = Post.query.first()
>>> post
User('Python3.7', '2019-12-30 16:04:45.068444', 'default.jpg')
>>> post.user_id
2
>>> post.author
User('raffi', 'raffi@gmail.com', 'default.jpg')
>>> post.user_id
2
>>> post.author
User('raffi', 'raffi@gmail.com', 'default.jpg')
>>> db.drop_all()
>>> db.create_all()
>>> User.query.all()
[]
>>> Post.query.all()
[]
>>> 
