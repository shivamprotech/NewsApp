from flask import Flask
from mongoengine import connect
from flask_bcrypt import Bcrypt

app = Flask(__name__)
#Secret key
app.config['SECRET_KEY'] = b'5946e24e408b8778e85f197e0755a3a0'
# # Mongo db connection.
connect('news')

bcrypt = Bcrypt(app)


from newsapp.news.routes import books
from newsapp.users.routes import users

app.register_blueprint(books)
app.register_blueprint(users)