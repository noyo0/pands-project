# analysis.py
# Author: Norbert Antal

## Program functions:  
# reads in Fisher’s Iris data set
# Outputs a summary of each variable to a single text file,  
# Saves a histogram of each variable to png files, and  
# Outputs a scatter plot of each pair of variables.  
# Performs other appropriate analysis (conditional means, heatmap, boxplot)
# Provides a sample classification routine with visualisation

## References: 
# pandas documentation: https://pandas.pydata.org/pandas-docs/stable/
# pandas tutorial ref: https://www.youtube.com/watch?v=vmEHCJofslg&t=111s
# matplotlib tutorial ref: https://www.youtube.com/watch?v=DAQNHzOcO5A
# matplotlib with pandas ref: https://www.youtube.com/watch?v=0P7QnIQDBJY
# RA Fisher's original paper: https://digital.library.adelaide.edu.au/dspace/bitstream/2440/15227/1/138.pdf
# >>> Further references on individual problems are in line with the code or noted in the ReadMe.md file.

# ------------- load modules  --------------
import pandas as pd # for data analysis and dataframe
import matplotlib.pyplot as plt # for creating graphical representation of data
import seaborn as sns # for creating graphical representation of data
import os # for the clear screen function

#----read in data and give headers to each column, creating a dataframe-----------------------
SOURCEDATA="iris.data" # store path of source file in global variable (file is in the same folder so only file name here)
#----read in data and add headers to each column-----------------------
headers=[ #adding headers to dataframe (later reused as global variable for filtering) (headers taken from iris.names)
    "sepal length (cm)", 
    "sepal width (cm)", 
    "petal length (cm)", 
    "petal width (cm)",
    "species"]
df=pd.read_csv(SOURCEDATA, names=headers) # creating dataframe
# store species names globally for later use in filtering 
irises = df['species'].unique() #unique function ref: https://www.educative.io/answers/what-is-the-unique-function-in-pandas

# ------------Create usermenu
# User Menu ref: Week06 Practice - Studentmanagement.py
# return keyword ref: https://www.w3schools.com/python/ref_keyword_return.asp
# execute function stored as string ref: https://www.geeksforgeeks.org/exec-in-python/
# get list index numbers ref: https://towardsdatascience.com/looping-in-python-5289a99a116e#:~:text=Using%20the%20enumerate()%20Function&text=The%20enumerate()%20function%20takes,(the%20default%20is%200).&text=And%20that's%20it!
# update dictionary ref: https://thispointer.com/python-how-to-add-append-key-value-pairs-in-dictionary-using-dict-update/
# dictionary from list (zip) ref: https://stackoverflow.com/questions/209840/how-can-i-make-a-dictionary-dict-from-separate-lists-of-keys-and-values
def UserMenu():
    os.system('clear') # clear screen for better readability ref: https://www.geeksforgeeks.org/clear-screen-python/
    print('''
Welcome to Iris data analysis companion suite :)
Author: Norbert Antal - 2023
    ''')
    while UserMenu != None: #loop until user entry has match in list
        menu=[ #menu item structure: menu text, expected value from user, function to run stored as text
            {"menuTxt":"1. Data validation", "menuVal":"1", "function": "fn_datavalidation()"},
            {"menuTxt":"2. Summary of each variable" , "menuVal":"2", "function": "fn_textsummary()"},
            {"menuTxt":"3. Display and save a histogram for each varaible", "menuVal":"3", "function": "fn_makehists()"},
            {"menuTxt":"4. Display a scatter plot of each pair of variables", "menuVal": "4", "function": "fn_scatters()"},
            {"menuTxt":"5. Conditional means","menuVal": "5", "function": "fn_condmeans()"},
            {"menuTxt":"6. Correlation - Heatmap","menuVal": "6", "function": "fn_heatmap()"},
            {"menuTxt":"7. Measurement distribution - BoxPlot","menuVal": "7", "function": "fn_boxplot()"},
            {"menuTxt":"8. Classifier routine - please try it, it's wonderful!","menuVal": "8", "function": "fn_classifier()"},
            {"menuTxt":"Q - Quit","menuVal": "Q", "function": "exit()"},
            {"menuTxt":"","menuVal": "q", "function": "exit()"}, #cheated a little so lower case q and empty entry also quits the program
            {"menuTxt":"","menuVal": "", "function": "exit()"}
            ]   
        print("\n USER MENU:\n") #user interaction, indicate expected entry
        for m in menu: #display menu items by iterating through menu list
            print(m["menuTxt"]) # and print each      
        UserSelect=input("\n Please select menu number 1-8 (or Q to quit):")# userinteraction - asking for input and store same in "UserSelect"
        for m in menu: # iterate through menu items to find match
            if UserSelect==m["menuVal"]: #if "UserSelect" matches "menu" list item:
                os.system('clear') # clear screen for better readability ref: https://www.geeksforgeeks.org/clear-screen-python/
                print("\n✓ ",m["menuTxt"]) #user feedback - confirm selection
                return(m["function"]) #return selected function as text to run with exec(Usermenu())
        # if there is no match, the function stays in the while loop until there is one 
        # hence the variations that will return the exit() command to prevent user getting stuck 

# -----user interaction after function finished: Return to menu or quit?
def fn_continue():
    userinput=input("Do you want to quit? (Q or any key) or Back to the Menu? (M)") #user interaction indicating expected entries
    if userinput=="M" or userinput=="m": # little cheat so user can use lowercase as well
        exec(UserMenu()) #exec will run whatever function is returned as string to UserMenu()
    else:
        exec(exit()) # exit program if user enters anything but M or m
#-------------------------end of function

# 1.---- Data Validation -------------
# commands to check for anomalies and to show the created dataframe structure
# ref: https://www.tutorialspoint.com/exploratory-data-analysis-on-iris-dataset
def fn_datavalidation(): 
    print("\n-------> dataframe structure: \n")
    print(df.head()) # first 5 lines of data
    print("\n-------> dataframe info: \n")
    print(df.info()) #outputs column names, count of non-null values and datatypes
    print("\n-------> Checking for Null entries: \n")
    print(df.isnull().sum()) #outputs the number of null entries in the dataframe
    print("\n")
    fn_continue()# return to menu or quit
#-------------------------end of function

# 2.---- create summary of each variable and output to summary.txt-------------
def fn_textsummary(): 
    #describe ref: (https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html)
    #output to string ref: https://stackoverflow.com/questions/31247198/python-pandas-write-content-of-dataframe-into-text-file
    print(f"THE SUMMARY OF EACH VARIABLE IN THE IRIS DATASHEET:\n\n{df.describe().to_string()}")
    print(f"\n\n\nTHE SUMMARY OF EACH VARIABLE BY SPECIES IN THE IRIS DATASHEET:\n")
    for i in irises: #irises is a global variable containing species names only
        #lookup/conditional filtering ref: https://www.kdnuggets.com/2022/12/five-ways-conditional-filtering-pandas.html
        # anatomy: dataframe.LOC[dataframe[lookuparray] == lookupvalue][returnarray].function() or functions
        print(f"\n\t\t\t\t\t{i}\n\n{df.loc[df['species']==i][headers[0:4]].describe().to_string()}\n") 
    print("\nOutput also saved in summary.txt\n") # tell user where to find output file
    with open('summary.txt','w') as f: #write formatted summaries to file
        f.write(f"THE SUMMARY OF EACH VARIABLE IN THE IRIS DATASHEET:\n\n{df.describe().to_string()}")
        f.write(f"\n\n\nTHE SUMMARY OF EACH VARIABLE BY SPECIES IN THE IRIS DATASHEET:\n")
        for i in irises:# write formatted summaries for each species using lookup/conditional filtering
            f.write(f"\n\t\t\t\t\t{i}\n\n{df.loc[df['species']==i][headers[0:4]].describe().to_string()}\n")
    fn_continue() # return to menu or quit
#-------------------------end of function

# 3.------- Create histogram of each variable and save results in png files  - 2 segments A, B
    
    # 3A. ------First set up histogram template
def fn_pnghist(column): # part of histogram sequence - draws one histogram with column name stored in column argument
    # ref: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.hist.html
    # ref: https://www.geeksforgeeks.org/how-to-set-plot-background-color-in-matplotlib/
    # ref: https://matplotlib.org/stable/tutorials/introductory/customizing.html
    plt.style.use('fast') # select style from style galery
    plt.grid(True, color="#7e9964", linestyle="dotted") # set grid on + style and colour
    df[column].hist(bins=10, color="#5a4fcf") # draw histogram for each column with column name taken from argument
    plt.suptitle(f"Histogram of {column}")
    plt.savefig(f"{column}.png") # save plot ref: https://chartio.com/resources/tutorials/how-to-save-a-plot-to-a-file-using-matplotlib/
    plt.show() # turns out plt.show() must be left in the end of the function to avoide having all histograms on one plot 💁
    print(f"\nPlot saved as <{column}.png>\n") # user feedback - display filename so user knows what to look for
#-------------------------end of function
    
    # 3B. ------Iterate template through each measurement column;
        # by calling the 'fn_pnghist' function to draw the histograms with each variable as per their column label
def fn_makehists():
    cols=headers[:-1] # created shorter list from 'headers' to avoid including the 'species column' that is not one of the measurements short list stored in 'cols'
    for c in cols: # loop through list and store header names
        fn_pnghist(c)
    fn_continue() # return to menu or quit
#-------------------------end of function
#--------------------end of segment 3.

# 4.------ Display a scatter plot of each pair of variables - 3 segments A, B, C
    # 4A.------Pair plot for each pair of measurements
def fn_pairplot(): #pairplot ref: https://www.youtube.com/watch?v=b7JuBsswDlo&t=45s
    plt.style.use('fast') # set style
    sns.pairplot(df, hue="species")  # create pairplot ref: https://seaborn.pydata.org/generated/seaborn.pairplot.html
    specfont1 = {"family":"serif","color":"#4a6741",'weight':'bold',"size":14} # set font style
    plt.suptitle("Pair plot of measurements in the Iris dataset", fontdict=specfont1) # set title
    plt.subplots_adjust(top=0.95) # reducing size of the plot to make more room for the title.
    #------output to -png
    plt.savefig(f"pairplot.png")
    plt.show(block = False)
    plt.pause(7) #plot only showed in jupyter, workaround ref: https://pythonguides.com/matplotlib-not-showing-plot/
    plt.close('all') # this is not ideal but program stucks otherwise
    print("\n Plot saved as <pairplot.png>\n")
#-------------------------end of function

    # 4B.------ Display a scatter plot for sepal and petal measurement pairs separately
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
    print("\n Plot saved as <sepal_petal.png>\n")
#-------------------------end of function

    # 4C.------- display and save both versions of the scatter plots
def fn_scatters():
    fn_sepal_petal()# run sepal and petal scatterplots first
    fn_pairplot() # then pairplot
    fn_continue() # return to menu function
#-------------------------end of function
#--------------------end of segment 4.

# 5.----------Conditional means from external file
# this is for testing code partitioning and external functions
def fn_condmeans():
    from condmeans import fn_condmeansext # importing a function from external file <condmeans.py>
    fn_condmeansext() # run the function to draw "conditional means" plot
    fn_continue() # return to menu function
#-------------------------end of function

# 6.------ Correlation - Heatmap
def fn_heatmap():
    # correlation heatmap ref: https://zion-oladiran.medium.com/exploratory-data-analysis-iris-dataset-68897497b120
    correlation = df.corr() # calculate correlation with corr() ref: https://www.geeksforgeeks.org/python-pandas-dataframe-corr/
    # text report
    print(f"\nCorrelation matrix:\n{correlation}")
    # title 
    plt.figure(figsize=(7,5)) # set figure size
    plt.subplots_adjust(top=0.90,left=0.2, bottom=0.28) # adjusting plot to fit title and labels
    plt.suptitle("Correlation - Heatmap", fontdict={"family":"serif","color":"#4a6741",'weight':'bold',"size":12})# set title and style
    # heatmap
    sns.heatmap(correlation, annot=True, cmap='Greens') # render heatmap
    plt.tight_layout() # prevent lable overlaps
    # save to file
    plt.savefig("heatmap.png")
    plt.show()
    print("\n Plot saved as <heatmap.png>\n") # userfeedback - file name
    fn_continue() # return to menu function
#-------------------------end of function

# 7.------------------Measurement distribution box plot
def fn_boxplot():
    # print a list of petal measurement ranges (min/max) per species:
        # pandas tutorial to filter data ref: https://www.youtube.com/watch?v=vmEHCJofslg&t=111s
        # limit describe output to min and max ref: https://stackoverflow.com/questions/19124148/modify-output-from-python-pandas-describe, 
    for i in irises: #irises is a global variable containing species names only
        # filter/lookup anatomy: dataframe.LOC[dataframe[lookuparray] == lookupvalue][returnarray].function() or functions
        # this lookpup filters petal lenght and width (header[2:4]) where species equals to the current iteration in the irises loop 
        # then applies two arguments (min and max) of the describe() function
        # prints the iterations of the loop (species name) the header names and the min/max value for each iteration
        print(i,'\n',df.loc[df['species']==i][headers[2:4]].describe().loc[['min','max']]) 

    # plot the boxlplot:
    #ref: https://www.youtube.com/watch?v=q68Qundmans&t=3076s
    #ref: https://www.geeksforgeeks.org/box-plot-in-python-using-matplotlib/
    plt.style.use("classic") # ref galery: http://tonysyu.github.io/raw_content/matplotlib-style-gallery/gallery.html
    pL = headers[2] #"petal length (cm)"
    pW = headers[3] #"petal width (cm)"
    fig, axs = plt.subplots(2, 1, figsize=(10, 5), facecolor='white') # plotting 2 subplots on top of each other, classic with white background

    for i in irises: # iterating through species #irises is a global variable containing species names only
        petal_lengths = df.loc[df['species'] == i][pL] #filter to petal lenghts per species
        petal_widths = df.loc[df['species'] == i][pW] #filter to petal widths per species
        med_petal_lengths = df.loc[df['species'] == i][pL].median() # minimum petal lenghts per species for label position
        med_petal_widths = df.loc[df['species'] == i][pW].median() # minimum petal widths per species for label position
        # top plot 
        axs[0].boxplot(x=petal_lengths, vert=False) # draw boxplot of lenghts, place it horizontally
        axs[0].set_title(f"{pL} by Species") # set title from variables
        axs[0].set_xlabel(pL,size='smaller') # # set axis lable from variables
        axs[0].set_xlim(0,7) # Aligning the two axes to make comparison easier
        axs[0].text(med_petal_lengths,0.75,f'{i}', color='grey', size='small', ha='center') # set, position and style labels
        
        # bottom plot
        axs[1].boxplot(x=petal_widths, vert=False)
        axs[1].set_title(f"{pW} by Species")
        axs[1].set_xlabel(pW, size='smaller')
        axs[1].set_xlim(0,7) 
        axs[1].text(med_petal_widths,0.75,f'{i}', color='grey', size='small', ha='center') 

    plt.tight_layout()
    plt.savefig("boxplot.png")
    print("\n Plot saved as <boxplot.png>\n")
    plt.show()
    fn_continue() # return to menu function
#-------------------------end of function


# 8.-----------------------------THE WONDERFUL CLASSIFIER

    #8.A------internal (try again) menu for classifier 
    # function allows user to try multiple samples without restarting the program or using the main menu
def fn_continue_classifier():
    userinput=input("\nQuit to Menu? (Q or any key) or try again? (Y)") #user interaction indicating expected entries
    if userinput=="Y" or userinput=="y": # little cheat so user can use lowercase as well
        fn_classifier() # start classifier again
    else:
        exec(UserMenu()) # exit program if user enters anything but M or m
#-------------------------end of function

    # 8.B------the classifier is a two part (classifier and visualiser) routine partitioned externally
from classifier import fn_classify
# The functions for the classifier routine were saved as a separate file and loaded back into analysis.py to test if it reduces loading time
    # online references were inconclusive:
        # Partitioning improves performance ref: https://gamedev.stackexchange.com/questions/203710/does-having-code-spread-in-multiple-files-decrease-performance
        # Partitioning has little effect ref: https://stackoverflow.com/questions/1083105/does-creating-separate-functions-instead-of-one-big-one-slow-processing-time
# It was found that there was no significant change in loading time for analysis.py by partitioning classifier.py (also condmeans.py) to separate files
    # Perhaps the overall amount of code is so little that partitioning has no menaingfull effect.
def fn_classifier(): # saving function in separate file <classifier.py> to reduce loading time (it made very little difference 😞)
        #function descritpion for user
    os.system('clear')
    #user interaction, brief
    print('''
Iris classification 

The user can receive the species name based on petal length value. 
This determination is made based on whether the petal length falls within the range of the minimum and maximum values of that species.
The output text is updated dynamically based on whether the sample matches any of the species' petal lengths.
If there is no match, the text indicates this and lists the minimum and maximum ranges for each species' petal lengths. 
If the sample falls within an overlapping range, both relevant species are listed. 
Finally, if sample value falls within a species' typical range, the output text indicates this as well.
    ''')
    fn_classify() # classification routine and visualisation - notes in the file <classifier.py> 
    fn_continue_classifier() # internal -try again- menu


#--------- Program run -------------
exec(UserMenu())
