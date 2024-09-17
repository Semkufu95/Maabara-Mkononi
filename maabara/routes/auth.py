from flask import Blueprint, render_template, request, redirect, flash
from werkzeug.security import generate_password_hash, check_password_hash
from app import mysql

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    '''
    Register a new user
    '''
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])

        cursor = mysql.connection,cursor()
        cursor.execute("INSERT INTO users(name, email, password) VALUES(%s, %s, %s)", (name, email, password))
        mysql.connection.commit()
        cursor.close()

        flash("Registration successful!")
        return redirect('/login')

    return render_template('registration.html')


@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    '''
    login user
    '''
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s", [email])
        user = cursor.fetchone()
        cursor.close()

        if user and check_password_hash(user['password'], password):
            flash("Login successful!")
            return redirect('/')
        else:
            flash("Invalid credentials")

    return render_template('login.html')
