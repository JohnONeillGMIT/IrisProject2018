import numpy as np
import pandas as pd
import seaborn as sns
#sns.set_palette('husl')
import matplotlib.pyplot as plt

from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv('Iris.csv')

tmp = data.drop('Species', axis=1)

g = sns.violinplot(y='Species', x='Sepal_Length', data=data, inner='quartile')
plt.show()
g = sns.violinplot(y='Species', x='Sepal_Width', data=data, inner='quartile')
plt.show()
g = sns.violinplot(y='Species', x='Petal_Length', data=data, inner='quartile')
plt.show()
g = sns.violinplot(y='Species', x='Petal_Width', data=data, inner='quartile')
plt.show()