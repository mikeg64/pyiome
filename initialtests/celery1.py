# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 03:08:33 2019

@author: mike
"""
#first install rabitmq
#http://www.rabbitmq.com/#getstarted
#erlang is needed
#http://www.erlang.org/downloads

#after starting rabitmq server
#follow quick start tutorial
#http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html

#run the worker using
#celery -A tasks worker --loglevel=info

#>>> from tasks import add
#>>> add.delay(4, 4)

#under windows there was an error used the workaround below
#see https://github.com/celery/celery/issues/4081
#pip install eventlet
#celery -A <mymodule> worker -l info -P eventlet


from tasks import add
res=add.delay(5, 4)