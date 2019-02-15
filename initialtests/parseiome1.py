# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 21:33:16 2019

@author: suilven
"""

import xml.etree.ElementTree as ET
import xmltodict

input_file = "simfile.xml"
with open(input_file) as fd:
    doc = xmltodict.parse(fd.read())

tree = ET.parse(input_file)
root = tree.getroot()

for child in root.iter('props'):
    print(child)
    print(child.tag)
    print(child.attrib)
    print(child.get('numprops'))

# empty dictionary
props = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
#my_dict = {'name': 'John', 1: [2, 4, 3]}

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

#newprop=ET.Element()
testchild=root[0][0]
newprop=ET.Element('prop',{'flag': '7', 'index': '4', 'name': 'newvar'})
newstrprop=ET.Element('string')
newstrprop.text='somecrap'
newprop.append(newstrprop)
testchild.append(newprop)
#create dictionary of properties       
for child in root.iter('prop'):
    print(child)
    print(child.tag)
    print(child.attrib)
    for val in child.iter('string'):
        print(val.text)


temp=props[3] 
print(temp['val'])
print(temp['name'])
print(temp['type'])   

tree.write("new.xml")


#insert an element


#for child in root:
#    print(child.tag)
#    print(child.attrib)
#    sim=child.tag

#for child in sim:
#    print(child.tag)
#    print(child.attrib)    
#""
#lst1 = tree.findall("*")
#lst2 =tree.findall()
#for item1 in lst1:
#    print('flag:',item1.get('flag'))
#    print('index:',item1.get('index'))
#    print('name:',item1.get('name'))
#    for item1_tags_and_nd in item1.iter('string'):
#        print(item1_tags_and_nd.get('k') + ":", item1_tags_and_nd.get('v'))
#""

""
#result_list = []
#for item in tree.findall("./prop"):
#    dictionary = {}
#    dictionary['flag'] = item.get('flag')
#    dictionary['index'] = item.get('index')
#    dictionary['name'] = item.get('name')
#    result_list.append(dictionary)
    
#result_list = [{k: item.get(k) for k in ('flag', 'index', 'name')}
#               for item in tree.findall("./prop")]    