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
headers=[ #adding headers to dataframe (later reused as global variable for filtering)
    "sepal length (cm)", 
    "sepal width (cm)", 
    "petal length (cm)", 
    "petal width (cm)",
    "species"]
df=pd.read_csv(SOURCEDATA, names=headers) # creating dataframe

irises = df['species'].unique() # store species for later use in filtering

# --------User interaction - Menu ref: Week06 Practice

# error handling with "while" ref: https://programming-21.mooc.fi/part-6/3-errors
# return keyword ref: https://www.w3schools.com/python/ref_keyword_return.asp
# execute function stored as string ref: https://www.geeksforgeeks.org/exec-in-python/
# get list index numbers ref: https://towardsdatascience.com/looping-in-python-5289a99a116e#:~:text=Using%20the%20enumerate()%20Function&text=The%20enumerate()%20function%20takes,(the%20default%20is%200).&text=And%20that's%20it!
# update dictionary ref: https://thispointer.com/python-how-to-add-append-key-value-pairs-in-dictionary-using-dict-update/
# dictionary from list (zip) ref: https://stackoverflow.com/questions/209840/how-can-i-make-a-dictionary-dict-from-separate-lists-of-keys-and-values
def UserMenu():
    while UserMenu != None: #loop until match in list
        menu=[ #menu item structure: ,menu text, expected value from user, function to run stored as text
            {"menuTxt":"1. Data validation", "menuVal":"1", "function": "fn_datavalidation()"},
            {"menuTxt":"2. Summary of each variable" , "menuVal":"2", "function": "fn_textsummary()"},
            {"menuTxt":"3. Display and save a histogram of each varaible", "menuVal":"3", "function": "fn_makehists()"},
            {"menuTxt":"4. Display a scatter plot of each pair of variables", "menuVal": "4", "function": "fn_pairplot()"},
            {"menuTxt":"5. Conditional means","menuVal": "5", "function": "fn_condmeans()"},
            {"menuTxt":"6. Correlation - Heatmap","menuVal": "6", "function": "fn_heatmap()"},
            {"menuTxt":"7. BoxPlot","menuVal": "7", "function": "fn_boxplot()"},
            {"menuTxt":"8. Classifier routine - please try it, it's wonderful!","menuVal": "8", "function": "fn_classifier()"},
            {"menuTxt":"Q - Quit","menuVal": "Q", "function": "exit()"},
            {"menuTxt":"","menuVal": "q", "function": "exit()"}, #cheated a little so lower case q and empty entry also quits the program
            {"menuTxt":"","menuVal": "", "function": "exit()"}
            ]   
        print("\n Please select menu number 1-8 (or Q to quit):\n") #user interaction
        for m in menu: #display menu items by iterating through menu list items
            print(m["menuTxt"])       
        UserSelect=input("\n Please select menu number 1-8 (or Q to quit):")# userinteraction - asking for input and store same
        for m in menu: # iterate through menu items to find match
            if UserSelect==m["menuVal"]: #if there is match:     
                print("\nYou selected",m["menuTxt"]) #user feedback
                return(m["function"]) #return function to run with exec(Usermenu(function)
        # if there is no match we stay in the while loop until there is one

# -----user interaction inside function: Return to menu?

def fn_continiue():
    userinput=input("Do you want to quit? (Q) or Back to the Menu? (M)")
    if userinput=="M" or userinput=="m": # little cheat so user can use lowercase as well
        exec(UserMenu()) #exec will run whatever function is returned as string to UserMenu()
    else:
        exec(exit()) # exit program

# ---- Data Validation -------------

# ref: https://www.tutorialspoint.com/exploratory-data-analysis-on-iris-dataset
def fn_datavalidation(): #all explained in the titles
    print("\n-------> dataframe structure: \n")
    print(df.head()) # first 5 lines of data
    print("\n-------> dataframe info: \n")
    print(df.info()) #outputs column names, count of non-null values and datatypes
    print("\n-------> Checking for Null entries: \n")
    print(df.isnull().sum()) #outputs the number of null entries in the dataframe
    print("\n")
    # return to menu or quit
    fn_continiue()

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
    fn_continiue() #return to menu?

# ------- Create histogram of each variable and save results in png files 

def fn_pnghist(column): #part of histogram sequence - draws one histogram with column name stored in column argument
    # ref: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.hist.html
    # ref: https://www.geeksforgeeks.org/how-to-set-plot-background-color-in-matplotlib/
    # ref: https://matplotlib.org/stable/tutorials/introductory/customizing.html
    plt.style.use('fast') # select style from style galery
    plt.grid(True, color="#7e9964", linestyle="dotted") # set grid on + style and colour
    df[column].hist(bins=10, color="#5a4fcf") # draw histogram for each column with column name taken from argument
    plt.suptitle(f"Histogram of {column}")
    plt.savefig(f"{column}.png") # save plot ref: https://chartio.com/resources/tutorials/how-to-save-a-plot-to-a-file-using-matplotlib/
    plt.show() # turns out plt.show() must be left in the end of the function to avoide having all histograms on one plot 💁
    print(f"\nPlot saved as <{column}.png>") # user feedback - display filename so user knows what to look for

# ------ create a for loop to cycle through the variables in iris data,
# ------- and call the 'fn_pnghist' function to draw the histograms with each variable as per their column label
def fn_makehists():
    cols=headers[:-1] # created shorter list from 'headers' to avoid including the 'species column' that is not one of the measurements short list stored in 'cols'
    for c in cols: # loop through list and store header names
        fn_pnghist(c)

# ------ Display a scatter plot of each pair of variables
def fn_pairplot():
    plt.style.use('fast')
    sns.pairplot(df, hue="species")  #ref: https://seaborn.pydata.org/generated/seaborn.pairplot.html
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
    # correlation heatmap ref: https://zion-oladiran.medium.com/exploratory-data-analysis-iris-dataset-68897497b120
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


# -------------conditional means
def fn_condmeans():
    # seaborn galery ref: https://seaborn.pydata.org/examples/jitter_stripplot.html
    sns.set_theme(style="darkgrid", font='serif') # set style
    # "Melt" the dataset to "long-form" or "tidy" representation
    iris = pd.melt(df, "species", var_name="measurements") # this will put all measurements into one column
    # Initialize the figure
    f, ax = plt.subplots()
    sns.despine(bottom=True, left=True)
    # Show each observation with a scatterplot
    sns.stripplot( 
        data=iris, x="value", y="measurements", palette="Set1",
        dodge=True, alpha=.25, zorder=1
    )
    # Show the conditional means, aligning each pointplot in the
    # center of the strips by adjusting the width allotted to each
    # category (.8 by default) by the number of hue levels
    sns.pointplot(
        data=iris, x="value", y="measurements", hue="species",
        join=False, dodge=.8 - .8 / 3, palette="dark",
        markers="d", scale=.75, errorbar=None
    )
    plt.subplots_adjust(top=0.95,left=0.3) # adjusting plot to fit title and labels
    ax.set_title("Conditional Means") # set title
    # Improve the legend
    sns.move_legend(
        ax, loc="upper left", ncol=1, frameon=True, columnspacing=1, handletextpad=0
    )    
    plt.savefig("condmeans.png")
    plt.show()
    print("\n Plot saved as <condmeans.png>")

# ------------------box plot
def fn_boxplot():

    # - - first a list of minimax data per species:
     # pandas tutorial to filter data ref: https://www.youtube.com/watch?v=vmEHCJofslg&t=111s
    # limit describe output to min and max ref: https://stackoverflow.com/questions/19124148/modify-output-from-python-pandas-describe, 
    irises = df['species'].unique()
    for i in irises:
        print(i,'\n',df.loc[df['species']==i][headers[2:4]].describe().loc[['min','max']]) 

    #  - - then the boxlplot:
    #ref: https://www.youtube.com/watch?v=q68Qundmans&t=3076s
    plt.style.use("classic") # ref galery: http://tonysyu.github.io/raw_content/matplotlib-style-gallery/gallery.html
    l = headers[2] #"petal length (cm)"
    w = headers[3] #"petal width (cm)"
    fig, axs = plt.subplots(2, 1, figsize=(10, 5), facecolor='white') # plotting 2 subplots on top of each other, classic with white background
    for i in irises: # iterating through species
        petal_lengths = df.loc[df['species'] == i][l] #filter to petal lenghts per species
        petal_widths = df.loc[df['species'] == i][w] #filter to petal widths per species
        med_petal_lengths = df.loc[df['species'] == i][l].median() # minimum petal lenghts per species for label position
        med_petal_widths = df.loc[df['species'] == i][w].median() # minimum petal widths per species for label position
        # top plot 
        axs[0].boxplot(x=petal_lengths, vert=False) # draw boxplot of lenghts, place it horizontally
        axs[0].set_title(f"{l} by Species") # set title from variables
        axs[0].set_xlabel(l,size='smaller') # # set axis lable from variables
        axs[0].set_xlim(0,7) # Aligning the two axes to make comparison easier
        axs[0].text(med_petal_lengths,0.75,f'{i}', color='grey', size='small', ha='center') # set, position and style labels
        # bottom plot
        axs[1].boxplot(x=petal_widths, vert=False)
        axs[1].set_title(f"{w} by Species")
        axs[1].set_xlabel(w, size='smaller')
        axs[1].set_xlim(0,7) 
        axs[1].text(med_petal_widths,0.75,f'{i}', color='grey', size='small', ha='center') 

    plt.tight_layout()
    plt.savefig("boxplot.png")
    print("\n Plot saved as <boxplot.png>")
    plt.show()

# ------------Classifier visualisation
def fn_classifiervisualiser(a_number,text):
    # ref: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.boxplot.html
    l = headers[2] #"petal length (cm)"
    plt.style.use("classic") # ref galery: http://tonysyu.github.io/raw_content/matplotlib-style-gallery/gallery.html
    plt.figure(figsize=(10,3),facecolor='white')
    plt.title("Position of Sample value on Petal measurements")
    for i in irises:
        min_petal_lengths = df.loc[df['species'] == i][l].min()
        max_petal_lengths = df.loc[df['species'] == i][l].max()
        med_petal_lengths = df.loc[df['species'] == i][l].quantile(0.25) #left side of the box is the end of the first quantile
        l_toboxplot=df.loc[df['species'] == i][l]
        plt.boxplot(l_toboxplot,
            vert=False,
            whiskerprops={'color':'blue', 'linestyle':'-', 'lw':0.5}
            )
        plt.tight_layout(pad=-5)
        plt.xlim(0,8) # set axis min and max to make rom for text
        plt.axvline(min_petal_lengths, color='red', linestyle='-',lw=0.5) #minimum petal line
        plt.axvline(max_petal_lengths, color='green', linestyle='-',lw=0.5) #max petal line
        plt.axvline(a_number, color='black', linestyle=':',lw=0.5) # plotting the sample measurement from the classifier
        plt.text(min_petal_lengths,0.75,f'←{i}(min)', color='red', size='small') # min lables
        plt.text(max_petal_lengths+0.022,1.2,f'{i}(max)→', color='green', size='small', ha='right') # max label
        plt.text(med_petal_lengths,0.89,f'{i} (box)', color='#4468a6', size='smaller',ha='left') # med lables
        plt.text(a_number-0.04,1.25,f'✕ ←your sample: ({a_number}cm)\n      is {text}',color='black',bbox=dict(facecolor='yellow', alpha=0.15, edgecolor='white', pad=1), size='small') # classifier sample label
    plt.show()
# ------------CLassifier routine + boxplot display of sample
def fn_classifier():
    userinput=input(('Please enter the petal length as floating number in cm: \n')) #user defined sample size
    test=float(userinput)
    returnme=[]
    petalmeasurements = []# container for min/max tresholds
    pL = headers[2] #"petal length (cm)"
    for species in df['species'].unique(): #select species individually to filter data
        l_min = df.loc[df['species'] == species][pL].min() # select minimum petal length for matching species
        l_max = df.loc[df['species'] == species][pL].max() # select maximum petal length for matching species
        petalmeasurements.append([species, l_min, l_max]) # list container for min/max tresholds for display
    #---create a tiny dataframe for tresholds---
    criteria = pd.DataFrame(petalmeasurements, columns=['species','Petal Lenght min','Petal Lenght max']) 
    #---check where sample size falls
    result = criteria.loc[(criteria['Petal Lenght min'] <= test) & (criteria['Petal Lenght max'] >= test)]
    if result.empty: #error handling for Empty Dataframe (ref: https://stackoverflow.com/questions/48558511/create-an-exception-for-empty-dataframe)
        print("No matching species in the dataframe for that sample size")
        print(f"\n \t\tClassification criteria: \n\n",criteria)
    else: # output:
        for index, row in result.iterrows(): # iterate if more than one result (ref: https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas)            
            returnme.append(row['species']) #final result
    print("The sample matches criteria for the following species:")
    if returnme==[]:# exception handling if no match
        display="not a match"
    else:
        display = " or ".join(returnme)
    print(display)
    
    fn_classifiervisualiser(test,display) #run plot with final result and text
    fn_continiue()






#---!!!! ------ Program run -------------

exec(UserMenu())
