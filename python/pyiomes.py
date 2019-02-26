# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 07:37:34 2019

@author: mike


# pyiomes
#Client and test calls to server


set FLASK_APP=pyiomes.py 
flask run
 * Running on http://localhost:5000/
 
  > set FLASK_APP=pyiomes.py
    > set FLASK_ENV=development
    > flask run

Options:
  --version  Show the flask version
  --help     Show this message and exit.
 
 
 
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
import ast
import sys
#import xml.etree.ElementTree as ET  #used by loadiome
import iome.iome as io
from iome.tasks import runjob

app = Flask(__name__)

print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: " , str(sys.argv))

#sysarg -i is input xmlfile by default reads iome.xml

#init server




jobtype=1

@app.route("/hello")
def hello():
    return "Hello World!"

#@app.route('/submit', methods=['GET', 'PUT'])
@app.route('/submit', methods=['GET'],)
def submit():

    #load dictionary of elements
    xmlfile="testsimfile.xml"
    inparams=ast.literal_eval(request.args.get('data', ''))    
    
    if io.processinputs(xmlfile, 'simfile.xml', inparams) == 0:
        print("Processed inputs")
    else:
        return("Processing fault: Check input string")
        
    #Next do the job submission
    #method1 submit script for system - generic scheduler
    if jobtype == 0:
        print("Generic Job submitted")
        res=runjob()
        #method2 use celery and rabbitmq for job submission
    elif jobtype == 1:
        print("Job submitted")
        res=runjob.delay()
        
    if res==0:
        return "Jobsubmitted"
    else:
        return "Jobfailed"






