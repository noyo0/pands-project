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
SOURCEDATA="iris.data"
#----read in with giving headers to each column-----------------------
headers=[
    "sepal length (cm)", 
    "sepal width (cm)", 
    "petal length (cm)", 
    "petal width (cm)",
    "species"]
df=pd.read_csv(SOURCEDATA, names=headers)

# ----create summary of each variable and output summary.txt-------------
summary=df.describe()
output=(f"THE SUMMARY OF EACH VARIABLE IN THE IRIS DATASHEET\n\n {summary}")
with open('summary.txt','w') as f:
    #f.write("THE SUMMARY OF EACH VARIABLE IN THE IRIS DATASHEET\n",df.describe().to_string())
    f.write(output)

# Create histogram of each variable and save results in png files

# create a function to draw and save the histograms with column data as variable and column name as file name
def fn_pnghist(column):
    plt.style.use('fast')
    plt.grid(True, color="#7e9964", linestyle="dotted")
    df[column].hist(bins=10, color="#5a4fcf")
    plt.suptitle(f"Histogram of {column}")
    plt.savefig(f"{column}.png") # save plot ref: https://chartio.com/resources/tutorials/how-to-save-a-plot-to-a-file-using-matplotlib/
    plt.show() # turns out plt.show() must be left in the end of the function to avoide having all histograms on one plot 💁


#create a for loop to cycle through the variables in iris data and call the 'fn_hist' function to draw the histograms with each variable as per their column label
cols=headers[:-1] # created shorter list from 'headers' to avoid including the 'species column' that is not one of the measurements short list stored in 'cols'
for c in cols:
    fn_pnghist(c)

'''
plt.style.use('fivethirtyeight')
plt.legend(facecolor='k', labelcolor='b')
#----- scatter plot for sepal variables
ax_x = "sepal length (cm)"
ax_y = "sepal width (cm)"
sns.scatterplot(data=df,x=ax_x, y=ax_y, hue='species')
plt.show()
#----- scatter plot for petal variables
ax_x = "petal length (cm)"
ax_y = "petal width (cm)"
sns.scatterplot(data=df,x=ax_x, y=ax_y, hue='species')
plt.show()
'''