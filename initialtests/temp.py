# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests

""" another example """
"""import requests"""

""" a post request example"""

"""
curl -d @request.json --header "Content-Type: application/json" https://www.googleapis.com/qpxExpress/v1/trips/search?key=mykeyhere
"""
url = 'https://www.googleapis.com/qpxExpress/v1/trips/search?key=mykeyhere'
payload = open("request.json")
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=payload, headers=headers)


"""
could invoke fn like server payload as

curl -H "Content-Type: application/json" -d '{"name":"Bob"}' http://localhost:8080/t/pythonapp/pythonfn-trigger
"""
"""
see link
https://fnproject.io/tutorials/python/intro/
"""



r = requests.get("http://localhost:5000/submit?data={'useremail': 'mikeg2107@gmail.com', 'jobtype': 'SH', 'imagefile': 'testimage2.jpg'}")
#r = requests.get("http://localhost:5000/submit?data={ 'jobtype': 'QH', 'imagefile': 'testimage3.jpg'}")

#r = requests.get("http://localhost:5000/submit?data={ 'imagefile': 'testimage3.jpg'}")

#request for docker job
#r = requests.get("http://localhost:5000/submit?data={ 'useremail': 'm.griffiths@sheffield.ac.uk','carprop': 'mpg'}")


print(r)




