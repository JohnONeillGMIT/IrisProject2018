# John O'Neill 17/04/2018 - Using the Numpy.py file with column 1 to work on graphs from Mathplotlib.



#Calculating the mean of Col 1

# In order to run the data analysis and produce charts etc. I have to import these "modules"/"libraries" to perform the tasks.
import numpy as np # the AS gives you a shorthand version of the module name
import pandas as pd #https://www.pythonprogramming.net/data-analysis-python-pandas-tutorial-introduction/
import matplotlib.pyplot as plt #https://matplotlib.org/tutorials/introductory/sample_plots.html#sphx-glr-tutorials-introductory-sample-plots-py
import seaborn as sns #https://www.kaggle.com/jchen2186/machine-learning-with-iris-dataset/notebook NB


#import numpy as np #https://www.kaggle.com/jchen2186/machine-learning-with-iris-dataset/notebook NB
#import pandas as pd
#import seaborn as sns #https://seaborn.pydata.org/tutorial/distributions.html?highlight=scatterplot...learning seaborn 20/04
#sns.set_palette('husl')
#import matplotlib.pyplot as plt
#%matplotlib inline


data = pd.read_csv('virginica.csv') 
#Learning for today!!: Having a file cal;led pandas.py in the directory causes and Attribute error!
#https://stackoverflow.com/questions/43696005/attributeerror-module-pandas-has-no-attribute-read-csv-python3-5

df  = pd.read_csv("iris.csv")
df.plot()  # plots all columns against index
df.plot(kind='scatter',x='x',y='y') # scatter plot

#read in the Iris file

#data = numpy.genfromtxt('iris.csv', dtype=float, delimiter= ',') #pulls in the iris.csv file, delimited by ','

#firstcol = data[:,0] #assigns the first column of data from the csv file
#meanfirstcol =numpy.nanmean(data[:,0]) #added nan so that columns with no value #n/a wont drive an error
#minfirstcol =numpy.nanmin(data[:,0])
#maxfirstcol =numpy.nanmax(data[:,0])

#print("Average of the First column is:", meanfirstcol)
#print("Min of the First column is:", minfirstcol)
#print("Max of the First column is:", maxfirstcol)

