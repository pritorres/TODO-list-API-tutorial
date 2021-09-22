#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request, Response,json
app = Flask(__name__)

todos = [{'label': 'My first task', 'done': False},
         {'label': 'My second task', 'done': False}]

API_ENDPOINT = \
    'https://3245-ivory-gerbil-24gc4wds.ws-us15.gitpod.io/todos'


@app.route('/todos', methods=['GET'])
def add_new_get():

    return jsonify(todos)


@app.route('/todos', methods=['POST'])
def add_new_todo():
  data_origin = request.data
  data_transf = json.loads(data_origin)
  todos.append(data_transf)
  return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    print(dir(todos.pop(position)))
    return jsonify(todos)

# These two lines should always be at the end of your app.py file.

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
