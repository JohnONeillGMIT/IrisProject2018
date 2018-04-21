# John O'Neill 17/04/2018 Inital Working with Numpy
# Taken from Ians Lecture on Mathplotlib https://web.microsoftstream.com/video/f0788c1c-c7bd-4347-98ac-477186938ed7
# Keeping it simple for now! Will add loops etc later once I get the basics right.

#Calculating the mean of Col 1

import numpy
from beautifultable import BeautifulTable

#read in the Iris file
# this pulls in the file containing all the Iris species in 1 file (overall measure)
data = numpy.genfromtxt('iris.csv', dtype=float, delimiter= ',') #pulls in the iris.csv file, delimited by ','

firstcol = data[:,0] #assigns the first column of data from the csv file
#Sepal Length Column
meanfirstcol =numpy.nanmean(data[:,0]) #added nan so that columns with no value #n/a wont drive an error
minfirstcol =numpy.nanmin(data[:,0])
maxfirstcol =numpy.nanmax(data[:,0])

Secondcol = data[:,1] #assigns the first column of data from the csv file
#Sepal Width Column
meanSecondcol =numpy.nanmean(data[:,1]) 
minSecondcol =numpy.nanmin(data[:,1])
maxSecondcol =numpy.nanmax(data[:,1])

thirdcol = data[:,2] #assigns the first column of data from the csv file
#Petal Length Column
meanthirdcol =numpy.nanmean(data[:,2]) 
minthirdcol =numpy.nanmin(data[:,2])
maxthirdcol =numpy.nanmax(data[:,2])

fourthcol = data[:,3] #assigns the first column of data from the csv file
#Petal Width Column
meanfourthcol =numpy.nanmean(data[:,3]) 
minfourthcol =numpy.nanmin(data[:,3])
maxfourthcol =numpy.nanmax(data[:,3])


# importing the file with the 3 Iris species data files separately... bit simplistic I know!
data1 = numpy.genfromtxt('setosa.csv', dtype=float, delimiter= ',') #pulls in the iris.csv file, delimited by ','

firstcolv = data1[:,0] #assigns the first column of data from the csv file
meanfirstcolv =numpy.nanmean(data1[:,0]) #added nan so that columns with no value #n/a wont drive an error
minfirstcolv =numpy.nanmin(data1[:,0])
maxfirstcolv =numpy.nanmax(data1[:,0])

Secondcolv = data1[:,1] #assigns the first column of data from the csv file
meanSecondcolv =numpy.nanmean(data1[:,1]) #added nan so that columns with no value #n/a wont drive an error
minSecondcolv =numpy.nanmin(data1[:,1])
maxSecondcolv =numpy.nanmax(data1[:,1])

thirdcolv = data1[:,2] #assigns the first column of data from the csv file
meanthirdcolv =numpy.nanmean(data1[:,2]) #added nan so that columns with no value #n/a wont drive an error
minthirdcolv =numpy.nanmin(data1[:,2])
maxthirdcolv =numpy.nanmax(data1[:,2])

fourthcolv = data1[:,3] #assigns the first column of data from the csv file
meanfourthcolv =numpy.nanmean(data1[:,3]) #added nan so that columns with no value #n/a wont drive an error
minfourthcolv =numpy.nanmin(data1[:,3])
maxfourthcolv =numpy.nanmax(data1[:,3])

data2 = numpy.genfromtxt('versicolor.csv', dtype=float, delimiter= ',') #pulls in the iris.csv file, delimited by ','

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

fourthcolv = data2[:,3] #assigns the first column of data from the csv file
meanfourthcolv =numpy.nanmean(data2[:,3]) #added nan so that columns with no value #n/a wont drive an error
minfourthcolv =numpy.nanmin(data2[:,3])
maxfourthcolv =numpy.nanmax(data2[:,3])

data3 = numpy.genfromtxt('virginica.csv', dtype=float, delimiter= ',') #pulls in the iris.csv file, delimited by ','

firstcolv = data3[:,0] #assigns the first column of data from the csv file
meanfirstcolv =numpy.nanmean(data3[:,0]) #added nan so that columns with no value #n/a wont drive an error
minfirstcolv =numpy.nanmin(data3[:,0])
maxfirstcolv =numpy.nanmax(data3[:,0])

Secondcolv = data3[:,1] #assigns the first column of data from the csv file
meanSecondcolv =numpy.nanmean(data3[:,1]) #added nan so that columns with no value #n/a wont drive an error
minSecondcolv =numpy.nanmin(data3[:,1])
maxSecondcolv =numpy.nanmax(data3[:,1])

thirdcolv = data3[:,2] #assigns the first column of data from the csv file
meanthirdcolv =numpy.nanmean(data3[:,2]) #added nan so that columns with no value #n/a wont drive an error
minthirdcolv =numpy.nanmin(data3[:,2])
maxthirdcolv =numpy.nanmax(data3[:,2])

fourthcolv = data3[:,3] #assigns the first column of data from the csv file
meanfourthcolv =numpy.nanmean(data3[:,3]) #added nan so that columns with no value #n/a wont drive an error
minfourthcolv =numpy.nanmin(data3[:,3])
maxfourthcolv =numpy.nanmax(data3[:,3])
# 19/04/18 Installed a pip import to display the output data in a "nicer" tabular format
# https://stackoverflow.com/questions/8356501/python-format-tabular-output
# https://pypi.org/project/beautifultable/

#imported the module to create a "nice" output table to better represent the data
from beautifultable import BeautifulTable
table = BeautifulTable()
print("Measure of Iris - All Species")
table.column_headers = ["Species","Name", "Mean", "Min","Max"]
table.append_row(["All       ","Sepal_Length", meanfirstcol, minfirstcol, maxfirstcol])
table.append_row(["All       ","Sepal_Width", meanSecondcol, minSecondcol, maxSecondcol])
table.append_row(["All       ","Petal_Length", meanthirdcol, minthirdcol, maxthirdcol])
table.append_row(["All       ","Petal_Width", meanfourthcol, minfourthcol, maxfourthcol])
print('\n',table,'\n') #adding a new line before and after the table for cosmetics

table1 = BeautifulTable()
print("Measure of Iris setosa")
table1.column_headers = ["Species","Name", "Mean", "Min","Max"]
table1.append_row(["setosa    ","Sepal_Length", meanfirstcol, minfirstcol, maxfirstcol])
table1.append_row(["setosa    ","Sepal_Width", meanSecondcol, minSecondcol, maxSecondcol])
table1.append_row(["setosa    ","Petal_Length", meanthirdcol, minthirdcol, maxthirdcol])
table1.append_row(["setosa    ","Petal_Width", meanfourthcol, minfourthcol, maxfourthcol])
print('\n',table1,'\n')

table2 = BeautifulTable()
print("Measure of Iris versicolor")
table2.column_headers = ["Species","Name", "Mean", "Min","Max"]
table2.append_row(["versicolor","Sepal_Length", meanfirstcol, minfirstcol, maxfirstcol])
table2.append_row(["versicolor","Sepal_Width", meanSecondcol, minSecondcol, maxSecondcol])
table2.append_row(["versicolor","Petal_Length", meanthirdcol, minthirdcol, maxthirdcol])
table2.append_row(["versicolor","Petal_Width", meanfourthcol, minfourthcol, maxfourthcol])
print('\n',table2,'\n')

table3 = BeautifulTable()
print("Measure of Iris - Iris virginica")
table3.column_headers = ["Species","Name", "Mean", "Min","Max"]
table3.append_row(["virginica ","Sepal_Length", meanfirstcolv, minfirstcolv, maxfirstcolv])
table3.append_row(["virginica ","Sepal_Width", meanSecondcolv, minSecondcolv, maxSecondcolv])
table3.append_row(["virginica ","Petal_Length", meanthirdcolv, minthirdcolv, maxthirdcolv])
table3.append_row(["virginica ","Petal_Width", meanfourthcolv, minfourthcolv, maxfourthcolv])
print('\n',table3,'\n')

#I want to sent this data to a txt file output for later presentation in the Readme.md

with open('Output_of_SimpleMeasure_code.txt', 'w') as f:
   f.write(str(table)),'\n' #All Iris measures written to the Output file
   f.write(str(table1)),'\n' # setosa measures written to the Output file
   f.write(str(table2)),'\n' # versicolor measures written to the Output file
   f.write(str(table3)),'\n' # virgini measures written to the Output file

#https://campus.datacamp.com/courses/statistical-thinking-in-python-part-1/graphical-exploratory-data-analysis?ex=5&_escaped_fragment_=#next
