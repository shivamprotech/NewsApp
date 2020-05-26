from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField, SubmitField, FileField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Optional, Email, ValidationError
from datetime import date
from newsapp.users.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    dob = DateField('Date of Birth', format='%Y-%m-%d', validators=[Optional()])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        if User.objects(username=username.data):
            raise ValidationError('Username is Taken, Please choose a different one.')
    
    def validate_email(self, email):
        if User.objects(email=email.data):
            raise ValidationError('Email is Taken, Please choose a different one.')


class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
