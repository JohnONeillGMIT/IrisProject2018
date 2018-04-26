# John O'Neill 17/04/2018 Inital Working with Numpy
# Taken from Ians Lecture on Mathplotlib https://web.microsoftstream.com/video/f0788c1c-c7bd-4347-98ac-477186938ed7
# This is VERY BASIC code I know!! Keeping it simple for now! Will add loops etc later once I get the basics right.
# Discovered Pandas later :-)
# Need to check "enumerate" as more effective command


import numpy as np
import statistics
from beautifultable import BeautifulTable

#read in the Iris file
#this pulls in the file containing all the Iris species in 1 file (overall measure)
data = np.genfromtxt('iris.csv', dtype=float, delimiter= ',') #pulls in the iris.csv file, delimited by ','

firstcol = data[:,0] #assigns the first column of data from the csv file
#Sepal Length Column
for x in firstcol: # looking at options to tidy the code...
    a =np.mean(data[:,0])
    b =np.min(data[:,0])
    c =np.max(data[:,0])
    d =statistics.mode(data[:,0]) #Return the most common data point...central location
    e =statistics.stdev(data[:,0]) 

Secondcol = data[:,1] #assigns the first column of data from the csv file
#Sepal Width Column
meanSecondcol =np.mean(data[:,1]) 
minSecondcol =np.min(data[:,1])
maxSecondcol =np.max(data[:,1])
d1 =statistics.mode(data[:,1]) 
e1 =statistics.stdev(data[:,1]) 

thirdcol = data[:,2] #assigns the first column of data from the csv file
#Petal Length Column
meanthirdcol =np.mean(data[:,2]) 
minthirdcol =np.min(data[:,2])
maxthirdcol =np.max(data[:,2])
d2 =statistics.mode(data[:,2]) 
e2 =statistics.stdev(data[:,2]) 

fourthcol = data[:,3] #assigns the first column of data from the csv file
#Petal Width Column
meanfourthcol =np.mean(data[:,3]) 
minfourthcol =np.min(data[:,3])
maxfourthcol =np.max(data[:,3])
d3 =statistics.mode(data[:,3]) 
e3 =statistics.stdev(data[:,3]) 

# importing the file with the 3 Iris species data files separately... bit simplistic I know!
data1 = np.genfromtxt('setosa.csv', dtype=float, delimiter= ',') #pulls in the iris.csv file, delimited by ','

firstcol1 = data1[:,0] #assigns the first column of data from the csv file
meanfirstcol1 =np.mean(data1[:,0]) #added nan so that columns with no value #n/a wont drive an error
minfirstcol1 =np.min(data1[:,0])
maxfirstcol1 =np.max(data1[:,0])

Secondcol1 = data1[:,1] #assigns the first column of data from the csv file
meanSecondcol1 =np.mean(data1[:,1]) #added nan so that columns with no value #n/a wont drive an error
minSecondcol1 =np.min(data1[:,1])
maxSecondcol1 =np.max(data1[:,1])

thirdcol1 = data1[:,2] #assigns the first column of data from the csv file
meanthirdcol1 =np.mean(data1[:,2]) #added nan so that columns with no value #n/a wont drive an error
minthirdcol1 =np.min(data1[:,2])
maxthirdcol1 =np.max(data1[:,2])

fourthcol1 = data1[:,3] #assigns the first column of data from the csv file
meanfourthcol1 =np.mean(data1[:,3]) #added nan so that columns with no value #n/a wont drive an error
minfourthcol1 =np.min(data1[:,3])
maxfourthcol1 =np.max(data1[:,3])

data2 = np.genfromtxt('versicolor.csv', dtype=float, delimiter= ',') #pulls in the iris.csv file, delimited by ','

firstcol2 = data2[:,0] #assigns the first column of data from the csv file
meanfirstcol2 =np.mean(data2[:,0]) 
minfirstcol2 =np.min(data2[:,0])
maxfirstcol2 =np.max(data2[:,0])

Secondcol2 = data2[:,1] #assigns the 2nd column of data from the csv file
meanSecondcol2 =np.mean(data2[:,1]) 
minSecondcol2 =np.min(data2[:,1])
maxSecondcol2 =np.max(data2[:,1])

thirdcol2 = data2[:,2] #assigns the 3rd column of data from the csv file
meanthirdcol2 =np.mean(data2[:,2]) 
minthirdcol2 =np.min(data2[:,2])
maxthirdcol2 =np.max(data2[:,2])

fourthcol2 = data2[:,3] #assigns the 4th column of data from the csv file
meanfourthcol2 =np.mean(data2[:,3]) 
minfourthcol2 =np.min(data2[:,3])
maxfourthcol2 =np.max(data2[:,3])

data3 = np.genfromtxt('virginica.csv', dtype=float, delimiter= ',') #pulls in the iris.csv file, delimited by ','

firstcol3 = data3[:,0]
meanfirstcol3 =np.mean(data3[:,0]) 
minfirstcol3 =np.min(data3[:,0])
maxfirstcol3 =np.max(data3[:,0])

Secondcol3 = data3[:,1] 
meanSecondcol3 =np.mean(data3[:,1]) 
minSecondcol3 =np.min(data3[:,1])
maxSecondcol3 =np.max(data3[:,1])

thirdcol3 = data3[:,2] 
meanthirdcol3 =np.mean(data3[:,2]) 
minthirdcol3 =np.min(data3[:,2])
maxthirdcol3 =np.max(data3[:,2])

fourthcol3 = data3[:,3] 
meanfourthcol3 =np.mean(data3[:,3]) 
minfourthcol3 =np.min(data3[:,3])
maxfourthcol3 =np.max(data3[:,3])
# 19/04/18 Installed a pip import to display the output data in a "nicer" tabular format
# https://stackoverflow.com/questions/8356501/python-format-tabular-output
# https://pypi.org/project/beautifultable/

#imported the module to create a "nice" output table to better represent the data
from beautifultable import BeautifulTable
table = BeautifulTable()
print("Measure of Iris - All Species")
table.column_headers = ["Species","Name", "Mean", "Min","Max","mode", "Stdev"]
table.append_row(["All       ","Sepal_Length", a, b, c,d,e])
table.append_row(["All       ","Sepal_Width", meanSecondcol, minSecondcol, maxSecondcol,d1,e1])
table.append_row(["All       ","Petal_Length", meanthirdcol, minthirdcol, maxthirdcol,d2,e2])
table.append_row(["All       ","Petal_Width", meanfourthcol, minfourthcol, maxfourthcol,d3,e3])
print('\n',table,'\n') #adding a new line before and after the table for cosmetics

table1 = BeautifulTable()
print("Measure of Iris setosa")
table1.column_headers = ["Species","Name", "Mean", "Min","Max"]
table1.append_row(["setosa    ","Sepal_Length", meanfirstcol1, minfirstcol1, maxfirstcol1])
table1.append_row(["setosa    ","Sepal_Width", meanSecondcol1, minSecondcol1, maxSecondcol1])
table1.append_row(["setosa    ","Petal_Length", meanthirdcol1, minthirdcol1, maxthirdcol1])
table1.append_row(["setosa    ","Petal_Width", meanfourthcol1, minfourthcol1, maxfourthcol1])
print('\n',table1,'\n')

table2 = BeautifulTable()
print("Measure of Iris versicolor")
table2.column_headers = ["Species","Name", "Mean", "Min","Max"]
table2.append_row(["versicolor","Sepal_Length", meanfirstcol2, minfirstcol2, maxfirstcol2])
table2.append_row(["versicolor","Sepal_Width", meanSecondcol2, minSecondcol2, maxSecondcol2])
table2.append_row(["versicolor","Petal_Length", meanthirdcol2, minthirdcol2, maxthirdcol2])
table2.append_row(["versicolor","Petal_Width", meanfourthcol2, minfourthcol2, maxfourthcol2])
print('\n',table2,'\n')

table3 = BeautifulTable()
print("Measure of Iris - Iris virginica")
table3.column_headers = ["Species","Name", "Mean", "Min","Max"]
table3.append_row(["virginica ","Sepal_Length", meanfirstcol3, minfirstcol3, maxfirstcol3])
table3.append_row(["virginica ","Sepal_Width", meanSecondcol3, minSecondcol3, maxSecondcol3])
table3.append_row(["virginica ","Petal_Length", meanthirdcol3, minthirdcol3, maxthirdcol3])
table3.append_row(["virginica ","Petal_Width", meanfourthcol3, minfourthcol3, maxfourthcol3])
print('\n',table3,'\n')

#I want to sent this data to a txt file output for later presentation in the Readme.md

with open('Output_of_SimpleMeasure_code.txt', 'w') as f:
   f.write(str(table)) #All Iris measures written to the Output file
   f.write(str(table1)) # setosa measures written to the Output file
   f.write(str(table2)) # versicolor measures written to the Output file
   f.write(str(table3)) # virgini measures written to the Output file

#https://campus.datacamp.com/courses/statistical-thinking-in-python-part-1/graphical-exploratory-data-analysis?ex=5&_escaped_fragment_=#next
