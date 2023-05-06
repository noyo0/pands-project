# classifier.py
# Author: Norbert Antal
# Classify iris species based on the sample values of petal lengths.

# ------------- load modules  --------------
#import numpy as np # for mathematicalfunctions
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


# ------------Classifier visualisation
def fn_classifiervisualiser(a_number,text):
    # ref: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.boxplot.html
    pL = headers[2] #"petal length (cm)"
    plt.style.use("classic") # ref galery: http://tonysyu.github.io/raw_content/matplotlib-style-gallery/gallery.html
    plt.figure(figsize=(10,3.5),facecolor='white', frameon=False,)
    plt.title("Position of Sample value")
    for i in irises:
        min_petal_lengths = df.loc[df['species'] == i][pL].min()
        max_petal_lengths = df.loc[df['species'] == i][pL].max()
        med_petal_lengths = df.loc[df['species'] == i][pL].quantile(0.25) #left side of the box is the end of the first quantile
        l_toboxplot=df.loc[df['species'] == i][pL]
        plt.boxplot(x=l_toboxplot,
            vert=False,
            whiskerprops={'color':'blue', 'linestyle':'-', 'lw':0.5}
            )
        plt.tight_layout(pad=0.5)
        plt.xlim(0,8) # set axis min and max to make room for text
        plt.xlabel("Petal length (cm)", size='small')
        plt.yticks([])
        plt.axvline(min_petal_lengths, color='red', linestyle='-',lw=0.5) #minimum petal line
        plt.axvline(max_petal_lengths, color='green', linestyle='-',lw=0.5) #max petal line
        plt.axvline(a_number, color='magenta', linestyle=':',lw=1) # plotting the sample measurement from the classifier
        plt.text(min_petal_lengths,0.75,f'←{i}(min)', color='red', size='small') # min lables
        plt.text(max_petal_lengths+0.01,1.2,f'{i}(max)→', color='green', size='small', ha='right') # max label
        plt.text(med_petal_lengths,0.87,f'{i} (box)', color='#4468a6', size='smaller',ha='left') # med lables
        plt.text(a_number-0.02,1.3,f' ←your sample: ({a_number}cm)\n      {text}',color='black',bbox=dict(facecolor='magenta', alpha=0.175, edgecolor='white', pad=0.5), size='small') # classifier sample label
    plt.show()
# ------------CLassifier routine + boxplot display of sample
def fn_classify():
    userinput=input(('Please enter the petal length as floating number in cm: \n')) #user defined sample size
    test=float(userinput)
    display = "no match"
    returnme=[]
    petalmeasurements = []# container for min/max tresholds
    typicalmeasurements = []# container for tipical range
    pL = headers[2] #"petal length (cm)"
    for species in df['species'].unique(): #select species individually to filter data
        l_min = df.loc[df['species'] == species][pL].min() # select minimum petal length for matching species
        l_max = df.loc[df['species'] == species][pL].max() # select maximum petal length for matching species
        boxleft = df.loc[df['species'] == species][pL].quantile(0.25) #left side of the box is the end of the first quantile
        boxright = df.loc[df['species'] == species][pL].quantile(0.75) #right side of the box is the end of the third quantile
        petalmeasurements.append([species, l_min, l_max]) # list container for min/max tresholds 
        typicalmeasurements.append([species, boxleft, boxright]) # container for typical range
    #---create tiny dataframes for tresholds---
    criteria = pd.DataFrame(petalmeasurements, columns=['species','Petal Lenght min','Petal Lenght max']) 
    typical = pd.DataFrame(typicalmeasurements, columns=['species','typicalmin','typicalmax'])
    #---check where sample size falls
    result = criteria.loc[(criteria['Petal Lenght min'] <= test) & (criteria['Petal Lenght max'] >= test)]
    typicalsample = typical.loc[(typical['typicalmin'] <= test) & (typical['typicalmax'] >= test)]
    
    if result.empty: #error handling for Empty Dataframe (ref: https://stackoverflow.com/questions/48558511/create-an-exception-for-empty-dataframe)
        print("No matching species in the dataframe for that sample size")
        print(f"\n \t\tClassification criteria: \n\n",criteria)
    else: # output:
        for index, row in result.iterrows(): # iterate if more than one result (ref: https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas)            
            returnme.append(row['species']) #final result
    # output results
    if returnme==[]:# exception handling if no match
        display="not a match"
    else:
        verdict = " or ".join(returnme) # result can be one ore two species
    #    display = " or ".join(returnme) # output with sensible language
    # check for typical:
        if len(returnme) == 1: # if hit list has one member it is checked for typical
            if typicalsample.empty:
                display = f"The sample is likely an {verdict}"
            else:
                display = f"The sample is a typical {verdict}"
        else:
            display = f"The sample is non-typical \n     could be either {verdict}"

    #print(display)
    
    fn_classifiervisualiser(test,display) #run plot with final result and text