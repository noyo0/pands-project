# ATU - Programming and Scripting Project 2023

### Author: Norbert Antal

## Summary of the Iris dataset
<br><br>

### Introduction
<br>
The Iris flower data set, also known as Fisher’s Iris data set, is a multivariate data set that was introduced by British statistician and biologist Ronald Fisher. <br>The data was collected by Edgar Anderson to quantify the morphologic variation of Iris flowers of three related species and was utilised by Fisher to demonstrate the use of linear discriminant analysis in his 1936 paper titled “The use of multiple measurements in taxonomic problems” published in the Annals of Eugenics.
<br>Today the dataset is widely used as a typical test case for statistical classification in machine learning.<br> 
The Iris dataset contains 50 samples of three Iris flower species: Iris setosa, Iris virginica, and Iris versicolor. Each sample has four features measured in centimetres: sepal length and width and petal length and width. Using these four variables, Ronald Fisher developed a linear discriminant model to differentiate between the species.<br>
(ref: https://en.wikipedia.org/wiki/Iris_flower_data_set )
<br>

### Python Program (analysis.py) for analysis of the Iris data 

The program **analysys.py** can be found and executed from the root directory. 

- The main functions of the program can be accessed from the main menu:

1. Data validation
2. Summary of each variable
3. Display and save a histogram of each varaible
4. Display a scatter plot of each pair of variables
5. Conditional means
6. Correlation - Heatmap
7. Boxplot
8. Classifier routine

The relevant *Program menu* will be noted under the title of each section of the analyis.
Output from the program is saved in the root folder. Filenames will be noted at the relevant sections as well.

### Modules used for this project

+ **pandas** - for data manipulation and analysis (ref: https://en.wikipedia.org/wiki/Pandas_(software))
+ **matplotlib** - for creating graphical representation of data (ref: https://en.wikipedia.org/wiki/Matplotlib)
+ **seaborn** - also for graphical data representation with extended finctionality and styling options (ref: https://en.wikipedia.org/wiki/Matplotlib)

### Data source:

Source files downloaded from https://archive.ics.uci.edu/ml/datasets/iris 
The source file **iris.data** is in a comma-separated value file format without headers, **iris.names** is a brief description of the dataset which contains information regarding the headers for the data. 

### Reading in data
Data will be analysed using mainly Pandas which is a popular data analysis library in Python that provides user-friendly data structures and data analysis tools. The comma separated value file is converted to Pandas DataFrame which is a two-dimensional table with labelled columns and rows, similar to a spreadsheet. (ref: https://towardsdatascience.com/a-python-pandas-introduction-to-excel-users-1696d65604f6)

Iris flower measurement values are imported from **iris.data**, header lables added manually from the data description in **iris.names** and the two combined into a pandas dataframe. <br>

### Data validation and structure 
#### (Program menu: 1.)

The resulting dataframe is checked for anomalies such as missing or Null entries or unsuitable data formats and a general information on its structure<br>

+ #### **Dataframe info:**


| Column             | Non-Null Count | Dtype   |
|--------------------|----------------|---------|
| sepal length (cm)  | 150            | float64 |
| sepal width (cm)   | 150            | float64 |
| petal length (cm)  | 150            | float64 |
| petal width (cm)   | 150            | float64 |
| species            | 150            | object  |

Data columns (total 5 columns):

| #  | Column            | Non-Null Count | Dtype  
---  |------             |--------------  |-----  
| 0  | sepal length (cm) | 150 non-null   | float64
| 1  | sepal width (cm)  | 150 non-null   | float64
| 2  | petal length (cm) | 150 non-null   | float64
| 3  | petal width (cm)  | 150 non-null   | float64
| 4  | species           | 150 non-null   | object 

Dtypes: 
float64(4)
object(1)

Memory usage: 6.0+ KB

+ #### **Checking for Null entries:**

| Column             | Null Entries |
|--------------------|--------------|
| sepal length (cm)  | 0            |
| sepal width (cm)   | 0            |
| petal length (cm)  | 0            |
| petal width (cm)   | 0            |
| species            | 0            |

It appears that the dataframe contains 150 value entries per column, 4 columns contain floating point numbers and one contains text data and there is an added index column that is assigned by pandas automatically when creating the dataframe. (Automatic indexing ref: https://blog.hubspot.com/website/pandas-indexing)
In the subsequent check "Checking for Null entries", it was found that there are no Null entries in the dataframe. <br> Null entries can cause unexpected results with calculations, comparison of data and pandas functions. (Dealing with Null values ref: https://medium.com/geekculture/dealing-with-null-values-in-pandas-dataframe-1a67854fe834)

+ #### **Snapshot view of the created Dataframe**

<br>

|   | sepal length (cm)  | sepal width (cm)  | petal length (cm)  | petal width (cm)  | species        |
|---|--------------------|-------------------|--------------------|-------------------|----------------|
| 0 | 5.1                | 3.5               | 1.4                | 0.2               | Iris-setosa    |
| 1 | 4.9                | 3.0               | 1.4                | 0.2               | Iris-setosa    |
| 2 | 4.7                | 3.2               | 1.3                | 0.2               | Iris-setosa    |
| 3 | 4.6                | 3.1               | 1.5                | 0.2               | Iris-setosa    |
| 4 | 5.0                | 3.6               | 1.4                | 0.2               | Iris-setosa    |

<br>

Output shows that the added headers make logical sense, floating point numbers are under flower measurements and species names are under species.<br>
The dataframe appears to be ready for further analysis.

<br>

## Project task 1. Output a summary of each variable to a single text file 
#### (Program menu: 2.) - Output saved in **summary.txt**
<br>
Pandas DataFrame describe() method returns a description of the data in the DataFrame. The description -if the data is numeric- contains the following information: 

+ count - The number of not-empty values.
+ mean - The average (mean) value.
+ std - The standard deviation.
+ min - the minimum value.
+ 25% - The 25% percentile*.
+ 50% - The 50% percentile*.
+ 75% - The 75% percentile*.
+ max - the maximum value.

(ref: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html)
(ref: https://www.w3schools.com/python/pandas/ref_df_describe.asp#:~:text=The%20describe()%20method%20returns,std%20%2D%20The%20standard%20deviation)

Initial summary reveals that there are 150 values for each measurement which makes later comparisons easier. It also shows that based on the standard variation (std) figures, sepal width values have the lowest variation and the petal length values have the highest. However, it is more useful to separate these figures by species so the data can be used for comparison.
<br>The describe() method iterated through each of the species provides a more comprehensive view of the data. It shows that every species have an equal number of samples (50) for each of the 4 measurements. This will allow direct comparison without truncating for example. At first glance, differences between species are not significant enough to rely on numeric analysis alone. Graphical representation of the data is more suitable to highlight the differences and similarities among the species...

*As per the project task description, the results of the summary analysis are saved into a text file (summary.txt) that includes both an overall summary of the data and a species-specific summary, divided by title text for ease of readability.*

## Project task 2. Create histogram of each variable and save results in png files 
#### (Program menu: 3.) - output saved in separate image files in >measurement<.png format (eg. sepal width (cm).png)

A histogram is a plot that shows frequency distribution (shape) of a set of values. A histogram in the context of the Iris dataset can visualise the distribution of the various measurement values of the dimensions of the petals and sepals of the Iris flower. (ref: https://statistics.laerd.com/statistical-guides/understanding-histograms.php) <br>
Key characteristics of histograms are *peaks* and *spread* that represent the most typical values and how much the data variates, *skewed data* or presence of *outliers* may indicate patterns that could be investigated or errors in the sample.
(ref: https://chartio.com/learn/charts/histogram-complete-guide/)
+ **Histogram of sepal lengths (cm)**
    The histogram is quite widely spread, slightly skewed to the left towards the smaller values which indicates that sepals with less than the median length are more common than long ones. The data shows three distinct peaks indicating sepal lengths around 5.5cm to be the most common but peaks of sample lengths just under 5cm and between 6.0 and 6.5cm are a frequent occurrence as well.
+ **Histogram of sepal width (cm)**
    This histogram is almost symmetric indicating close to normal distribution and has a narrow spread which is not surprising as standard deviation is the smallest in this category at 0.433594. 
+ **Histogram of petal length (cm)**
    This is a bimodal histogram with two distinct peaks or modes, one at the extreme left indicating a large number of samples with short petals while the other peak is at 4-5cm with a wider base with an almost normal distribution shape. Multimodal histograms could indicate subgroups in the dataset.
+ **Histogram of petal width (cm)**
    This a multimodal histogram although similarly to the previous histogram, there is a distinct cluster at the extreme left showing a significant number of samples with narrow petals, the remaining samples are gathering in an almost separate multimodal shape with multiple peaks.

Since the data is not separated by species the resulting histograms are more suitable to identify outliers and errors but it is worth noting that both histograms representing petal measurements (see: *petal length (cm).png* and *petal width (cm).png*) show a distinct cluster of samples with short and/or narrow petals. 

## Project task 3. Output a scatter plot of each pair of variables
#### (Program menu: 4.) - Output saved in **pairplot.png** and **sepal_petal.png**

A scatter plot uses dots to represent values of two numeric variables, with each dot indicating the values of an individual data point on the horizontal and vertical axis. It is used to visualise relationships between variables.  (ref: https://chartio.com/learn/charts/what-is-a-scatter-plot/) <br>
Pairplot from the Seaborn library of Python is used for creating a grid of scatterplots and histograms, visualizing the pairwise relationships in a dataset. (ref: https://seaborn.pydata.org/generated/seaborn.pairplot.html) The comparison is made easier by having all the pairs of measurements plotted side by side using subplots. Where the same measurement paired, a histogram is drawn. The three separate species are colour coded in order to distinguish which measurement belongs to which Iris species. (pairplot.png) <br>
The pairplot demonstrates that Iris-setosa measurements are showing in their own cluster on multiple plots while versicolor and virginica have overlapping measurements in all.
When comparing petal and sepal measurements in pairs side by side on a separate plot (sepal_petal.png), it is apparent that there is considerable overlap in sepal length and width across the different species. However, in terms of petal measurements, Iris-setosa is clearly separated having the smallest petals, while the majority of the versicolor and virginica samples are also distinct, with only slight overlap between them. Virginica noticeably having the largest petals, both in terms of length and width.
According to the scatter plots, the most effective pair of measurements for distinguishing between the three Iris species is petal width and length.<br>
Scatter plots can also indicate correlation between pairs of variables as demonstrated on the Petal Measurements scatter plot (sepal_petal.png), where a correlation between petal length and width can be observed, revealing that the longer petals tend to be wider as well.


## Project task 4. Any other analysis

### Conditional means 
#### (Program menu: 5.) - Output saved in **condmeans.png**

The "Conditional Means" (condmeans.png) plot is a direct reutilisation of a sample plot from the seaborn plot gallery. 
It is combining a strip plot for each of the flower measurement values and point plot for each of the means figures for each of the values grouped by species. The chart indicates the distinction of Iris-setosa values once again but it doesn't reveal additional information about the data, certainly can't assist with the distinction of the other two species. 

### Correlation - Heatmap
#### (Program menu: 6.) - Output saved in **heatmap.png**

Correlation between the different columns of the data can be calculated using pandas .corr() function which using the Pearson method as default. (ref: https://zion-oladiran.medium.com/exploratory-data-analysis-iris-dataset-68897497b120)  
The Pearson correlation coefficient, that falls between -1 and 1, measures linear correlation. A coefficient of 1 indicates positive correlation, while a coefficient of -1 indicates negative correlation. A coefficient of 0 means that the two variables likely have no effect on each other. (ref: https://www.scribbr.com/statistics/pearson-correlation-coefficient/#:~:text=The%20Pearson%20correlation%20coefficient%20(r,the%20relationship%20between%20two%20variables.) 
The resulting correlation matrix is displayed in terminal output however, a graphical representation of the matrix would help recognising relevant patterns in the data.
A heatmap is a two-dimensional data-representation in which values are represented by colours to show relationships between two variables, one plotted on each axis. (ref: vhttps://chartio.com/learn/charts/heatmap-complete-guide/)
Such plot can be used for the representation of a correlation matrix, showing the relationships between pairs of variables as a grid of colored squares. Each square's colour represents the value of the correlation coefficient.
Using seaborn .heatmap plot function the resulting heatmap reveals that there is a strong positive correlation (0.96) between petal length and petal width, as well as between sepal length and petal length and width (0.87 and 0.82). 
This indicates that the larger petals retain their proportions as they grow in size since the wider they are their length increases. Also revealed that a flower with a longer sepal will likely have a larger petal. 
Sepal width has a weak negative correlation with petal length and petal width. This suggests that the sepals may become slightly narrower as the petals grow in size. 

### Petal Lenght and width measuement distribution among the species - Box plot
#### (Program menu: 7.) - Plot saved in **boxplot.png**, petal measurement tresholds ranges for each species output to the terminal

A boxplot (or box and whisker plot) is the visualisation of data distribution based on five attributes; minimum, first quartile, median, third quartile and maximum. (ref: https://builtin.com/data-science/boxplot) The box represents the central 50% of the data with a line representing the median value, while the whiskers cover the remaining range of the data. Outliers are plotted outside the whiskers range as individual points. ˙ref: https://chartio.com/learn/charts/box-plot-complete-guide/)
As previous visualisations demonstrated, petal measurements are the most useful to distinguish the species therefore the box plot only focuses on petal lenght and width divided into two subplot arranged vertically. The three species are plotted on the same subplot for easier comparison. 
Once again, Iris-setosa shown completely separately on both subplots, just as it did in the scatter plots. The other two species also demonstrate the same overlap as before.
However, unlike the scatter plot that was very informative with regards to individual datapoints, the box plot provides a comprehensive picture of the data distribution, showing the median, typical values, and outliers.
Typical values or the central 50% of the datapoints show distinction between versicolor and virginica although 

Since the petal length data gives a wider range of values than the petal width data, it is more suitable to focus on the petal lengths for classification purposes.

### Summary and proposed practical use of findings
#### (Program menu: 8. Classifier routine) Classification result output to terminal also a visualisation saved as **classification.png**

This project analysed Fisher's Iris dataset, originally published in 1936 describing 3 species of the Iris flower.
The data was downloaded and converted into a dataframe and after an initial "health-check" it was analysed using python's pandas library. Matplotlib and seaborn libraries were used for visualisation of the data.
The summary of each variable has not revealed anything useful although in retrospect petal lenght already noticeable with the highest standard deviation figure indicating the widest variation of values. Grouping the data per species ultimately was used in the classification proces but without graphical illustration it was difficult make sense of the data.
First visualisation was a histogram for each measurement. It revealed that petal measurements produce bi- and multimodal histograms suggesting possible grouping within the data especially on the lower range of values.
The pairplot produced from the data creating a grid of scatterplots and histograms for each pair of measurements with a colourcode for each species was much more revelative. Petal measurements for Iris-setosa very clearly stand apart while the other two species show some overlap. A general correlation between petal length and width was also revealed.
In further analysis a combnination plot was created to display conditional means along with the individual datapoints however this plot did not bring any furter insight other than reinforcing the separation of Iris-setosa samples.
For the next plot a correlation analysis was carried out and the resulting heatmap plot revealed that the petals keep their proportions as they get bigger since lenght and width and it is also indicated that flowers with larger petals are likely to have longer sepals.
As previously the sepal data proven to be ambiguous, the last visualisation focused on petal measurements only.
The two boxplots revealed the typical measurements for each species along with the minimum and maximum measurements and the outliers. 

#### Findings:

+ Only one of the three Iris species; Iris-setosa can be clearly separated based on the minimum and maximum size of petals.
+ While the other two species have overlapping data for petal dimansions, the analysis was able to establish a range for typical petal lengths and widths for the three species and visualised on a box plot: 
  + Iris-setosa typical petal lenght is between 1.4-1.58cm, 
  + Iris-versicolor is between 4.0-4.6cm and 
  + Iris-virginica petal lenght is between 5.1-5.88cm. 
+ A strong correlation demonstrated on scatterplots and heatmap visualiation between petal widths and legths indicate that across the three species the petals keep their proportions regardless of overall size.
+ A correlation demonstrated on a heatmap plot suggests that iris flowers with bigger petals likely to heve longer sepals.

#### Practical use of the data:
##### (Program menu: 8. Classifier routine)

If we were to identify species in future samples of Iris flowers without counting chromosomes we can use the min and max measurements of petal dimensions for each species to separate them and leave only the overlapping ones for chromosome counting.
Based on petal measurements grouped by species and classifier routin was created (Program menu: 8. Classifier routine)
Since petal lenghts have a much wider variety it is the basis of the program.
The user can enter the petal length of a new sample as a floating point number, and receive the name of the species that the sample likely belongs to, based on whether the petal length falls within the range of the minimum and maximum values of that species. If it falls into an overlapping range, both relevant species are listesd.
The program is complete with a plot that displays the ranges of each species with a box plot and the position of the new sample data.







