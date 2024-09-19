#!/usr/bin/python3
'''
Main flask application 
'''

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config

from routes.auth import auth_blueprint
from routes.tests import tests_blueprint


app = Flask(__name__)
app.config.from_object(Config)

#Replaced MySQL with SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@localhost/database_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Initialize MySQL
db = SQLAlchemy(app)

#Register blueprints
app.register_blueprint(auth_blueprint)
app.register_blueprint(tests_blueprint)


@app.route('/')
def home():
    '''
    return the home page for the webApp
    '''
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
