# analysis.py.py
# Author: Norbert Antal

## Program functions:  
# reads in Fisher’s Iris data set
# Outputs a summary of each variable to a single text file,  
# Saves a histogram of each variable to png files, and  
# Outputs a scatter plot of each pair of variables.  
# Performs other appropriate analysis

## References: 
# pandas documentation: https://pandas.pydata.org/pandas-docs/stable/
# pandas tutorial ref: https://www.youtube.com/watch?v=vmEHCJofslg&t=111s
# matplotlib tutorial ref: https://www.youtube.com/watch?v=DAQNHzOcO5A
# matplotlib with pandas ref: https://www.youtube.com/watch?v=0P7QnIQDBJY
# add headers ref: https://www.geeksforgeeks.org/how-to-add-header-row-to-a-pandas-dataframe/
# inspiration: https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/
# RA Fisher's original paper: https://digital.library.adelaide.edu.au/dspace/bitstream/2440/15227/1/138.pdf

# ------------- load modules  --------------
import numpy as np # for mathematicalfunctions
import pandas as pd # for data analysis
import matplotlib.pyplot as plt # for creating graphical representation of data
import seaborn as sns # # for creating prettier graphical representation of data
import os # for file operations

# ------------- load data and add headers --------------
sourcedata="iris.data"
df=pd.read_csv(sourcedata, names=[ # ref: header names taken from "iris.names"
    "sepal length (cm)", 
    "sepal width (cm)", 
    "petal length (cm)", 
    "petal width (cm)",
    "species"])

# ------------- analysis  --------------
described=df.describe()
#print(test.loc[test.index=='std']) # standard dev only
print(described)

# ------------- plot  --------------
#test.loc[test.index == "std"].plot(kind='bar') # bar plot without 'count' series
df["sepal length (cm)"].hist()
'''sns.scatterplot( # scatter plot with selected variables
    x="sepal length (cm)", 
    y="sepal width (cm)",
    hue='species',
    data=df)
plt.legend(bbox_to_anchor=(1, 1), loc=0) # placing plot legend'''
plt.show()

'''# ------------- save results to txt file  --------------
FILENAME ="analysisReport.txt"
if os.path.exists(FILENAME):
    with open(FILENAME, "wt") as f:
        f.write(test)
else:
    with open(FILENAME, "wt") as f:
        f.write(df.describe())'''