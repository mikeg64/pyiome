
Here are the steps that were followed  to install the python library.

   1. The IOME python client kit is dependent on the python xml libraries and the ZSI solera library
   2. The IOME python client library includes the ZSI library components
   3. Add the environment variable IOME_HOME e.g. to .bashrc
   4. Modify the PYTHONPATH variable as follows
   5. export PYTHONPATH=$PYTHONPATH”:$IOME_HOME/src



To install ZSI toolkit from a commnad prompt dos or linux
easy_install ZSI...version.egg

Add python distribution scripts directory to path
use the wsdl2py application to generate web service client
and server stubs 

information for installing and using easy_install is at
http://pypi.python.org/pypi/setuptools#using-setuptools-and-easyinstall
