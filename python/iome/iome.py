# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 16:53:42 2019

@author: mike
"""
import xml.etree.ElementTree as ET  #used by loadiome

def loadiome(xmlfile):
    # empty dictionary
    props = {}
    xmldic = {}
    
   
    #with open(xmlfile) as fd:
    #    doc = xmltodict.parse(fd.read())

    tree = ET.parse(xmlfile)
    root = tree.getroot()

    for child in root.iter('props'):
        print(child)
        print(child.tag)
        print(child.attrib)
        print(child.get('numprops'))

    #create a dictionary

    id=1
    for child in root.iter('prop'):
        print(child)
        print(child.tag)
        print(child.attrib)
        test=child.attrib
    for val in child.iter('string'):
        print(val.tag)
        print(val.attrib)
        print(val.text)
        prop={}
        prop['val']=val.text
        prop['type']='string'
        prop['name']=test['name']
        props[id]=prop
        id=id+1


    f = open(xmlfile,"r")
    job = f.read() 
   
    xmldic=[]
    xmldic.append(root)
    xmldic.append(props)
    xmldic.append(job)    
    
    
    
    
    return xmldic

