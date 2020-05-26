import datetime
from mongoengine import StringField, DateTimeField, ImageField, Document
from flask_login import UserMixin


class User(Document, UserMixin):
    username = StringField(max_length=50, required=True)
    email = StringField(required=True)
    password = StringField(required=True)
    dob = DateTimeField(required=False)