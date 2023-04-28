# ATU - Programming and Scripting Project 2023

### Author: Norbert Antal

## Summary of the Iris dataset
<br><br>

### Introduction
<br>
The Iris flower data set, also known as Fisher’s Iris data set, is a multivariate data set that was introduced by British statistician and biologist Ronald Fisher. <br>The data was collected by Edgar Anderson to quantify the morphologic variation of Iris flowers of three related species and was utilised by Fisher to demonstrate the use of linear discriminant analysis in his 1936 paper titled “The use of multiple measurements in taxonomic problems” published in the Annals of Eugenics.
<br>Today the dataset is widely used as a typical test case for statistical classification in machine learning. 
The Iris dataset contains 50 samples of three Iris flower species: Iris setosa, Iris virginica, and Iris versicolor. Each sample has four features measured in centimetres: sepal length and width and petal length and width. Using these four variables, Ronald Fisher developed a linear discriminant model to differentiate between the species.<br>
(ref: https://en.wikipedia.org/wiki/Iris_flower_data_set )
<br>

### Python Program (analysis.py) for analysis of the Iris data 

The program **analysys.py** can be found and executed from the root directory. 

- The main functions of the program can be accessed from the main menu:

1. Datavalidation
2. Summary of each variable
3. Display and save a histogram of each varaible
4. Display a scatter plot of each pair of variables
5. Correlation - Heatmap
6. ---+++ continue----+++

The relevant *Program menu* will be noted under the title of each section of the analyis.
Output from the program is saved in the root folder. Filenames will be noted at the relevant sections as well.

### Modules used for this project

+ **numpy** - is a library for adding support for large, multi-dimensional arrays along with a large collection of high-level mathematical functions to operate on these arrays (ref: https://en.wikipedia.org/wiki/NumPy)
+ **pandas** - for data manipulation and analysis (ref: https://en.wikipedia.org/wiki/Pandas_(software))
+ **matplotlib** - for creating graphical representation of data (ref: https://en.wikipedia.org/wiki/Matplotlib)
+ **seaborn** - also for graphical data representation with extended finctionality and styling options (ref: https://en.wikipedia.org/wiki/Matplotlib)

### Datasource:

Source files downloaded from https://archive.ics.uci.edu/ml/datasets/iris 
The source file **iris.data** is in a comma-separated value file format without headers, **iris.names** is a brief description of the dataset which contains information regarding the headers for the data. 

### Reading in data
Data will be analysed using mainly Pandas which is a popular data analysis library in Python that provides user-friendly data structures and data analysis tools. The comma separated value file is converted to Pandas DataFrame which is a two-dimensional table with labelled columns and rows, similar to a spreadsheet. (ref: https://towardsdatascience.com/a-python-pandas-introduction-to-excel-users-1696d65604f6)

Iris flower measurement values are imported from **iris.data**, header lables added manually from the data description in **iris.names** and the two combined into a pandas dataframe. <br>

### Data validation and structure 
#### (Program menu: 1.)

The resulting dataframe is checked for anomalies such as missing or Null entries or unsuitable data formats and a general information on its struture<br>

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

+ #### **Snapshot wiew of the created Dataframe**

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
The dataframe apperas to be ready for further analyis.

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
<br>The describe() method iterated through each of the species provides a more comprehensive view of the data. It shows that every species have an equal number of samples (50) for each of the 4 measurements. This will allow direct comparison without truncating for example. However, differences between species are not significant enough to rely on numeric analysis alone. Graphical representation of the data is more suitable to highlight the differences and similarities among the species...

*As per the project task description, the results of the summary analysis are saved into a text file (summary.txt) that includes both an overall summary of the data and a species-specific summary, divided by title text for ease of readability.*

## Project task 2. Create histogram of each variable and save results in png files 
#### (Program menu: 3.) - output saved in separate image files in >measurement<.png format (eg. sepal width (cm).png)

A histogram is a plot that shows frequency distribution (shape) of a set of values.(ref: https://statistics.laerd.com/statistical-guides/understanding-histograms.php) A histogram in the context of the Iris dataset can visualise the distribution of the various measurement values of the dimensions of the petals and sepals of the Iris flower. <br>
Since the data is not separated by species the resulting histograms are more suitable to identify outliers and errors but it is worth notig that on the histograms of the petal lenght and the petal width (see: *petal length (cm).png* and *petal width (cm).png*) a higher frequency of small value measurements can be seen in clusters. Significance of this observation is yet to be determined.

## Project task 3. Output a scatter plot of each pair of variables
#### (Program menu: 4.) - Output saved in **pairplot.png** and **sepal_petal.png**

Pairplot from the Seaborn library of Python is used for creating a grid of scatterplots and histograms, visualizing the relationships between each pair of the Iris measurements. The comparison is made easier by having all the pairs of measurements plotted side by side using subplots. The three separate species are colour coded in order to distinguish which measurement belongs to which Iris species. (pairplot.png) <br>
The pairplot demonstrates that Iris-setosa measurements are showing in their own cluster on multiple plots while versicolor and virginica have overlapping measurements in all.
<br>
Plotting petal and sepal measurements side by side on a separate plot it is more noticeable (sepal_petal.png) that while there is significant overlap in sepal length and width between the species, in case of the petal measurements Iris-setosa very clearly separated and the majority of the versicolor and virginica samples are also stand apart with only marginal overlap. 
Based on the scatter plots the most distinguishing measurement pair to visualise the differences between the three Iris species is the Petal width and length. 







