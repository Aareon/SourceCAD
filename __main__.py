import logging
from os import urandom
import sys
from passlib.hash import bcrypt
from flask import Flask, flash, redirect, render_template, request, session, url_for, Markup
from utils.database import Database, User
from string import ascii_uppercase
from string import digits as string_digits
from random import choice

# create a Flask application with name "__main__"
db = Database()
app = Flask(__name__)

@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    """Role selection page"""
    # if user is logged in, render role selection page
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    email, username, unit_number, rank, is_civilian, is_dispatch, is_police, is_admin = db.get_user_info(session['user_id'])
    session['email'] = email
    session['username'] = username
    session['unit_number'] = unit_number
    session['rank'] = rank
    session['is_civilian'] = is_civilian
    session['is_dispatch'] = is_dispatch
    session['is_police'] = is_police
    session['is_admin'] = is_admin
    return render_template('index.html',
                           user_rank=rank,
                           user_name=username,
                           user_unit_number=unit_number)

@app.route('/login', methods=['POST', 'GET'])
def login():
    """Login page"""
    if request.method == 'POST':
        # get unit number/email field
        units = request.form.get('units')
        print(units)
        if units is None:
            return index()

        # figure out if the user used their email or unit code to login
        use_email = True if '@' in units else False
        use_unit_number = True if '@' not in units else False

        # get password, send them back if they didn't put anything
        password = request.form.get('password')
        if password is None:
            return index()

        # get old password hash and salt for a given user from database
        id, pass_hash = db.get_password(units, use_email=use_email, use_unit_number=use_unit_number)
        print(id, pass_hash)

        # in case a specific user doesn't exist
        if id is None:
            return index()

        # verify password matches previous hash
        if bcrypt.verify(password, pass_hash):
            session['user_id'] = id
            session['logged_in'] = True

        # complete login... or not.
        return redirect(url_for('index'))

    # in case of 'GET' request
    else:
        return render_template('login.html')

@app.route('/registration', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        unit_number = request.form.get('unit_number')
        password = request.form.get('password')
        is_dispatch = bool(request.form.get('is_dispatch', False))
        is_civilian = bool(request.form.get('is_civilian', False))
        is_police = bool(request.form.get('is_police', False))
        if len(password) < 8:
            return registration()

        password = bcrypt.hash(password)

        access_token = request.form.get('access_token')

        with open('access_token.txt') as f:
            if access_token != f.read():
                print('bad token')
                return registration()

        if '@' not in email:
            return registration()

        if '.' not in email:
            return registration()

        if len(username) > 32:
            return registration()
        
        if '-' not in unit_number or len(unit_number) > 5:
            return registration()

        success = db.create_user(username, email, unit_number, password, is_dispatch, is_civilian, is_police)
        if success:
            return login()
        else:
            return registration()

    return render_template('registration.html')

def gen_bolo_table():
    bolos = db.get_bolos()
    if len(bolos) == 0:
        return Markup('<div class="dispatch-callout-current">No active BOLOs</div>')

    template = '<div class="dispatch-callout-current">\n\
      Reason: {reason} <br>\n\
      Location: {location} <br>\n\
      Description: {description}<br>\n\
      Notes: {notes} <br>\n\
    </div>\n'

    output = ''
    for bolo in bolos:
        reason = bolo[1]
        location = bolo[2]
        description = bolo[3]
        notes = bolo[4]
        output += template.format(reason=reason, location=location, description=description, notes=notes)
    return Markup(output)


def gen_callout_table():
    callouts = db.get_callouts()

    if len(callouts) == 0:
        return Markup('<div class="dispatch-callout-current">No active callouts</div>')

    template = '<div class="dispatch-callout-current">\n\
    Reason: {reason} <br>\n\
    Location: {location} <br>\n\
    Details: {details}<br>\n\
    Present Units: {units} <br>\n\
    </div>\n'

    output = ''
    for callout in callouts:
        reason = callout[1]
        location = callout[2]
        details = callout[3]
        present_units = callout[4]
        output += template.format(reason=reason, location=location, details=details, units=present_units)
    return Markup(output)

@app.route('/dispatch')
def dispatch():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    callouts = gen_callout_table()
    bolos = gen_bolo_table()
    return render_template('dispatch.html', callouts=callouts, bolos=bolos)

@app.route('/police')
def police():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    return render_template('police.html')

@app.route('/civilian')
def civilian():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    return render_template('civilian.html')

def gen_access_token():
    chars = ascii_uppercase + string_digits
    return ''.join(random.choice(chars) for _ in range(8))
    

@app.route('/admin')
def admin():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    if not session.get('is_admin'):
        return redirect(url_for('index'))

    return render_template('admin.html')

if __name__ == '__main__':
    app.config['SECRET_KEY'] = urandom(24)
    app.run()
