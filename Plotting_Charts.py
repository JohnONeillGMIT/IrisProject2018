# John O'Neill 26/04/2018 - Doingh the charts on separate files
# 
'''This file is an effort to learn how to use pandas and apply in the the measurements of iris data set
reviewing multiple tutorials on line. The data in then preseneted as scatter sharts.

References: 
https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/
https://www.pythonprogramming.net/data-analysis-python-pandas-tutorial-introduction/
https://matplotlib.org/tutorials/introductory/sample_plots.html#sphx-glr-tutorials-introductory-sample-plots-py
https://www.kaggle.com/jchen2186/machine-learning-with-iris-dataset/notebook
https://seaborn.pydata.org/tutorial/distributions.html?highlight=scatterplot
https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/
#22/04 https://pandas.pydata.org/pandas-docs/stable/groupby.html nbb

'''


# In order to run the data analysis and produce charts etc. I have to import these "modules"/"libraries" to perform the tasks.
import numpy as np # the AS gives you a shorthand version of the module name
import pandas as pd #https://www.pythonprogramming.net/data-analysis-python-pandas-tutorial-introduction/
import matplotlib.pyplot as plt #https://matplotlib.org/tutorials/introductory/sample_plots.html#sphx-glr-tutorials-introductory-sample-plots-py
import seaborn as sns #https://www.kaggle.com/jchen2186/machine-learning-with-iris-dataset/notebook NB
#https://seaborn.pydata.org/tutorial/distributions.html?highlight=scatterplot...learning seaborn 20/04
from matplotlib import style

data=pd.read_csv('iris.csv') #pandas takes the Iris.csv file as the input


#https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/
#came on the "groupby" information from this site and also saw the "Agg" command introduced
#https://intoli.com/blog/pandas-aggregation/ - further learning on the Agg functionality here
#data[][data['Species'] =='Iris-setosa'].mean() #gets mean od SL in Setosa!!
#data.groupby('Species')# data is now "grouped" by Species of Iris (just kept as learning point for me...)
#data.groupby('Species').groups.keys()# dict_keys(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']) (just kept as learning point for me...)

#stats = data.groupby('Species').agg(['mean','min','max'])
#stats.columns = [' '.join(col) for col in stats.columns] #concatenate the orig. colname (‘SL’) with name of the agg. function (‘max’).
#stats.reset_index() #tidies header column in table to align #https://intoli.com/blog/pandas-aggregation/ 

#stats.to_csv('Summary.csv')



#data.plot.scatter('SL','SW',c='Species') #ref https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.plot.scatter.html

#ax = plt.subplots()
#colors = {'Iris-setosa':'red', 'Iris-versicolor':'blue', 'Iris-virginica':'green'}
#grouped = data.groupby('Species')
#for key, group in grouped:
#   group.plot(ax=ax, kind='scatter', x='carat', y='price', label=key, colors=color[key])

#scatter_matrix(data)
#data.groupby('Species').groups.keys()
#plt.title('Scatter Chart of SL to SW relationship/n for All Data Sample')
#plt.legend()
#plt.show()


# I am using seaborn to plot the scatter as thiw was the "easiest" method to get the colurs of the Species outputted as I wanted.
#sns.FacetGrid(data, hue="Species")
#map(plt.scatter,'SL','SW')
#.add_legend()


# histograms
##data.hist()
#plt.show()


#Learning for today!!: Having a file cal;led pandas.py in the directory causes and Attribute error!
#https://stackoverflow.com/questions/43696005/attributeerror-module-pandas-has-no-attribute-read-csv-python3-5



