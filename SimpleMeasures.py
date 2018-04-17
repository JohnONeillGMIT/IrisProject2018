# John O'Neill 17/04/2018 Inital Working with Numpy
# Taken from Ians Lecture on Mathplotlib https://web.microsoftstream.com/video/f0788c1c-c7bd-4347-98ac-477186938ed7
# Keeping it simple for now! Will add loops etc later once I get the basics right.

#Calculating the mean of Col 1

import numpy

#read in the Iris file

data = numpy.genfromtxt('iris.csv', dtype=float, delimiter= ',') #pulls in the iris.csv file, delimited by ','

firstcol = data[:,0] #assigns the first column of data from the csv file
meanfirstcol =numpy.nanmean(data[:,0]) #added nan so that columns with no value #n/a wont drive an error
minfirstcol =numpy.nanmin(data[:,0])
maxfirstcol =numpy.nanmax(data[:,0])

Secondcol = data[:,1] #assigns the first column of data from the csv file
meanSecondcol =numpy.nanmean(data[:,1]) #added nan so that columns with no value #n/a wont drive an error
minSecondcol =numpy.nanmin(data[:,1])
maxSecondcol =numpy.nanmax(data[:,1])

thirdcol = data[:,2] #assigns the first column of data from the csv file
meanthirdcol =numpy.nanmean(data[:,2]) #added nan so that columns with no value #n/a wont drive an error
minthirdcol =numpy.nanmin(data[:,2])
maxthirdcol =numpy.nanmax(data[:,2])

fourthcol = data[:,3] #assigns the first column of data from the csv file
meanfourthcol =numpy.nanmean(data[:,3]) #added nan so that columns with no value #n/a wont drive an error
minfourthcol =numpy.nanmin(data[:,3])
maxfourthcol =numpy.nanmax(data[:,3])


print("Average of the First column is:", meanfirstcol)
print("Min of the First column is:", minfirstcol)
print("Max of the First column is:", maxfirstcol)

print("Average of the Second column is:", meanSecondcol)
print("Min of the Second column is:", minSecondcol)
print("Max of the Second column is:", maxSecondcol)

print("Average of the Third column is:", meanthirdcol)
print("Min of the Third column is:", minthirdcol)
print("Max of the Third column is:", maxthirdcol)

print("Average of the First column is:", meanfourthcol)
print("Min of the First column is:", minfourthcol)
print("Max of the First column is:",maxfourthcol)
