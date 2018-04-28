# John O'Neill 17/04/2018 - Using the Numpy.py file with column 1 to work on graphs from Mathplotlib.



#Calculating the mean of Col 1

# In order to run the data analysis and produce charts etc. I have to import these "modules"/"libraries" to perform the tasks.
import numpy as np # the AS gives you a shorthand version of the module name
import pandas as pd #https://www.pythonprogramming.net/data-analysis-python-pandas-tutorial-introduction/
import matplotlib.pyplot as plt #https://matplotlib.org/tutorials/introductory/sample_plots.html#sphx-glr-tutorials-introductory-sample-plots-py
import seaborn as sns #https://www.kaggle.com/jchen2186/machine-learning-with-iris-dataset/notebook NB
sns.set_palette('husl') #https://seaborn.pydata.org/tutorial/distributions.html?highlight=scatterplot ...learning seaborn 20/04


df= pd.read_csv('iris.csv')
print (df)

df.to_csv('newname.csv') #no index written to file in output https://www.youtube.com/watch?v=-0NwrcZOKhQ

#Learning for today!!: Having a file cal;led pandas.py in the directory causes and Attribute error!
#https://stackoverflow.com/questions/43696005/attributeerror-module-pandas-has-no-attribute-read-csv-python3-5





