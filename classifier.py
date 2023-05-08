# classifier.py
# Author: Norbert Antal
# Classify iris species based on user defined sample petal length values.

# The functions for the classifier routine were saved as a separate file and loaded byck into analysis.py to test if it reduces loading time
    # online references were inconclusive:
        # Partitioning improves performance ref: https://gamedev.stackexchange.com/questions/203710/does-having-code-spread-in-multiple-files-decrease-performance
        # Partitioning has little effect ref: https://stackoverflow.com/questions/1083105/does-creating-separate-functions-instead-of-one-big-one-slow-processing-time
# It was found that there was no significant change in loading time for analysis.py by partitioning classifier.py (also condmeans.py) to separate files
    # Perhaps the overall amount of code is so little that partitioning has no menaingfull effect.

# ------------- load modules  --------------
import pandas as pd # for dataframe and analysis
import matplotlib.pyplot as plt # for creating boxplot

# ------------- load data and add headers --------------
SOURCEDATA="iris.data"
#----read in data and give headers to each column, creating a dataframe-----------------------
headers=[ #adding headers to dataframe (headers taken from iris.names) + can be reused as global list variable in filtering
    "sepal length (cm)", 
    "sepal width (cm)", 
    "petal length (cm)", 
   "petal width (cm)",
    "species"]
df=pd.read_csv(SOURCEDATA, names=headers) # creating dataframe
#  store species names globally for later use in filtering
irises = df['species'].unique() # unique function ref: https://www.educative.io/answers/what-is-the-unique-function-in-pandas

# ------------Classifier visualisation with box plot
# this function visualises the petal lenght data distribution on a boxplot for each species
# displays plot lines for minimum and maximum range of petal lengths for each species
# also displays the relative position of the sample data taken from the classifier routine including sample classification description
def fn_classifiervisualiser(a_number,text): 
    # argument stores the sample data from user interaction "a_number" and "text" for formated classification result
    pL = headers[2] # store filter to the third column "petal length (cm) in a short named variable "
    plt.style.use("classic") # style galery ref: http://tonysyu.github.io/raw_content/matplotlib-style-gallery/gallery.html
    plt.figure(figsize=(10,3.5),facecolor='white', frameon=True,) # set figure siz and style
    plt.title("Position of Sample value", color='magenta') # set figure title
    for i in irises: # loop for each species
        # find and store minimum/max and left side of box value among values that are in the same row as species in the loop in the dataframe
            # (this is for the vertical plotlines and labels positions)
        # a value lookup will return a list of values matching lookup criteria:
            # anatomy: variable=dataframe.LOC[dataframe[lookuparray] == lookupvalue][returnarray]
        min_petal_lengths = df.loc[df['species'] == i][pL].min() # adding min() will result the smallest value from the list 
        max_petal_lengths = df.loc[df['species'] == i][pL].max() # adding max() will result the largest value from the list 
        med_petal_lengths = df.loc[df['species'] == i][pL].quantile(0.25) #left side of the box is the end of the first quantile
        # boxplot ref: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.boxplot.html 
        l_toboxplot=df.loc[df['species'] == i][pL] # get data for boxplot by locating each petal lenght value for each species
        plt.boxplot(x=l_toboxplot, # as the boxplot is inside the loop, each species values will be plotted on the same axis
            vert=False, # plot horizontally
            whiskerprops={'color':'blue', 'linestyle':'-', 'lw':0.5} #style the whiskers
            )
        plt.tight_layout(pad=0.5) # prevents labels overlapping ref: https://www.statology.org/matplotilb-tight_layout/
        plt.xlim(0,8) # set axis min and max to make room for text, ref: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html
        plt.xlabel("Petal length (cm)", size='small') # set x axis label
        plt.yticks([]) #hide y axle tick label ref: https://www.geeksforgeeks.org/how-to-hide-axis-text-ticks-or-tick-labels-in-matplotlib/
        # plot lines ref: https://www.geeksforgeeks.org/matplotlib-pyplot-axvline-in-python/
        plt.axvline(min_petal_lengths, color='red', linestyle='-',lw=0.5) # minimum petal line
        plt.axvline(max_petal_lengths, color='green', linestyle='-',lw=0.5) #max petal line
        plt.axvline(a_number, color='magenta', linestyle='solid',lw=3, ymin=0.8) # sample value from the classifier, short line ref: https://www.skytowner.com/explore/drawing_a_vertical_line_in_matplotlib
        # plot line lables - plt.text ref: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html
        plt.text(min_petal_lengths,0.75,f'←{i}(min)', color='red', size='small') # min lables
        plt.text(max_petal_lengths+0.01,1.2,f'{i}(max)→', color='green', size='small', ha='right') # max label
        plt.text(med_petal_lengths,0.87,f'{i} (box)', color='#4468a6', size='smaller',ha='left') # med lables
        plt.text(a_number-0.02,1.3, # classifier sample data label with background colour ref: https://stackoverflow.com/questions/17086847/box-around-text-in-matplotlib
                 f' ←your sample: ({a_number}cm)\n      {text}',
                 color='white',bbox=dict(facecolor='magenta', alpha=0.175, edgecolor='white', pad=1.5), 
                 size='small') 
    plt.savefig("ClassificationResult.png")
    print("Result saved as <ClassificationResult.png>")
    plt.show()

# ------------CLassifier routine ----------------------------------
# function description displayed when the function called
def fn_classify():
    while True: # exception handling ref: https://docs.python.org/3/tutorial/errors.html#handling-exceptions
        try:
            sample=float(input(('Please enter the petal length as floating-point number in cm: \n'))) #user defines sample size
            break
        except ValueError:
            print('Error: invalid entry.\n')
    display = "✕" # default value to display
    returnme=[] # result container for species names
    petalmeasurements = []# container for min/max petal length range
    typicalmeasurements = []# container for tipical petal length range
    pL = headers[2] # store filter to the third column "petal length (cm) in a short named variable "
    # loop for each species
        # find and store values for lable and plotline locations
        # a value lookup will return a list of values matching lookup criteria:
            # anatomy: variable=dataframe.LOC[dataframe[lookuparray] == lookupvalue][returnarray]
            #for species in df['species'].unique()
    for i in irises: #select species individually to filter data
        l_min = df.loc[df['species'] == i][pL].min() # select minimum petal length for matching species
        l_max = df.loc[df['species'] == i][pL].max() # select maximum petal length for matching species
        boxleft = df.loc[df['species'] == i][pL].quantile(0.25) #left side of the box is the end of the first quantile
        boxright = df.loc[df['species'] == i][pL].quantile(0.75) #right side of the box is the end of the third quantile
        petalmeasurements.append([i, l_min, l_max]) # list container for min/max tresholds 
        typicalmeasurements.append([i, boxleft, boxright]) # container for typical range
    #-create tiny dataframes for lookup ranges
    criteria = pd.DataFrame(petalmeasurements, columns=['species','Petal Lenght min','Petal Lenght max']) 
    typical = pd.DataFrame(typicalmeasurements, columns=['species','typicalmin','typicalmax'])
    #-lookups with sample value
    result = criteria.loc[(criteria['Petal Lenght min'] <= sample) & (criteria['Petal Lenght max'] >= sample)]
    typicalsample = typical.loc[(typical['typicalmin'] <= sample) & (typical['typicalmax'] >= sample)]
    #-classification based on lookup results
    if result.empty: #error handling for out of range samples (ref: https://stackoverflow.com/questions/48558511/create-an-exception-for-empty-dataframe)
        plotme=0 # block boxplot function as there is nothing to plot = out of range procedure
    else: # output if there is a match:
        plotme=1 # unblock boxplot function - within range procedure
        for index, row in result.iterrows(): # iterate for more than one result (ref: https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas)            
            returnme.append(row['species']) #result(s) added to the result lilst
        verdict = " or ".join(returnme) # text to express result is two species
        if len(returnme) == 1: # if result only one species it is checked if within typical range
            if typicalsample.empty:
                display = f"The sample is likely an {verdict}" # if not tipical, say it's likely
            else:
                display = f"The sample is a typical {verdict}" # if it is typical 
        else: # if result is not exactly 1, the sample is ambiguous
            display = f"The sample is ambiguous \n     could be either {verdict}" #format text accordingly
    print(display) # output dynamically formatted text to terminal
    
    if plotme == 1: # 0 = out of range procedure, 1 = within range procedure
        fn_classifiervisualiser(sample,display) # within range: run plot with final result and dynamically formatted text
    else: # out of range: user interaction if sample out of range and run classifier function again.
        print('''
                        Sample is out of range
    No matching species in the dataframe for that sample size
        ''')
        print(f"\n \t\tClassification criteria: \n\n",criteria,"\n\n") # remind user of valid range
        print('Please try again:') 
        fn_classify() 

# End of classifier with visualisation program