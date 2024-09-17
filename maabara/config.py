#!/usr/bin/python3
"""
This file stores the configuration of the whole app
"""

import os
from flask_mysqldb import MySQL

mysql = MySQL()


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecret')
    MYSQL_USER = os.getenv('MYSQL_USER', 'user')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'password')
    MYSQL_DB = os.getenv('MYSQL_DB', 'maabara_mkononi')
    MYSQL_CURSORCLASS = 'DictCursor'
