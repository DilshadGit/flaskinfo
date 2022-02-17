from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Initialized app
app = Flask(__name__)

app.config['SECRET_KEY'] = 'b83db2fa7f4b761557ce54d0c8c43ca9b784'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projectinfo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)
# Initialized  password
bcrypt = Bcrypt(app)

# Init
login_manager = LoginManager(app)
# This is tell when in the routes login_required need!
login_manager.login_view = 'login'
# this is show the alert
login_manager.login_message_category = 'info'

from tryflask import routes
