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
# RA Fisher's original paper: https://digital.library.adelaide.edu.au/dspace/bitstream/2440/15227/1/138.pdf
# >>> Further references on individual problems are noted in the ReadMe.md file.

# ------------- load modules  --------------
import numpy as np # for mathematicalfunctions
import pandas as pd # for data analysis
import matplotlib.pyplot as plt # for creating graphical representation of data
import seaborn as sns # # for creating prettier graphical representation of data

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

# ---- Data Validation -------------
def fn_datavalidation():
    print("\n-------> dataframe structure: \n")
    print(df.head())
    print("\n-------> dataframe info: \n")
    print(df.info()) 
    print("\n-------> Checking for Null entries: \n")
    print(df.isnull().sum()) #outputs the number of null entries in the dataframe
    print("\n")

# ---- create summary of each variable and output summary.txt-------------
def fn_textsummary(): 
    #describe ref: (https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html)
    #output to string ref: https://stackoverflow.com/questions/31247198/python-pandas-write-content-of-dataframe-into-text-file
    irises=df['species'].unique() 
    #unique function ref: https://www.educative.io/answers/what-is-the-unique-function-in-pandas
    print(f"THE SUMMARY OF EACH VARIABLE IN THE IRIS DATASHEET:\n\n{df.describe().to_string()}")
    print(f"\n\n\nTHE SUMMARY OF EACH VARIABLE BY SPECIES IN THE IRIS DATASHEET:\n")
    for i in irises:
        print(f"\n\t\t\t\t\t{i}\n\n{df.loc[df['species']==i][headers[0:4]].describe().to_string()}\n") 
        #conditional filtering ref: https://www.kdnuggets.com/2022/12/five-ways-conditional-filtering-pandas.html
    print("Output also saved in summary.txt")
    with open('summary.txt','w') as f:
        f.write(f"THE SUMMARY OF EACH VARIABLE IN THE IRIS DATASHEET:\n\n{df.describe().to_string()}")
        f.write(f"\n\n\nTHE SUMMARY OF EACH VARIABLE BY SPECIES IN THE IRIS DATASHEET:\n")
        for i in irises:
            f.write(f"\n\t\t\t\t\t{i}\n\n{df.loc[df['species']==i][headers[0:4]].describe().to_string()}\n")

# ------- Create histogram of each variable and save results in png files 
def fn_pnghist(column):
    plt.style.use('fast')
    plt.grid(True, color="#7e9964", linestyle="dotted")
    df[column].hist(bins=10, color="#5a4fcf")
    plt.suptitle(f"Histogram of {column}")
    plt.savefig(f"{column}.png") # save plot ref: https://chartio.com/resources/tutorials/how-to-save-a-plot-to-a-file-using-matplotlib/
    plt.show() # turns out plt.show() must be left in the end of the function to avoide having all histograms on one plot 💁
    print(f"\nPlot saved as <{column}.png>")

# ------ create a for loop to cycle through the variables in iris data and call the 'fn_hist' function to draw the histograms with each variable as per their column label
def fn_makehists():
    cols=headers[:-1] # created shorter list from 'headers' to avoid including the 'species column' that is not one of the measurements short list stored in 'cols'
    for c in cols:
        fn_pnghist(c)

# ------ Display a scatter plot of each pair of variables
def fn_pairplot():
    plt.style.use('fast')
    sns.pairplot(df, hue="species")
    specfont1 = {"family":"serif","color":"#4a6741",'weight':'bold',"size":14}
    plt.suptitle("Pair plot of measurements in the Iris dataset", fontdict=specfont1) # set title
    plt.subplots_adjust(top=0.95) # reducing size of the plot to make more room for the title.
    #------output to -png
    plt.savefig(f"pairplot.png")
    plt.show(block = False)
    plt.pause(7) #plot only showed in jupyter, workaround ref: https://pythonguides.com/matplotlib-not-showing-plot/
    plt.close('all')
    print("\n Plot saved as <pairplot.png>")
    
# ------ Display a scatter plot for sepal and petal measurement pairs separately
def fn_sepal_petal():
#-----Set plot style 
    plt.style.use('fast') #ref: https://matplotlib.org/stable/gallery/style_sheets/index.html
    plt.rc("font", family="serif")# default text style ref: customise default style ref: https://stackoverflow.com/questions/3899980/how-to-change-the-font-size-on-a-matplotlib-plot
    #-----two plots side by side ref: https://realpython.com/python-matplotlib-guide/#subplots, ref: https://stackoverflow.com/questions/42818361/how-to-make-two-plots-side-by-side
    fig, axes = plt.subplots(ncols=2, figsize=(12, 6)) #create a plot object with 2 subplots (specified in 'ncols') and set plotsize 12x6
    #-----1. draw scatter plot for sepal variables which are the first two headers stored in 'ax_x' and 'ax_y'
    ax_x = headers[0] #"sepal width (cm)"
    ax_y = headers[1] #"sepal length (cm)"
    sns.scatterplot(data=df, x=ax_x, y=ax_y, hue='species', ax=axes[0])
    #-----labels and title for above
    axes[0].set_xlabel(ax_x)
    axes[0].set_ylabel(ax_y)
    axes[0].set_title("Sepal Measurements")
    #-----2. draw scatter plot for petal variables which are the next two headers stored in 'ax_x' and 'ax_y'
    ax_x = headers[2] #"petal width (cm)"
    ax_y = headers[3] #"petal length (cm)"
    sns.scatterplot(data=df, x=ax_x, y=ax_y, hue='species', ax=axes[1])
    #-----labels and title for above
    axes[1].set_xlabel(ax_x)
    axes[1].set_ylabel(ax_y)
    axes[1].set_title("Petal Measurements")
    #------output to -png
    plt.savefig(f"sepal_petal.png")
    plt.show()
    print("\n Plot saved as <sepal_petal.png>")

# ------- display and save both versions of the scatter plots
def fn_scatters():
    fn_sepal_petal()
    fn_pairplot()

    


# ------- Correlation Heatmap
def fn_heatmap():
    # calculate correlation
    correlation = df.corr()
    # text report
    print(correlation)
    # title 
    plt.figure(figsize=(7,5))
    plt.subplots_adjust(top=0.90,left=0.2, bottom=0.28) # adjusting plot to fit title and labels
    plt.suptitle("Correlation - Heatmap", fontdict={"family":"serif","color":"#4a6741",'weight':'bold',"size":12})
    # heatmap
    sns.heatmap(correlation, annot=True, cmap='Greens')
    # save to file
    plt.savefig("heatmap.png")
    plt.show()
    print("\n Plot saved as <heatmap.png>")

#---!!!! ------ Program run -------------

#MENU 
# 1. Datavalidation ---> fn_datavalidation()
# 2. Summary of each variable ---> fn_textsummary()
# 3. Display and save a histogram of each varaible ---> fn_makehists()
# 4. Display a scatter plot of each pair of variables --> fn_pairplot()
# 5. Correlation - Heatmap

fn_scatters()

