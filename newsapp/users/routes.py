from flask import Flask, url_for, render_template, Blueprint, flash, redirect, request, send_from_directory
from newsapp import app, bcrypt
from newsapp.users.forms import RegistrationForm
from newsapp.users.models import User
from werkzeug.utils import secure_filename
import os

users = Blueprint('users', __name__)


@app.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegistrationForm()
    if register_form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(register_form.password.data)
        user = User(username=register_form.username.data,
                    email=register_form.email.data,
                    password=hashed_password,
                    dob=register_form.dob.data).save()
        flash('Congrates, Your account has been created.', 'ui info floating small message')
        return redirect(url_for('login'))
    return render_template('register.html', register_form=register_form)

@app.route('/login')
def login():
    return render_template('login.html')