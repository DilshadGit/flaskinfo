import email_validator
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    BooleanField,
)
# We import User from models to check if the data in the fields
# are exisite in the db
from .models import User

from wtforms.validators import (
	DataRequired,
	length,
	Email,
	EqualTo,
	ValidationError
	)


class RegisterationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(),
							length(min=4, max=12)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	password_confirm = PasswordField('Confirm Password',
							validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')

	# This function is check if the fields are correct like email or username
	# hase been duplicated as well with email.
	# def validate_username(self, username):
	# 	user = User.query.first(username=username.data).first()
	# 	if True:
	# 		raise ValidationError('Validation message')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('This user is taken, please try another username!')

	def validate_email(self, email):
		email = User.query.filter_by(email=email.data).first()
		if email:
			raise ValidationError('This email is exisit, please try another email!')


class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	
	submit = SubmitField('Login')
