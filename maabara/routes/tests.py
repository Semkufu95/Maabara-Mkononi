'''
Test Booking and results management routes
'''

from flask import Blueprint, render_template, requests, redirect, flash
from app import mysql

tests_blueprint = Blueprint('tests', __name__)

@tests_blueprint.route('/book_test', methods=['GET', 'POST'])
def book_test():
    '''
    Fuction to book a test
    '''
    if request.method == 'POST':
        user_id = request.form['user_id']
        test_type = request.form['test_type']
        date = request.form['date']

        cursor = mysql.connection.cursor()
        cursor.execute("USER INTO test_bookings(user_id, test_type, date) VALUES(%s, %s, %s)", (user_id, test_type, date))
        mysql.connection.commit()
        cursor.close()

        flash("Test Booked Successfully!")
        return redirect('/')

    return render_template('book_test.html')


@tests_blueprint.route('/results/<int:user_id>')
def results(user_id):
    '''
    Resullts
    '''
    cursor = mysql.connection.cursor()
    cursor.execut("SELECT * FROM test_results WHERE user_id = %s", [user_id])
    results = cursor.fetchall()
    cursor.close()

    return render_template('results.html', results=results)
