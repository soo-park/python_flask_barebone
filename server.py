# -*- coding: utf-8 -*-
# the above line is necessary to run the server in utf-8

"""This module is built to run a simple RESTful API"""
import os

# bringin json
from json import dumps

# bring in datetime object
import datetime

# Execute Flask object
from flask import Flask, jsonify, request, redirect, url_for, make_response, abort

# from flask_debugtoolbar import DebugToolbarExtension
app = Flask(__name__)

# "source secret.sh" to run flask server prior to "python server.py"
# content of the sercret.sh: export secret_key="<your secret key>"
app.secret_key = os.environ['secret_key']

@app.route('/')
def index():
    """root get request"""
    return "[CONNECTED] available routes: consult README.md", 200

# /hello?firstname={first name}&lastname={last name}&gender={m/f}
# curl -i http://localhost:5000/hello?firstname=tien&lastname=nguyen&gender=m
# "Hello Mr Tien Nguyen"
@app.route('/hello', methods=['GET'])
def say_hello():
    """say hello with gender, first/last name"""

    firstname = request.args.get('firstname')[0].upper() + request.args.get('firstname')[1:]
    lastname = request.args.get('lastname')[0].upper() + request.args.get('lastname')[1:]
    gender = request.args.get('gender')

    if gender == "m":
        prefix = "Mr"
    elif gender == "f":
        prefix = "Ms"
    else:
        prefix = "M"

    return dumps("Hello" + " " +prefix + " " + firstname + " " + lastname), 201


# /compute?num1={num1}&num2={num2}&operator={add/subtract/multiply/divide}
# /compute?num1=5&num2=3&operation=subtract
# returns “2” (5-3=2)
@app.route('/compute', methods=['GET'])
def calculate():
    """calculation"""

    num1 = int(request.args.get('num1').decode('utf-8'))
    num2 = int(request.args.get('num2').decode('utf-8'))
    operation = request.args.get('operation').lower()

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1- num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        result = num1 / num2
    else:
        return "ERROR: Input incorrect to calculate", 404

    return dumps(result), 201


# /date
# with the current date in the form “yyyy-mm-dd” eg. “2017-09-20”
@app.route('/date')
def date():
    """date get request"""
    date_obj = datetime.datetime.now()
    return dumps(date_obj.isoformat()), 200


@app.errorhandler(404)
def not_found(error):
    """Better error handling"""
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    # debug=True here, since it need be True at point DebugToolbarExtension get invoked
    app.run(debug=True)

    # # Use the DebugToolbar
    # DebugToolbarExtension(app)

    # Run internal server
    app.run(port=5000, host='0.0.0.0')
