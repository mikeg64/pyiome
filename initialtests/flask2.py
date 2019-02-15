# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 16:23:41 2019

@author: suilven
"""

import os

#from flask import Flask
from flask import Flask, request

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    @app.route('/goodbye')
    def goodbye():
        return 'Goodbye, World!'
    
    @app.route("/")
    def form():
        return '<form action="/echo" method="GET"><input name="text"><input type="submit" value="Echo"></form>'
 
    @app.route("/echo")
    def echo(): 
        return "You said: " + request.args.get('text', '')
    
    #todisplay an image or get ouput
    #http://localhost:5000/hellotest?text=timetogetlouis%20now 
    @app.route("/hellotest")
    def hellotest(): 
        return "You said: " + request.args.get('text', '')
 

    
    
    
    

    return app