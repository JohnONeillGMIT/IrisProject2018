# John O'Neill 22/04/2018 - 
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

'''

#Calculating the mean of Col 1

# In order to run the data analysis and produce charts etc. I have to import these "modules"/"libraries" to perform the tasks.
import numpy as np # the AS gives you a shorthand version of the module name
import pandas as pd #https://www.pythonprogramming.net/data-analysis-python-pandas-tutorial-introduction/
import matplotlib.pyplot as plt #https://matplotlib.org/tutorials/introductory/sample_plots.html#sphx-glr-tutorials-introductory-sample-plots-py
import seaborn as sns #https://www.kaggle.com/jchen2186/machine-learning-with-iris-dataset/notebook NB
#https://seaborn.pydata.org/tutorial/distributions.html?highlight=scatterplot...learning seaborn 20/04



#import seaborn as sns #https://seaborn.pydata.org/tutorial/distributions.html?highlight=scatterplot...learning seaborn 20/04
#sns.set_palette('husl')
#%matplotlib inline


df= pd.read_csv('iris.csv') #pandas takes the Iris.csv file as the input
print (df)

#https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/
#getting a lot of great information from this site!!
df['SL'][df['Species'] =='Iris-setosa'].mean() #gets mean od SL in Setosa!!
df.groupby('Species')# data is now "grouped" by Species of Iris
df.groupby('Species').groups.keys()# dict_keys(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'])


df.describe.groupby('Species'))


df.plot.scatter('SL','SW') #ref https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.plot.scatter.html
plt.show()


# histograms
df.hist()
plt.show()

df.to_csv('newname.csv') #no index written to file in output https://www.youtube.com/watch?v=-0NwrcZOKhQ

#Learning for today!!: Having a file cal;led pandas.py in the directory causes and Attribute error!
#https://stackoverflow.com/questions/43696005/attributeerror-module-pandas-has-no-attribute-read-csv-python3-5



