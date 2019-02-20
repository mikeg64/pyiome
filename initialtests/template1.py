# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 15:58:59 2019

@author: mike
"""
from flask import Flask, request

import sys
#from app import app



app = Flask(__name__)

@app.route('/')
@app.route("/hello")
def hello():
    return "Hello World!"


@app.route('/submit')
def submit():
    user = {'useremail': 'm.griffiths@sheffield.ac.uk','jobtype': 'QH', 'imagefile': '126519929316b_cal_1.png'}
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
				<string>126519929316b_cal_1.png</string>
			</prop>
			<prop flag="7" index="2" name="jobtype">
				<string>QH</string>
			</prop>
		</props>
		<steps configstepfreq="1" statestepfreq="1">2</steps>
		<fileprops configfilename="configfile.xml" configreadmethod="1" configwritemethod="1" simreadmethod="1" simwritemethod="1" statefilename="statefile.xml" statereadmethod="1" statewritemethod="1"/>
	</simulation>
</iosim>'''

    return job






#<html>
#    <head>
#        <title>Home Page - Microblog</title>
#    </head>
#    <body>
#        <h1>Hello, ''' + user['username'] + '''!</h1>
#    </body>
#</html>'''