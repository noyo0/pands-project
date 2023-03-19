# Project_2023.py
# Author: Norbert Antal
# pandas documentation: https://pandas.pydata.org/pandas-docs/stable/
# pandas tutorial ref: https://www.youtube.com/watch?v=vmEHCJofslg&t=111s
# matplotlib tutorial ref: https://www.youtube.com/watch?v=DAQNHzOcO5A
# matplotlib with pandas ref: https://www.youtube.com/watch?v=0P7QnIQDBJY
# add headers ref: https://www.geeksforgeeks.org/how-to-add-header-row-to-a-pandas-dataframe/


"""headers:
   1. sepal length in cm
   2. sepal width in cm
   3. petal length in cm
   4. petal width in cm"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#-------------------read in --------------------------------------------------------------------------------
file="iris practice.data"
df=pd.read_csv(file, names=[
    "sepal length (cm)", 
    "sepal width (cm)", 
    "petal length (cm)", 
    "petal width (cm)",
    "class"])
#------------------------check first 5 lines-------------------------------------------------------
# print(df.head(5))
#-------------------filter --------------------------------------------------------------------------------
##print(df["class"]) print "class" column only
#print(df["class"][145]) 145th entry in "class" column
#----------conditional filtering------------------------------------------------------------------------------------
# print(df.loc[df["petal length (cm)"]>6.1]) # conditional filtering
#------------loop through individual objects---------------------------------------------------------------------------------------
#for index, row in df.iterrows(): # print individually each object
#    print(index, row['class']) #filter to 'class' column
#----------basic statistical-------------------------------------------------------------------------------------------
#print(df.describe()) # gives simple stats of the data.
#-----------basic plotting-------------------------------------------------------------------------------------------
# df.describe().plot(kind="bar") #plots a bar chjart of stats
# plt.show()
#stats = df.describe()
#stats.loc[stats.index != "count"].plot(kind="bar")   #----> plots bar chart without 'counbt' element
#plt.show()
#---------------SORTING -----------------------------------------------------------------------------------------------
#print(df.sort_values(["class","petal width  (cm)"], ascending=[1,0])) # class is ascending, petal widht is descending

#--****------making chnages to data------*****--------------------------------------
#------- add summary column "Total"----------------
#df['Total'] = df["sepal length (cm)"]+df["sepal width (cm)"]+df["petal length (cm)"]+df["petal width (cm)"]
#print(df.head(5))
#--------- remove column "Total" -----------------
#-------------another adding texhinc (quicker)-------(axis=0 (or axis='rows' is horizontal axis. axis=1 (or axis='columns') is vertical axis)--

df["Total"] = df.iloc[:,0:4].sum(axis='columns') # df.iloc[all rows, columns 1-3].sum˛[axis=0 rows, axis=1 columns]---------
print(df.head(5))

