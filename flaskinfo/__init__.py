from flask import Flask

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = 'b83db2fa7f4b761557ce54d0c8c43ca9b784'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projectinfo.db'

# Initialize database
db = SQLAlchemy(app)

from flaskinfo import routes
