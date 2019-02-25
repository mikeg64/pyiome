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

    #for child in root.iter('props'):
    #    print(child)
    #    print(child.tag)
    #    print(child.attrib)
    #    print(child.get('numprops'))

    #create a dictionary

    id=0
    #print('print each prop ')
    for child in root.iter('prop'):
        #print(child)
        #print(child.tag)
        #print('attrib')
        #print(child.attrib)
        attribs=child.attrib
        #print(attribs['name'])
        prop={}
        prop['type']='string'
        prop['name']=attribs['name']
        props[id]=prop
        id=id+1
        for val in child.iter('string'):
            #print(val.text)
            prop['val']=val.text


        #test=child.attrib
    
    #print('print prop set')
    for val in child.iter('string'):
        #print(val.tag)
        #print(val.attrib)
        #print(val.text)
        prop={}
        prop['val']=val.text
        prop['type']='string'
        prop['name']=val.attrib
        props[id]=prop
        #print(len(props))
        id=id+1

    for i in range(id-1):
        prop=props[i]
        #print(i)
        #print(prop['type'])
        #print(prop['name'])
        #print(prop['val'])
        
    f = open(xmlfile,"r")
    job = f.read() 
   
    xmldic=[]
    xmldic.append(tree)
    xmldic.append(props)
    xmldic.append(job)    
    
    
    
    
    return xmldic

def writeiome(xmlfile, tree):
    tree.write(xmlfile)