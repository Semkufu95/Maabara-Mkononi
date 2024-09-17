#!/usr/bin/python3
'''
Main flask application 
'''

from flask import Flask, render_template
from flask_mysqldb import MySQL
from config import Config

from routes.auth import auth_blueprint
from routes.tests import tests_blueprint


app = Flask(__name__)
app.config.from_object(Config)

#Initialize MySQL
mysql = MySQL(app)

#Register blueprints
app.register_blueprint(auth_blueprint)
app.register_blueprint(tests_blueprint)


@app.route('/')
def home():
    '''

    '''
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
