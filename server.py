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
    return "Now connected to the localhost:5000"


@app.route('/date')
def date():
    """date get request"""
    date_obj = datetime.datetime.now()
    return dumps(date_obj.isoformat())

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


# curl -i http://localhost:5000/todo/api/v1.0/tasks
@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    """tasks get request"""
    print "yay"
    return jsonify({'tasks': tasks})


# curl -i http://localhost:5000/todo/api/v1.0/tasks/2
# returns the task
# curl -i http://localhost:5000/todo/api/v1.0/tasks/3
# returns 404
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """individual task get request"""
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


@app.errorhandler(404)
def not_found(error):
    """Better error handling"""
    return make_response(jsonify({'error': 'Not found'}), 404)

# curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' http://localhost:5000/todo/api/v1.0/tasks
@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    """POST task"""
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201


# curl -i -H "Content-Type: application/json" -X PUT -d '{"done":true}' http://localhost:5000/todo/api/v1.0/tasks/2
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """task put"""
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})


# curl -i -X DELETE http://localhost:5000/todo/api/v1.0/tasks/2
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """delete task"""
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})


if __name__ == '__main__':
    # debug=True here, since it need be True at point DebugToolbarExtension get invoked
    app.run(debug=True)

    # # Use the DebugToolbar
    # DebugToolbarExtension(app)

    # Run internal server
    app.run(port=5000, host='0.0.0.0')
