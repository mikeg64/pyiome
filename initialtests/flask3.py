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



from flask import Flask, request

import sys
print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: " , str(sys.argv))



app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World!"


    
@app.route('/goodbye')
def goodbye():
    return 'Goodbye, World!'
    
@app.route("/form")
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



