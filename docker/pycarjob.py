
# coding: utf-8

# ![title](Header__0009_1.png "Header")
# ___
# # Chapter 1 - Data Munging Basics
# ## Segment 5 - Grouping and data aggregation

# In[25]:

import iome.iome as iom
import io
import numpy as np
import pandas as pd
from pandas import Series, DataFrame






# ### Grouping data by column index

# In[26]:

xmlfile="/home/pyio/data/simfile.xml"
outfile="/home/pyio/data/outfile.txt"
xmldic=iom.loadiome(xmlfile)

#print(xmldic[2])
props=xmldic[1]
prop0=props[0]
prop2=props[2]
print(prop0['val'])
print(prop2['val'])

address = 'mtcars.csv'
cars = pd.read_csv(address)

cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
cars.head()


# In[29]:

#selectedcolumn='mpg'
selectedcolumn=prop2['val']
# object_name.groupby('Series_name')
# ♔┈♔┈♔┈( WHAT THIS DOES )┈♔┈♔┈♔
# To group a  DataFrame by its values in a particular column, call the .groupby() method off of the DataFrame, and then pass
# in the column Series you want the DataFrame to be grouped by.
cars_groups = cars.groupby(cars['cyl'])
carmeans=cars_groups.mean()
print(carmeans)

print(carmeans[selectedcolumn])


#write to data folder
scm=carmeans.to_json()
file=open(outfile,'w')
file.write(scm)
file.close()






