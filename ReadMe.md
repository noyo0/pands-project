# ATU - Programming and Scripting Project 2023

### Author: Norbert Antal

## Summary of the Iris dataset
<br><br>

### Introduction
<br>
The Iris flower data set, also known as Fisher’s Iris data set, is a multivariate data set that was introduced by British statistician and biologist Ronald Fisher. <br>The data was collected by Edgar Anderson to quantify the morphologic variation of Iris flowers of three related species and was utilised by Fisher to demonstrate the use of linear discriminant analysis in his 1936 paper titled “The use of multiple measurements in taxonomic problems” published in the Annals of Eugenics.
<br>Today the dataset is widely used as a typical test case for statistical classification in machine learning. 
The Iris dataset contains 50 samples of three Iris flower species: Iris setosa, Iris virginica, and Iris versicolor. Each sample has four features measured in centimetres: sepal and petal length and width. Using these four variables, Ronald Fisher developed a linear discriminant model to differentiate between the species.<br>
(ref: https://en.wikipedia.org/wiki/Iris_flower_data_set )
<br>

### Modules used for this project

+ **numpy** - is a library for adding support for large, multi-dimensional arrays along with a large collection of high-level mathematical functions to operate on these arrays (ref: https://en.wikipedia.org/wiki/NumPy)
+ **pandas** - for data manipulation and analysis (ref: https://en.wikipedia.org/wiki/Pandas_(software))
+ **matplotlib** - for creating graphical representation of data (ref: https://en.wikipedia.org/wiki/Matplotlib)
+ **seaborn** - also for graphical data representation with extended finctionality and styling options (ref: https://en.wikipedia.org/wiki/Matplotlib)

### Datasource:

**iris.data** and **iris.names** files downloaded from https://archive.ics.uci.edu/ml/datasets/iris in a comma-separated value file format
<br>

### Reading in data
Data will be analysed using mainly Pandas which is a popular data analysis library in Python that provides user-friendly data structures and data analysis tools. The comma separated value file is converted to Pandas DataFrame which is a two-dimensional table with labelled columns and rows, similar to a spreadsheet. (ref: https://towardsdatascience.com/a-python-pandas-introduction-to-excel-users-1696d65604f6)

Iris flower measurement values are imported from **iris.data**, header lables added manually from **iris.names** and the two combined into a pandas dataframe. <br>

### Data validation and structure

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
<br>

<br>

+ #### **Checking for Null entries:**

| Column             | Null Entries |
|--------------------|--------------|
| sepal length (cm)  | 0            |
| sepal width (cm)   | 0            |
| petal length (cm)  | 0            |
| petal width (cm)   | 0            |
| species            | 0            |

It appears that the datafdrame contains 150 value entries per column, 4 columns contain floating point numbers and one contains text data and there is an added index column that is assigned by pandas automatically when creating the dataframe. (Automatic indexing ref: https://blog.hubspot.com/website/pandas-indexing)
<br>
In the subsequent check "Checking for Null entries", it was found that there are no Null entries in the dataframe. <br> Null entries can cause unexpected results with calculations, comparison of data and pandas functions. (Dealing with Null values ref: https://medium.com/geekculture/dealing-with-null-values-in-pandas-dataframe-1a67854fe834)

#### **Snapshot wiew**

<br>

|   | sepal length (cm) | sepal width (cm) | petal length (cm) | petal width (cm) | species       |
|---|--------------------|-------------------|--------------------|-------------------|-----------------|
| 0 | 5.1                | 3.5               | 1.4                | 0.2               | Iris-setosa    |
| 1 | 4.9                | 3.0               | 1.4                | 0.2               | Iris-setosa    |
| 2 | 4.7                | 3.2               | 1.3                | 0.2               | Iris-setosa    |
| 3 | 4.6                | 3.1               | 1.5                | 0.2               | Iris-setosa    |
| 4 | 5.0                | 3.6               | 1.4                | 0.2               | Iris-setosa    |
<br>

It seems the added headers make logical sense, floating point numbers are under flower measurements and species names are under species.<br>
The dataframe apperas to be ready for further analyis.

<br>
## Project task 1. Output a summary of each variable to a single text file
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
<br>(ref: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html)
<br>(ref: https://www.w3schools.com/python/pandas/ref_df_describe.asp#:~:text=The%20describe()%20method%20returns,std%20%2D%20The%20standard%20deviation)