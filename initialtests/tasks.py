# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 03:01:04 2019

@author: mike
"""
#see comments on celery1.py
from celery import Celery

#rabbit mq server
#app = Celery('tasks', broker='pyamqp://guest@localhost//')

#redis server
app = Celery('tasks', broker='redis://localhost//')

@app.task
def add(x, y):
    print(x+y)
    return x + y
