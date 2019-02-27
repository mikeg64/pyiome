# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import time
import subprocess

workingdir=str(time.clock())
#workingdir="test"
    
#chdir(m_workingdir);
os.mkdir(workingdir) 
print(os.getcwd() )

#mkdir(jobdir.c_str(),0755);
#sprintf(command,"cp -p iogenericsim.sh %s/iogenericsim.sh",jobdir.c_str());
command="cp -r iogenericsim.sh "+workingdir+"/iogenericsim.sh"
#command="cp iogenericsim.sh iogenericsim1.sh"
subprocess.call([command], shell=True)
#os.system(command)
