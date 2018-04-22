# John O'Neill 22/04/2018 - This file is an effort to learn how to use pandas and apply in the the measurements of iris data set
# reviewing multiple tutorials on line
#References: 
#https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/



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


#vir = pd.read_csv('iris.csv',index_col=0) # reading in the csv file, index_col
#print (vir.head())
#print (vir.dtypes)

df= pd.read_csv('iris.csv') #pandas takes the Iris.csv file as the input
print (df)

#https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/
#getting a lot of great information from this site!!
df['SL'][df['Species'] =='Iris-setosa'].mean() #gets mean od SL in Setosa!!
df.groupby('Species')# data is now "grouped" by Species of Iris
df.groupby('Species').groups.keys()# 

df.to_csv('newname.csv') #no index written to file in output https://www.youtube.com/watch?v=-0NwrcZOKhQ

#Learning for today!!: Having a file cal;led pandas.py in the directory causes and Attribute error!
#https://stackoverflow.com/questions/43696005/attributeerror-module-pandas-has-no-attribute-read-csv-python3-5

#df  = pd.read_csv("iris.csv")
#df.plot()  # plots all columns against index
#df.plot(kind='scatter',x='x',y='y') # scatter plot

