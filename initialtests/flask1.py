# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 16:07:11 2019

@author: suilven
"""

"""
FLASK_APP=hello.py flask run
 * Running on http://localhost:5000/
 
  > set FLASK_APP=hello.py
    > set FLASK_ENV=development
    > flask run

Options:
  --version  Show the flask version
  --help     Show this message and exit.
 
 
 
 """



from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"