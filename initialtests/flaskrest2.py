# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 20:43:30 2019

@author: suilven
"""

"""
You can try it like this:

$ curl http://localhost:5000/todo1 -d "data=Remember the milk" -X PUT
{"todo1": "Remember the milk"}
"""
"""
$ curl http://localhost:5000/todo1
{"todo1": "Remember the milk"}
$ curl http://localhost:5000/todo2 -d "data=Change my brakepads" -X PUT
{"todo2": "Change my brakepads"}
$ curl http://localhost:5000/todo2
{"todo2": "Change my brakepads"}
Or from python if you have the requests library installed:

>>> from requests import put, get
>>> put('http://localhost:5000/todo1', data={'data': 'Remember the milk'}).json()
{u'todo1': u'Remember the milk'}
>>> get('http://localhost:5000/todo1').json()
{u'todo1': u'Remember the milk'}
>>> put('http://localhost:5000/todo2', data={'data': 'Change my brakepads'}).json()
{u'todo2': u'Change my brakepads'}
>>> get('http://localhost:5000/todo2').json()
{u'todo2': u'Change my brakepads'}
"""



from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}
myrequest='original'

class TodoSimple(Resource):
    def get(self, todo_id):
        #return {todo_id: todos[todo_id]}
        return myrequest

    def put(self, todo_id):
        #todos[todo_id] = request.form['data']
        #return {todo_id: todos[todo_id]}
        myrequest=request.data
        return myrequest

api.add_resource(TodoSimple, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)