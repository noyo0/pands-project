# condmeans.py
# Author: Norbert Antal
# program to test running a function from external file

# turns out modules have to be imported for the function to work elsewhere
import pandas as pd # for data analysis
import matplotlib.pyplot as plt # for creating graphical representation of data
import seaborn as sns # # for creating prettier graphical representation of data

# and the data has to be loaded as well even if it is already loaded in the host code 🤷‍♀️
SOURCEDATA="iris.data"
headers=[ 
    "sepal length (cm)", 
    "sepal width (cm)", 
    "petal length (cm)", 
    "petal width (cm)",
    "species"]
df=pd.read_csv(SOURCEDATA, names=headers) 

# ----------------------the actual function:
def fn_condmeansext():
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

# end of guest function