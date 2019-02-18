# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 07:37:34 2019

@author: mike


# pyiomes
#Client and test calls to server


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
import xml.etree.ElementTree as ET  #used by loadiome

import sys
print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: " , str(sys.argv))

#sysarg -i is input xmlfile by default reads iome.xml

#init server

#load dictionary of elements
{root,props}=loadiome("simfile.xml")

app = Flask(__name__)
api = Api(app)

todos = {}
Params = {}
requests = {}

class TodoSimple(Resource):
    
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}
    
class Submit(Resource):
    
    def get(self, Request):
        return {Request: requests[Request]}

    def put(self, Request):
        requests[Request] = request.form['data']
        return {Request: todos[Request]}

class Param(Resource):
    
    def get(self, Param):
        return {Param: todos[Param]}

    def put(self, Param):
        Params[Param] = request.form['data']
        return {Param: Params[Param]}    
    
    

api.add_resource(TodoSimple, '/<string:todo_id>')
api.add_resource(Submit, 'Submit/<string:Request>')
api.add_resource(Param, 'Param/<string:Param>')



if __name__ == '__main__':
    app.run(debug=True)


def loadiome(xmlfile):
    # empty dictionary
    props = {}
    xmldic = {}
    
    #with open(xmlfile) as fd:
    #    doc = xmltodict.parse(fd.read())

    tree = ET.parse(xmlfile)
    root = tree.getroot()

    for child in root.iter('props'):
        print(child)
        print(child.tag)
        print(child.attrib)
        print(child.get('numprops'))

    #create a dictionary

    id=1
    for child in root.iter('prop'):
        print(child)
        print(child.tag)
        print(child.attrib)
        test=child.attrib
    for val in child.iter('string'):
        print(val.tag)
        print(val.attrib)
        print(val.text)
        prop={}
        prop['val']=val.text
        prop['type']='string'
        prop['name']=test['name']
        props[id]=prop
        id=id+1
   
    xmldic={root,props}
    
    
    
    
    return xmldic

