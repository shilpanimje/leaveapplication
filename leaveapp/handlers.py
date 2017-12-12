from app import app
from flask import render_template, request, json
from leaveapp import config
from leaveapp.logic import user


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/createUser', methods=['POST'])
def create_user():
    # get form data and check  validate data
    name = request.form['name']
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['password2']

    if not name or not username or not password:
        return json.dumps(
            {'html': 'Please fill all required filled',
             'flag': 0})

    if password != confirm_password:
        return json.dumps(
            {'html': 'Confirm password does not match with password',
             'flag': 0})

    return user.create_user(request.form)


