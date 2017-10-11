# -*- coding: utf-8 -*-
# the above line is necessary to run the server in utf-8

"""This module is built to run a simple RESTful API"""
import os
import datetime
import numbers
from json import dumps
from flask import Flask, jsonify, request, render_template, redirect, url_for, make_response, abort

# from flask_debugtoolbar import DebugToolbarExtension
app = Flask(__name__)


@app.route('/')
def index():
    """
    [root get request]
    """
    return "[CONNECTED] available routes: consult README.md", 200


@app.route('/hello', methods=['GET', 'POST'])
def say_hello():
    """
    [Say hello with gender, first/last name]
    This route will receive three parameters, and will return a greeting.

    Route structure:
    /hello?firstname={first name}&lastname={last name}&gender={m/f}

    Parameters:
    firstname, lastname, gender(choose: m/f)

    Response: 
    "Hello Mr {First Name} {Last Name}”
    or
    “Hello Ms {First Name} {Last Name}”
    depending on the gender.

    Example:
    request “/hello?firstname=tien&lastname=nguyen&gender=m”
    response “Hello Mr Tien Nguyen”
    """

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


@app.route('/compute', methods=['GET', 'POST'])
def calculate():
    """
    [Basic Calculation]
    This route will receive three parameters and will return the result of calculation.abort

    Route structure: 
    /compute?num1={num1}&num2={num2}&operator={add/subtract/multiply/divide}

    Parameters:
    num1, num2, operator(choose: add/subtract/multiply/divide)

    Response:
    calculated result in an integer

    Example:
    the request “/compute?num1=5&num2=3&operation=subtract” returns “2” (5-3=2)
    """

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
        if (num2 == 0):
            return "Cannot divide with zero"
        result = num1 / num2
    else:
        return "ERROR: Input incorrect to calculate", 500

    return dumps(result), 201


@app.route('/date')
def get_date():
    """
    [Get date for today in iso format]
    This route will not receive any parameters, and will return today's date in iso format

    Route structure:
    /date

    Response:
    the current date in the form “yyyy-mm-dd”

    Example:
    “/date” returns “2017-09-20”
    """
    
    date_obj = datetime.date.today()
    
    return dumps(date_obj.isoformat()), 200


#####################
#   Error Routes
#####################  

@app.errorhandler(404)
def page_not_found(e):
    """Better error handling"""
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(500)
def internal_server_error(e):
    return make_response(jsonify({'error': 'Internal server error'}), 500)

@app.errorhandler(403)
def page_forbidden(e):
    return make_response(jsonify({'error': 'page_forbidden'}), 403)


# To run the error routes above, turn off the debug mode below
#####################
#   Context Processors
#####################

if __name__ == '__main__':
    # debug=True here, since it need be True at point DebugToolbarExtension get invoked
    app.run(debug=True)

    # # Use the DebugToolbar
    # DebugToolbarExtension(app)

    # Run internal server
    app.run(port=5000, host='0.0.0.0')
