# John O'Neill 17/04/2018 - Using the Numpy.py file with column 1 to work on graphs from Mathplotlib.



#Calculating the mean of Col 1

import numpy

#read in the Iris file

data = numpy.genfromtxt('iris.csv', dtype=float, delimiter= ',') #pulls in the iris.csv file, delimited by ','

firstcol = data[:,0] #assigns the first column of data from the csv file
meanfirstcol =numpy.nanmean(data[:,0]) #added nan so that columns with no value #n/a wont drive an error
minfirstcol =numpy.nanmin(data[:,0])
maxfirstcol =numpy.nanmax(data[:,0])

print("Average of the First column is:", meanfirstcol)
print("Min of the First column is:", minfirstcol)
print("Max of the First column is:", maxfirstcol)

