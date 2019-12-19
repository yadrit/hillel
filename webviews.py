import random
import string
import requests
from flask import Flask, request
from db import exec_query
from faker import Faker


app = Flask('app')

@app.route('/')
def hello():
    return 'Hello'

@app.route('/hello-world')
def hello_world():
    return 'Hello worlodo'

@app.route('/gen')
def gen():
    return ''.join(
        random.choice(string.ascii_uppercase) for i in range(10)
    )


# Task 1.1. Return content of requirements.txt on web view

@app.route('/req-txt')
def req_txt():
    with open('./requirements.txt') as file:
        return file.read()


# Task 1.2. Return names and emails of 100 random generated users

@app.route('/random-hundred')
def fake_hun():
    fake = Faker()
    return ' '.join(' | ' + fake.name() + ' ' + fake.email() for i in range(100))


# Task 1.3. Return average height and weight using provided csv file

@app.route('/mean-height-width')
#
#


# Task 1.4. Return the number of astronauts


@app.route('/cur-astronauts')
def cur_astr():
    r = requests.get('http://api.open-notify.org/astros.json', auth=('user', 'pass'))
    jsn = r.json()
    return str(jsn['number'])


# Task 2.3. View function returns the number of unique names (FirstName)

@app.route('/all-customers')
def all_customers():
    result = exec_query(f'SELECT COUNT (DISTINCT FirstName) FROM customers')
    return str(result)


# Task 2.4. View function returns total profit from invoice_items column

@app.route('/profit')
def profit():
    result = exec_query(f'SELECT SUM(UnitPrice * Quantity) FROM invoice_items')
    return str(result)

# Lesson 5
@app.route('/gener')
def gener():
    number = int(request.args['number'])
    # if number not in range(100)
    # return 'Wrong number'
    if 0 < number < 100:
        return ''.join(random.choice(string.ascii_uppercase) for _ in range(10))
    return "Wrong number"

if __name__ == '__main__':
    app.run(port=5000, debug=True)