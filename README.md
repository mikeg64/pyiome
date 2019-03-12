# pyiome
Interactive Management Object Library with Python


[IOME, A Toolkit for Distributed and Collaborative Computational Science and Engineering](https://drive.google.com/file/d/0B-AKVl-pk6ziMTJFMTU1OUZCRUQ0QzcyNjowLjE/view)
[IOME, Instructions](https://drive.google.com/file/d/0B-AKVl-pk6ziMTJFMTU0RUYxQjNGNkFCOTowLjE/view)
[CAIMAN paper](https://doi.org/10.1016/j.cmpb.2010.07.007)

Uses python  Flask with RestfulAPI to implement services over the web, datamangement/sharing and for structured markup processing.
[Flask web development framework](http://flask.pocoo.org/)
[Flask Restful API](https://flask-restful.readthedocs.io/en/latest)

[Structured Markup Processing tools for python](https://docs.python.org/3/library/markup.html)
[The Element Tree XML](https://docs.python.org/3/library/xml.etree.elementtree.html)






1. Build docker image


2. Start Redis (if not started) or start RabbitMQ (see 3)

	[Instructions for installing starting and testing REDIS](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-18-04)

	[Install celery redis python client)](http://docs.celeryproject.org/en/latest/getting-started/brokers/redis.html)
        $ pip install -U "celery[redis]"

        Change the linein tasks.py to use correct broker (REDIS or rabbitmq)
        #app = Celery('tasks', broker='pyamqp://guest@localhost//')  #rabbitmq
        app = Celery('tasks', broker='redis://localhost:6379/0')   #redis

	First attempt with redis failed it was necessary to re-install correct version of redis client
	pip install redis==2.10.6

        [celery redis issue solution](https://github.com/celery/celery/issues/5175)

	sudo service redis-server start
	sudo service redis-server stop
	sudo service redis-server status
 
3. Start  RabbitMQ

	# stop the local node
	sudo service rabbitmq-server stop

	# start it back
	sudo service rabbitmq-server start
	# check on service status as observed by service manager
	sudo service rabbitmq-server status
        
        see: https://www.rabbitmq.com/install-rpm.html
             https://www.rabbitmq.com/install-debian.html

4. Start Flask

        export FLASK_APP=pyiomes.py
        export FLASK_ENV=development  #note not for debug mode
        flask run

        http://flask.pocoo.org/docs/1.0/server/
        https://medium.com/@manivannan_data/how-to-deploy-the-flask-app-as-ubuntu-service-399c0adf3606


5. Start celery
        celery -A tasks worker --loglevel=info

        see: http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html#first-steps

        http://docs.celeryproject.org/en/latest/userguide/daemonizing.html

             
