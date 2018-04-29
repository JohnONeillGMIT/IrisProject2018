# John O'Neill 29/04/18

import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="ticks", color_codes=True)

iris = sns.load_dataset("iris")
g = sns.pairplot(iris, hue='species', markers='+')

plt.show()
