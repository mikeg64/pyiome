# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
#r = requests.get("http://localhost:5000/submit?data={'useremail': 'mikeg2107@gmail.com', 'jobtype': 'SH', 'imagefile': 'testimage2.jpg'}")
#r = requests.get("http://localhost:5000/submit?data={ 'jobtype': 'QH', 'imagefile': 'testimage3.jpg'}")

#r = requests.get("http://localhost:5000/submit?data={ 'imagefile': 'testimage3.jpg'}")

#request for docker job
r = requests.get("http://localhost:5000/submit?data={ 'useremail': 'm.griffiths@sheffield.ac.uk','carprop': 'mpg'}")


print(r)
