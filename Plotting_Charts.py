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

#data=pd.read_csv('iris.csv') #pandas takes the Iris.csv file as the input


'''
I originally had this scatter - all 1 colour and now what I wanted

data.plot.scatter(x='Sepal_Length',y='Sepal_Width') #ref https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.plot.scatter.html

plt.title('Scatter Chart of SL to SW relationship/n for All Data Sample')
plt.legend()
'''


sns.set(style="ticks", color_codes=True)
iris = sns.load_dataset('iris')
%matplotlib inline

iris = sns.load_dataset("iris")
sns.scatter(iris, hue="species")


#scatter_matrix(data)
#data.groupby('Species').groups.keys()

# I am using seaborn to plot the scatter as thiw was the "easiest" method to get the colurs of the Species outputted as I wanted.
#sns.FacetGrid(data, hue="Species")
#map(plt.scatter,'SL','SW')



# histograms
##data.hist()
#plt.show()


#Learning for today!!: Having a file cal;led pandas.py in the directory causes and Attribute error!
#https://stackoverflow.com/questions/43696005/attributeerror-module-pandas-has-no-attribute-read-csv-python3-5



