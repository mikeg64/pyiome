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
import xml.etree.ElementTree as ET  #used by loadiome
import iome.iome as io

app = Flask(__name__)

print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: " , str(sys.argv))

#sysarg -i is input xmlfile by default reads iome.xml

#init server




todos = {}
Params = {}
requests = {}


@app.route("/hello")
def hello():
    return "Hello World!"

#@app.route('/submit', methods=['GET', 'PUT'])
@app.route('/submit', methods=['GET'],)
def submit():

    #load dictionary of elements
    xmlfile="testsimfile.xml"
    xmldic=io.loadiome(xmlfile)
    
    props=xmldic[1]
    tree=xmldic[0]
    
    #tree = ET.parse("simfile.xml")
    #root = tree.getroot()
    
    #print(props)
    #user={}
    
    root = tree.getroot()
    #print('here1')
    #propse=ET.SubElement(root,'props')
    #print('here2')
    i=0
    #user = {'useremail': 'm.griffiths@sheffield.ac.uk','jobtype': 'QH', 'imagefile': '126519929316b_cal_1.png'}
    inparams=ast.literal_eval(request.args.get('data', ''))
    print("inparams")
    print(len(inparams))
    print(inparams)

    #only remove elements from the xml tree if the 
    #dictionary fields are in the xml file
    #for child in root.iter('prop'):
    #    for val in child.iter('string'):
    #        attribs=child.attrib
    #        sname=attribs['name']
            #for dname in inparams:
            #    if dname == sname:
            #        child.remove(val)
        
    
    for prope in root.iter('prop'):
    #for i in range(len(props)-1):
        prop=props[i]
        
        i=i+1
        try:
            #user[prop['name']]=inparams[prop['name']]
            
            #prope=ET.SubElement(propse,'prop')
            
            #print('prope')
            #print(prope)
            #print("%s - %s -%s" % (prope.tag, prope.text, prope.attrib))
            #nstringe=stringe
            #prope.remove(stringe)
            #propse.remove(prope)
            
            #print("before %s - %s - %s" % (stringe.tag, stringe.text, stringe.attrib))
            #stringe.clear()
            #prope.set(prop['name'],inparams[prop['name']])
            for val in prope.iter('string'):
                attribs=prope.attrib
                sname=attribs['name']
                for dname in inparams:
                    print("sname and dname")
                    print(dname)
                    print(sname)
                    if dname == sname:
                        prope.remove(val)  #remove the element because we are about to add a new one
                        stringe=ET.SubElement(prope,'string')                                                
                        stringe.text=inparams[prop['name']]
                        print("after %s - %s - %s" % (stringe.tag, stringe.text, stringe.attrib))
                        print(stringe.text)
                        print('set attrib')
                        print(prop['name'])
                        print(inparams[prop['name']])
            
        except:
            print('except')
            #print(user[prop['name']])
            #user[prop['name']]='test.default'
            
    
    print(inparams)
    io.writeiome('simfile.xml',tree)
    
    return prop['name']







