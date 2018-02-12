import logging
from os import urandom
import sys
from bcrypt import gensalt, hashpw
from flask import Flask, flash, redirect, render_template, request, session, url_for
from utils.database import Database, User

# create a Flask application with name "__main__"
logging.info('Creating `app`')
db = Database()
app = Flask(__name__)


@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    """Role selection page"""
    # if user is logged in, render role selection page
    if session.get('logged_in'):
        email, username, unit_number, rank, is_civilian, is_dispatch, is_police, is_admin = db.get_user_info(session['user_id'])
        return render_template('index.html',
                               user_rank=rank,
                               user_name=username,
                               user_unit_number=unit_number)
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['POST', 'GET'])
def login():
    """Login page"""
    if request.method == 'POST':
        # get unit number/email field
        units = request.form.get('units')
        if units is None:
            return index()

        # figure out if the user used their email or unit code to login
        use_email = False
        use_unit_number = False
        if '@' in units:
            use_email = True
        else:
            use_unit_number = True

        # get password, send them back if they didn't put anything
        password = request.form.get('password')
        if password is None:
            return index()

        # get old password hash and salt for a given user from database
        id, pass_hash, pass_salt = db.get_password(units, use_email=use_email, use_unit_number=use_unit_number)

        # in case a specific user doesn't exist
        if id is None:
            return index()

        # encode password for hashing
        password = password.encode('utf-8')
        # hash input password with the old salt, if the result matches the old hash, login
        if hashpw(password, pass_salt) == pass_hash:
            session['user_id'] = id
            session['logged_in'] = True

        # complete login... or not.
        return redirect(url_for('index'))

    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.config['SECRET_KEY'] = urandom(24)
    app.run()
