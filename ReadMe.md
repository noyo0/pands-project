# ATU - Programming and Scripting Project 2023

### Author: Norbert Antal

## **Summary of the Iris Dataset**
<br><br>

## **Introduction**
<br>
The Iris flower data set, also known as Fisher’s Iris data set, is a multivariate data set that was introduced by British statistician and biologist Ronald Fisher. <br>The data was collected by Edgar Anderson to quantify the morphologic variation of Iris flowers of three related species and was utilised by Fisher to demonstrate the use of linear discriminant analysis in his 1936 paper titled “The use of multiple measurements in taxonomic problems” published in the Annals of Eugenics.
<br>Today the dataset is widely used as a typical test case for statistical classification in machine learning.<br> 
The Iris dataset contains 50 samples of three Iris flower species: Iris setosa, Iris virginica, and Iris versicolor. Each sample has four features measured in centimetres: sepal length and width and petal length and width. Using these four variables, Ronald Fisher developed a linear discriminant model to differentiate between the species.<br>
(ref: https://en.wikipedia.org/wiki/Iris_flower_data_set )

<br>

### **Python Program **(analysis.py)** for analysis of the Iris data**
<br>

A Python program **analysys.py** can be found and executed from the root directory (assuming Python is installed on the PC). 

The program starts with a user menu where the main functions of the program can be accessed:

USER MENU:

1. Data validation
2. Summary of each variable
3. Display and save a histogram for each variable
4. Display a scatter plot of each pair of variables
5. Conditional means
6. Correlation - Heatmap
7. Measurement distribution - BoxPlot
8. Classifier routine - please try it, it's wonderful!

The relevant *Program menu* will be noted under the title of each section of the analysis.<br>
Output from the program is saved in the root folder. Filenames will be noted at the relevant sections as well.

## **Preparation**

### Software used for this project

+ VS Code editor
+ Python version 3.9.13 with imported libraries:
  + *pandas* - for data manipulation and analysis (ref: https://en.wikipedia.org/wiki/Pandas_(software))
  + *matplotlib* - for creating graphical representation of data (ref: https://en.wikipedia.org/wiki/Matplotlib)
  + *seaborn* - also for graphical data representation with extended functionality and styling options (ref: https://en.wikipedia.org/wiki/Matplotlib)

### Data source:
Source files downloaded from https://archive.ics.uci.edu/ml/datasets/iris 
The source file **iris.data** is in a comma-separated value file format without headers, **iris.names** is a brief description of the dataset which contains information regarding the headers for the data. 

### Reading in data
Data will be analysed using mainly Pandas which is a popular data analysis library in Python that provides user-friendly data structures and data analysis tools. The comma separated value file is converted to Pandas DataFrame which is a two-dimensional table with labelled columns and rows, similar to a spreadsheet. (ref: https://towardsdatascience.com/a-python-pandas-introduction-to-excel-users-1696d65604f6)

Iris flower measurement values are imported from **iris.data**, header lables added manually from the data description in **iris.names** and the two combined into a pandas dataframe. <br>

### **Data validation and structure**
#### (Program menu: 1.)

The resulting dataframe is checked for anomalies such as missing or Null entries or unsuitable data formats and general information on its structure<br>

+ #### **Dataframe information:**


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

The generated dataframe information indicates that the dataframe contains 150 value entries per column, 4 columns contain floating point numbers and one contains text data and there is an added index column that is assigned by pandas automatically when creating the dataframe. (Automatic indexing ref: https://blog.hubspot.com/website/pandas-indexing)
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

## **Project task 1. Output a summary of each variable to a single text file**
#### (Program menu: 2.) - Output saved in **summary.txt**
<br>
Pyton's Pandas describe() method returns a description of the data in the DataFrame. The description (provided that the data is numeric) contains the following information: 

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

Initial summary reveals that there are 150 values for each measurement which makes later comparisons easier. It also shows that based on the standard variation (std) figures, sepal width values have the lowest variation and the petal length values have the highest. However, this summary doesn't separate the data by species.
<br>The describe() method iterated through each of the species provides a more comprehensive view of the data. It shows that every species have an equal number of samples (50) for each of the 4 measurements. This will allow direct comparison without truncating for example. <br>
The resulting data could be used for further analysis but at first glance, differences between species are not significant enough to rely on numeric analysis alone. Graphical representation of the data is more suitable to highlight the differences and similarities and find correlations in the data.

*As per the project task description, the results of the summary analysis are saved into a text file (summary.txt) that includes both an overall summary of the data and a species-specific summary.*

## **Project task 2. Create histogram of each variable and save results in png files**
#### (Program menu: 3.) - output saved in separate image files in **<*measurement*.png> (e.g. <sepal width (cm).png>)** format

A histogram is a plot that shows frequency distribution (shape) of a set of values. (ref: https://statistics.laerd.com/statistical-guides/understanding-histograms.php) 
<br>A histogram in the context of the Iris dataset can visualize the distribution of the various measurement values of the dimensions of the petals and sepals of the Iris flower.<br>
Key characteristics of histograms are *peaks* and *spread* that represent the most typical values and how much the data variates, *skewed data* or presence of *outliers* may indicate patterns that could be investigated or errors in the sample.
(ref: https://chartio.com/learn/charts/histogram-complete-guide/)
+ **Histogram of sepal lengths (cm)**
    The histogram is quite widely spread, slightly skewed to the left towards the smaller values which indicates that sepals with less than the median length are more common than long ones. The data shows three distinct peaks indicating sepal lengths around 5.5cm to be the most common but peaks of sample lengths just under 5cm and between 6.0 and 6.5cm are a frequent occurrence as well.
+ **Histogram of sepal width (cm)**
    This histogram is almost symmetric indicating close to normal distribution and has a narrow spread which is not surprising as standard deviation is the smallest in this category at 0.433594. 
+ **Histogram of petal length (cm)**
    This is a bimodal histogram with two distinct peaks or modes, one at the extreme left indicating numerous samples with short petals while the other peak is at 4-5cm with a wider base with an almost normal distribution shape. Multimodal histograms could indicate subgroups in the dataset.
+ **Histogram of petal width (cm)**
    This a multimodal histogram although similarly to the previous histogram, there is a distinct cluster at the extreme left showing a significant number of samples with narrow petals, the remaining samples are gathering in an almost separate multimodal shape with multiple peaks.

Since the data is not separated by species the resulting histograms are more suitable to identify outliers and errors, but it is worth noting that both histograms representing petal measurements (see: *petal length (cm).png* and *petal width (cm).png*) show a distinct cluster of samples with short and/or narrow petals. 

## **Project task 3. Output a scatter plot of each pair of variables**
#### (Program menu: 4.) - Output saved in **<pairplot.png>** and **<sepal_petal.png>**

A scatter plot uses dots to represent values of two numeric variables, with each dot indicating the values of an individual data point on the horizontal and vertical axis. It is used to visualize relationships between variables.  (ref: https://chartio.com/learn/charts/what-is-a-scatter-plot/) <br>
Pairplot from the Seaborn library of Python is used for creating a grid of scatter plots and histograms, visualizing the pairwise relationships in a dataset. (ref: https://seaborn.pydata.org/generated/seaborn.pairplot.html) The comparison is made easier by having all the pairs of measurements plotted side by side using subplots. Where the same measurement paired, a histogram is drawn. The three separate species are colour coded in order to distinguish which measurement belongs to which Iris species. *(<pairplot.png>)* <br>
The pairplot demonstrates that Iris-setosa measurements are showing in their own cluster on multiple plots while versicolor and virginica have overlapping measurements in all.
When comparing petal and sepal measurements in pairs side by side on a separate plot *(<sepal_petal.png>)*, it is apparent that there is considerable overlap in sepal length and width across the different species. However, in terms of petal measurements, Iris-setosa is clearly separated having the smallest petals, while the majority of the versicolor and virginica samples are also distinct, with only slight overlap between them. Virginica noticeably having the largest petals, both in terms of length and width.
According to the scatter plots, the most effective pair of measurements for distinguishing between the three Iris species is petal width and length.<br>
Scatter plots can also indicate correlation between pairs of variables as demonstrated on the Petal Measurements scatter plot *(<sepal_petal.png>)*, where a correlation between petal length and width can be observed, revealing that the longer petals tend to be wider as well.<br>


## **Project task 4. Any other analysis**

### **Conditional means**
#### (Program menu: 5.) - Output saved in **<condmeans.png>**

The "Conditional Means" (condmeans.png) plot is a direct repurposing of a sample plot from the seaborn plot gallery. 
It is combining a strip plot for each of the flower measurement values and point plot for each of the means figures for each of the values grouped by species. The chart indicates the distinction of Iris-setosa values once again but it doesn't reveal additional information about the data, certainly can't assist with the distinction of the other two species. 

### **Correlation - Heatmap**
#### (Program menu: 6.) - Output saved in **<heatmap.png>**

Correlation between the different columns of the data can be calculated using pandas .corr() function which is using the Pearson method as default. (ref: https://zion-oladiran.medium.com/exploratory-data-analysis-iris-dataset-68897497b120)  
The Pearson correlation coefficient, takes a value between -1 and 1, measures linear correlation. A coefficient of 1 indicates positive correlation, while a coefficient of -1 indicates negative correlation. A coefficient of 0 means that the two variables likely have no effect on each other. (ref: https://www.scribbr.com/statistics/pearson-correlation-coefficient/#:~:text=The%20Pearson%20correlation%20coefficient%20(r,the%20relationship%20between%20two%20variables.) 
The resulting correlation matrix is displayed in terminal output however, a graphical representation of the matrix with a heatmap does help to recognize relevant patterns in the data.
A heatmap plot is a two-dimensional data-representation in which values are represented by colours to show relationships between two variables, one plotted on each axis. (ref: https://chartio.com/learn/charts/heatmap-complete-guide/)
<br>Such plot can be used for the representation of a correlation matrix, showing the relationships between pairs of variables as a grid of coloured squares. Each square's colour represents the value of the correlation coefficient.
Using seaborn's heatmap plot function the resulting heatmap (<heatmap.png>) reveals that there is a strong positive correlation (0.96) between petal length and petal width, as well as between sepal length and petal length and width (0.87 and 0.82).<br>
This indicates that the larger petals retain their proportions as they grow in size since the wider they are their length increases. Also revealed that a flower with a longer sepal will likely have a larger petal. 
Sepal width has a weak negative correlation with petal length and petal width. This suggests that the sepals may become slightly narrower as the petals grow in size. 

### **Petal Length and width measurement distribution among the species - Box plot**
#### (Program menu: 7.) - Plot saved in **<boxplot.png>**, petal measurement ranges for each species output to the terminal
<br>
A boxplot (or box and whisker plot) is the visualisation of data distribution based on five attributes; minimum, first quartile, median, third quartile and maximum. (ref: https://builtin.com/data-science/boxplot) The box represents the central 50% of the data with a line representing the median value, while the whiskers cover the remaining range of the data. Outliers are plotted outside the whiskers range as individual points. ˙ref: https://chartio.com/learn/charts/box-plot-complete-guide/)
As previous visualisations demonstrated, petal measurements are the most useful to distinguish the species therefore the box plot only focuses on petal lenght and width divided into two horizontal subplots arranged vertically. The three species are plotted on the same subplot for easier comparison. 
Once again, Iris-setosa shown completely separately on both subplots, just as it did in the scatter plots. The other two species also demonstrate the same overlap as before.
However, unlike the scatter plot, although very informative with regards to individual datapoints, the box plot provides a comprehensive picture of the data distribution as well, showing the median, typical values, and outliers.
Typical values or the central 50% of the datapoints show distinction between versicolor and virginica although 

Since the petal length data gives a wider range of values than the petal width data, it is more suitable to focus on the petal lengths for classification purposes.

## **Summary and proposed practical use of findings**
#### (Program menu: 8. Classifier routine) Classification result output to terminal and displayed on a box plot visualization saved as **<ClassificationResult.png>**

This project analysed Fisher's Iris dataset, originally published in 1936 describing 3 species of the Iris flower.
The data was downloaded and converted into a dataframe and after an initial "health-check" it was analysed using Python's pandas library. Matplotlib and seaborn libraries were used to visualize of the data.
The summary of each variable has not revealed anything useful although in retrospect petal length already noticeable with the highest standard deviation figure indicating the widest variation of values. Grouping the data per species did provide further insight in but without graphical illustration it was difficult make sense of the figures.
First visualization was a histogram for each measurement. It revealed that petal measurements produce bi- and multimodal histograms suggesting possible grouping within the data especially on the lower range of values.
The pair plot produced from the data creating a grid of scatter plots and histograms was much more revelative. Petal measurements for Iris-setosa very clearly stand apart while the other two species show some overlap. A positive correlation between petal length and width was also revealed.<br>
In further analysis a conditional means plot reinforced the separation of Iris-setosa samples.
A correlation analysis and the resulting heatmap plot supported the notion that the petals keep their proportions as they get bigger since length and width, and it is also indicated that flowers with larger petals are likely to have longer sepals.
As previously the sepal data proven to be ambiguous, the last visualization focused on petal measurements only.
The two box plots visualised minimum and maximum measurements and the outliers and revealed that the typical measurements for the species do stand apart even in the case of Iris-virginica and versicolor.

### **Findings:**

+ Only one of the three Iris species; Iris-setosa can be clearly separated based on the minimum and maximum size of petals.
+ While the other two species have overlapping data for petal dimensions, the analysis was able to establish a range for typical petal lengths and widths for the three species and visualised on a box plot: 
  + Iris-setosa typical petal length is between 1.4-1.58cm, 
  + Iris-versicolor is between 4.0-4.6cm and 
  + Iris-virginica petal length is between 5.1-5.88cm. 
+ A strong correlation demonstrated on scatter plots and heatmap visualization between petal widths and lengths indicate that across the three species the petals keep their proportions regardless of overall size.
+ A correlation demonstrated on a heatmap plot suggests that iris flowers with bigger petals likely to have longer sepals.

#### Practical use of the data:
##### (Program menu: 8. Classifier routine)

For a task of identifying species in future samples of Iris flowers without counting chromosomes we can use the min and max measurements of petal length for each species to separate them and leave only the overlapping ones for chromosome counting.
It is also possible to identify typical samples based solely on the Iris petal length data.
Based on petal measurements grouped by species a classifier routine was created <br>**(Program menu: 8. Classifier routine)**
<br>Since petal lengths have a much wider variety it was chosen to be the basis of classification.
The program functions as follows:<br>
The user can receive the species name based on petal length value.
The species is determined by the petal length falling within the range of the minimum and maximum values of that species.
The result is displayed on the terminal. <br>The output text is updated dynamically based on whether the sample matches any of the species' petal lengths.
If there is no match, the text indicates this and lists the minimum and maximum ranges for each species' petal lengths.
If the sample falls within an overlapping range, both relevant species are listed.
Finally, if sample value falls within a species' typical range, the output text indicates this as well.<br>
The program is complete with a box plot that displays the ranges of each species and the relative position of the new sample data.
<br>*Classification result displayed on the terminal and visualized on a box plot saved as **<ClassificationResult.png>**.*






