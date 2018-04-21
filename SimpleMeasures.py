# John O'Neill 17/04/2018 Inital Working with Numpy
# Taken from Ians Lecture on Mathplotlib https://web.microsoftstream.com/video/f0788c1c-c7bd-4347-98ac-477186938ed7
# Keeping it simple for now! Will add loops etc later once I get the basics right.

#Calculating the mean of Col 1

import numpy
from beautifultable import BeautifulTable

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



data2 = numpy.genfromtxt('virginica.csv', dtype=float, delimiter= ',') #pulls in the iris.csv file, delimited by ','

firstcolv = data2[:,0] #assigns the first column of data from the csv file
meanfirstcolv =numpy.nanmean(data2[:,0]) #added nan so that columns with no value #n/a wont drive an error
minfirstcolv =numpy.nanmin(data2[:,0])
maxfirstcolv =numpy.nanmax(data2[:,0])

Secondcolv = data2[:,1] #assigns the first column of data from the csv file
meanSecondcolv =numpy.nanmean(data2[:,1]) #added nan so that columns with no value #n/a wont drive an error
minSecondcolv =numpy.nanmin(data2[:,1])
maxSecondcolv =numpy.nanmax(data2[:,1])

thirdcolv = data2[:,2] #assigns the first column of data from the csv file
meanthirdcolv =numpy.nanmean(data2[:,2]) #added nan so that columns with no value #n/a wont drive an error
minthirdcolv =numpy.nanmin(data2[:,2])
maxthirdcolv =numpy.nanmax(data2[:,2])

fourthcolv = data[:,3] #assigns the first column of data from the csv file
meanfourthcolv =numpy.nanmean(data2[:,3]) #added nan so that columns with no value #n/a wont drive an error
minfourthcolv =numpy.nanmin(data2[:,3])
maxfourthcolv =numpy.nanmax(data2[:,3])
# 19/04/18 Installed a pip import to display the output data in a "nicer" tabular format
# https://stackoverflow.com/questions/8356501/python-format-tabular-output
# https://pypi.org/project/beautifultable/

from beautifultable import BeautifulTable
table = BeautifulTable()
print("Measure or Iris - All Species")
table.column_headers = ["Name", "Mean", "Min","Max"]
table.append_row(["SL", meanfirstcol, minfirstcol, maxfirstcol])
table.append_row(["SW", meanSecondcol, minSecondcol, maxSecondcol])
table.append_row(["PL", meanthirdcol, minthirdcol, maxthirdcol])
table.append_row(["PR", meanfourthcol, minfourthcol, maxfourthcol])
print(table)

table2 = BeautifulTable()
print("Measure or Iris virginica")
table2.column_headers = ["Name", "Mean", "Min","Max"]
table2.append_row(["SL", meanfirstcolv, minfirstcolv, maxfirstcolv])
table2.append_row(["SW", meanSecondcolv, minSecondcolv, maxSecondcolv])
table2.append_row(["PL", meanthirdcolv, minthirdcolv, maxthirdcolv])
table2.append_row(["PR", meanfourthcolv, minfourthcolv, maxfourthcolv])
print(table2)


#https://campus.datacamp.com/courses/statistical-thinking-in-python-part-1/graphical-exploratory-data-analysis?ex=5&_escaped_fragment_=#next
