# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 15:58:59 2019

@author: mike
"""
from flask import Flask, request

#import sys
import ast
#from app import app

#http://localhost:5000/submit?data={'useremail': 'mikeg2105@gmail.com', 'jobtype': 'SH', 'imagefile': 'testimage.jpg'}

app = Flask(__name__)

@app.route('/')
@app.route("/hello")
def hello():
    return "Hello World!"


@app.route('/submit')
def submit():
    #inparams = request.args.get('data', '')
    #inparams=ast.literal_eval("{'muffin' : 'lolz', 'foo' : 'kitty'}")
    user = {'useremail': 'm.griffiths@sheffield.ac.uk','jobtype': 'QH', 'imagefile': '126519929316b_cal_1.png'}
    inparams=ast.literal_eval(request.args.get('data', ''))
    try:
        user['useremail']=inparams['useremail']
    except:
        user['useremail']='m.griffiths@sheffield.ac.uk'
        
    try:
        user['jobtype']=inparams['jobtype']
    except:
        user['jobtype']='QH'   
        
        
    try:
        user['imagefile']=inparams['imagefile']
    except:
        user['imagefile']='shadingcor.jpg' 
        
    
    #user = {'useremail': 'm.griffiths@sheffield.ac.uk','jobtype': 'QH', 'imagefile': '126519929316b_cal_1.png'}
    job = '''
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- edited with XMLSPY v5 U (http://www.xmlspy.com) by Michael Kenneth Griffiths (Self Employed) -->
<iosim filename="iocaimanphp.xml">
	<simulation class="GenericSteerSimulation" createmethod="1" name="mysim" nprocs="1" simulantclass="AgentModel" simulanttype="0">
		<props flag="7" name="" numprops="3">
			<prop flag="7" index="0" name="useremail">
				<string>'''+user['useremail']+'''</string>
			</prop>
			<prop flag="7" index="1" name="imagefile">
				<string>'''+    user['imagefile']   +'''</string>
			</prop>
			<prop flag="7" index="2" name="jobtype">
				<string>'''+ user['jobtype']  +'''</string>
			</prop>
		</props>
		<steps configstepfreq="1" statestepfreq="1">2</steps>
		<fileprops configfilename="configfile.xml" configreadmethod="1" configwritemethod="1" simreadmethod="1" simwritemethod="1" statefilename="statefile.xml" statereadmethod="1" statewritemethod="1"/>
	</simulation>
</iosim>'''

#    return job
    return user['useremail']

    #todisplay an image or get ouput
    #http://localhost:5000/hellotest?text=timetogetlouis%20now 
@app.route("/hellotest")
def hellotest(): 
    return "You said: " + request.args.get('text', '')




#<html>
#    <head>
#        <title>Home Page - Microblog</title>
#    </head>
#    <body>
#        <h1>Hello, ''' + user['username'] + '''!</h1>
#    </body>
#</html>'''