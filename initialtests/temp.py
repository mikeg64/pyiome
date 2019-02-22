# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
r = requests.get("http://localhost:5000/submit?data={'useremail': 'mikeg2106@gmail.com', 'jobtype': 'QH', 'imagefile': 'testimage.jpg'}")
print(r)