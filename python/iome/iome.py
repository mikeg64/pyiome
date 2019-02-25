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
    
def processinputs(filetemplate, fileoutput, inputparameters):
    
    #load dictionary of elements
    #xmlfile="testsimfile.xml"
    xmldic=loadiome(filetemplate)
    
    props=xmldic[1]
    tree=xmldic[0]
    
    #tree = ET.parse("simfile.xml")
    #root = tree.getroot()
    
    #print(props)
    #user={}
    
    root = tree.getroot()
    #print('here1')
    #propse=ET.SubElement(root,'props')
    #print('here2')
    i=0
    #user = {'useremail': 'm.griffiths@sheffield.ac.uk','jobtype': 'QH', 'imagefile': '126519929316b_cal_1.png'}
    #inparams=ast.literal_eval(request.args.get('data', ''))
    #print("inparams")
    #print(len(inparams))
    #print(inparams)

    #only remove elements from the xml tree if the 
    #dictionary fields are in the xml file
    #for child in root.iter('prop'):
    #    for val in child.iter('string'):
    #        attribs=child.attrib
    #        sname=attribs['name']
            #for dname in inparams:
            #    if dname == sname:
            #        child.remove(val)
        
    
    for prope in root.iter('prop'):
    #for i in range(len(props)-1):
        prop=props[i]
        
        i=i+1
        try:
            #user[prop['name']]=inparams[prop['name']]
            
            #prope=ET.SubElement(propse,'prop')
            
            #print('prope')
            #print(prope)
            #print("%s - %s -%s" % (prope.tag, prope.text, prope.attrib))
            #nstringe=stringe
            #prope.remove(stringe)
            #propse.remove(prope)
            
            #print("before %s - %s - %s" % (stringe.tag, stringe.text, stringe.attrib))
            #stringe.clear()
            #prope.set(prop['name'],inparams[prop['name']])
            for val in prope.iter('string'):
                attribs=prope.attrib
                sname=attribs['name']
                for dname in inputparameters:
                    print("sname and dname")
                    print(dname)
                    print(sname)
                    if dname == sname:
                        prope.remove(val)  #remove the element because we are about to add a new one
                        stringe=ET.SubElement(prope,'string')                                                
                        stringe.text=inputparameters[prop['name']]
                        print("after %s - %s - %s" % (stringe.tag, stringe.text, stringe.attrib))
                        print(stringe.text)
                        print('set attrib')
                        print(prop['name'])
                        print(inputparameters[prop['name']])
            
        except:
            print('except')
            #print(user[prop['name']])
            #user[prop['name']]='test.default'
            
    
    #print(inparams)
    writeiome(fileoutput,tree)
    
    return 0