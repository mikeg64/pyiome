# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 20:39:10 2019

@author: suilven
"""
"""
$ python api.py
 * Running on http://127.0.0.1:5000/
 * Restarting with reloader
 
 
 $ curl http://127.0.0.1:5000/
{"hello": "world"}
 
"""




from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)