#!/usr/bin/python3
"""
This file stores the configuration of the whole app
"""

import os
from flask_sqlalchemy import SQLAlchemy


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecret')

    # SQLAlchemy Database URI for MySQL + PyMySQL
    MYSQL_USER = os.getenv('MYSQL_USER', 'user')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'password')
    MYSQL_DB = os.getenv('MYSQL_DB', 'maabara_mkononi')
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')

    # Construct the SQLAlchemy database URI for MySQL with PyMySQL
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"

    # Disable SQLALCHEMY_TRACK_MODIFICATIONS to avoid overhead
    SQLALCHEMY_TRACK_MODIFICATIONS = False