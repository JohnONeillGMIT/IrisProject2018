# John O'Neill 17/04/2018 Inital Working with Numpy
''' 
The purpose of this file is to calculate the Min, Max, and Std Dev. of each column.
Measures were calculated for All the sample and for each individual Species(3) called out in the data set
Inital input taken from Ians Lecture on Mathplotlib https://web.microsoftstream.com/video/f0788c1c-c7bd-4347-98ac-477186938ed7
This is VERY BASIC (almost embarrassing) code I know but it works!! Keeping it simple for now! Will add loops etc later once I get the basics right.

The measured were outputted to the terminal and also to a Tabular view of the data.
Discovered Pandas later :-)... used this to cross check results of output (100% match)

'''
#Need to check "enumerate" as more effective command


import numpy as np
import statistics
from beautifultable import BeautifulTable # this module was iported as it provides a "better" way to show the data outputs

#read in the Iris file
#this pulls in the file containing all the Iris species in 1 file (overall measure)
data = np.genfromtxt('iris.csv', dtype=float, delimiter= ',',skip_header=1) #pulls in the iris.csv file, delimited by ','

firstcol = data[:,0] #assigns the 1st column of data from the csv file
#Sepal Length Column
#the 4 lines calculate measures for the list - mean, min, max, stdev

meanfirstcol =np.mean(data[:,0])
minfirstcol =np.min(data[:,0])
maxfirstcol =np.max(data[:,0])
devfirstcol =statistics.stdev(data[:,0]) 

secondcol = data[:,1] #assigns the 2nd column of data from the csv file
#Sepal Width Column
meansecondcol =np.mean(data[:,1]) 
minsecondcol =np.min(data[:,1])
maxsecondcol =np.max(data[:,1])
devsecondcol =statistics.stdev(data[:,1]) 

thirdcol = data[:,2] #assigns 3rd column of data from the csv file
#Petal Length Column
meanthirdcol =np.mean(data[:,2]) 
minthirdcol =np.min(data[:,2])
maxthirdcol =np.max(data[:,2])
devthirdcol =statistics.stdev(data[:,2]) 

fourthcol = data[:,3] #assigns the 4th column of data from the csv file
#Petal Width Column
meanfourthcol =np.mean(data[:,3]) 
minfourthcol =np.min(data[:,3])
maxfourthcol =np.max(data[:,3])
devfourthcol =statistics.stdev(data[:,3]) 

# importing the file with the 3 Iris species data files separately... bit simplistic I know!
data1 = np.genfromtxt('setosa.csv', dtype=float, delimiter= ',',skip_header=1) #pulls in the iris.csv file, delimited by ','

firstcol1 = data1[:,0] 
meanfirstcol1 =np.mean(data1[:,0]) 
minfirstcol1 =np.min(data1[:,0])
maxfirstcol1 =np.max(data1[:,0])
devfirstcol1 =statistics.stdev(data1[:,0]) 


secondcol1 = data1[:,1] 
meansecondcol1 =np.mean(data1[:,1]) 
minsecondcol1 =np.min(data1[:,1])
maxsecondcol1 =np.max(data1[:,1])
devsecondcol1 =statistics.stdev(data1[:,1])


thirdcol1 = data1[:,2] 
meanthirdcol1 =np.mean(data1[:,2]) 
minthirdcol1 =np.min(data1[:,2])
maxthirdcol1 =np.max(data1[:,2])
devthirdcol1 =statistics.stdev(data1[:,2])

fourthcol1 = data1[:,3] 
meanfourthcol1 =np.mean(data1[:,3]) 
minfourthcol1 =np.min(data1[:,3])
maxfourthcol1 =np.max(data1[:,3])
devfourthcol1 =statistics.stdev(data1[:,3])

data2 = np.genfromtxt('versicolor.csv', dtype=float, delimiter= ',',skip_header=1) #pulls in the iris.csv file, delimited by ','


firstcol2 = data2[:,0] 
meanfirstcol2 =np.mean(data2[:,0]) 
minfirstcol2 =np.min(data2[:,0])
maxfirstcol2 =np.max(data2[:,0])
devfirstcol2 =statistics.stdev(data2[:,0])

secondcol2 = data2[:,1] 
meansecondcol2 =np.mean(data2[:,1]) 
minsecondcol2 =np.min(data2[:,1])
maxsecondcol2 =np.max(data2[:,1])
devsecondcol2 =statistics.stdev(data2[:,1])

thirdcol2 = data2[:,2]
meanthirdcol2 =np.mean(data2[:,2]) 
minthirdcol2 =np.min(data2[:,2])
maxthirdcol2 =np.max(data2[:,2])
devthirdcol2 =statistics.stdev(data2[:,2])

fourthcol2 = data2[:,3] 
meanfourthcol2 =np.mean(data2[:,3]) 
minfourthcol2 =np.min(data2[:,3])
maxfourthcol2 =np.max(data2[:,3])
devfourthcol2 =statistics.stdev(data2[:,3])

data3 = np.genfromtxt('virginica.csv', dtype=float, delimiter= ',',skip_header=1) #pulls in the iris.csv file, delimited by ','

firstcol3 = data3[:,0]
meanfirstcol3 =np.mean(data3[:,0]) 
minfirstcol3 =np.min(data3[:,0])
maxfirstcol3 =np.max(data3[:,0])
devfirstcol3 =statistics.stdev(data3[:,0])

secondcol3 = data3[:,1] 
meansecondcol3 =np.mean(data3[:,1]) 
minsecondcol3 =np.min(data3[:,1])
maxsecondcol3 =np.max(data3[:,1])
devsecondcol3 =statistics.stdev(data3[:,1])

thirdcol3 = data3[:,2] 
meanthirdcol3 =np.mean(data3[:,2]) 
minthirdcol3 =np.min(data3[:,2])
maxthirdcol3 =np.max(data3[:,2])
devthirdcol3 =statistics.stdev(data3[:,2])

fourthcol3 = data3[:,3] 
meanfourthcol3 =np.mean(data3[:,3]) 
minfourthcol3 =np.min(data3[:,3])
maxfourthcol3 =np.max(data3[:,3])
devfourthcol3 =statistics.stdev(data3[:,3])
# 19/04/18 Installed a pip import to display the output data in a "nicer" tabular format
# https://stackoverflow.com/questions/8356501/python-format-tabular-output
# https://pypi.org/project/beautifultable/

#imported the module to create a "nice" output table to better represent the data
from beautifultable import BeautifulTable
table = BeautifulTable()
print("Measure of Iris - All Species")
table.column_headers = ["Species","Name", "Mean", "Min","Max", "Stdev"]
table.append_row(["All       ","Sepal_Length", meanfirstcol, minfirstcol,  maxfirstcol, devfirstcol])
table.append_row(["All       ","Sepal_Width", meansecondcol, minsecondcol, maxsecondcol,devsecondcol])
table.append_row(["All       ","Petal_Length", meanthirdcol, minthirdcol,  maxthirdcol, devthirdcol])
table.append_row(["All       ","Petal_Width", meanfourthcol, minfourthcol, maxfourthcol,devfourthcol])
print('\n',table,'\n') #adding a new line before and after the table for cosmetics

table1 = BeautifulTable()
print("Measure of Iris setosa")
table1.column_headers = ["Species","Name", "Mean", "Min","Max", "Stdev"]
table1.append_row(["setosa    ","Sepal_Length", meanfirstcol1, minfirstcol1,  maxfirstcol1,  devfirstcol1])
table1.append_row(["setosa    ","Sepal_Width", meansecondcol1, minsecondcol1, maxsecondcol1,devsecondcol1])
table1.append_row(["setosa    ","Petal_Length", meanthirdcol1, minthirdcol1,  maxthirdcol1,  devthirdcol1])
table1.append_row(["setosa    ","Petal_Width", meanfourthcol1, minfourthcol1, maxfourthcol1,devfourthcol1])
print('\n',table1,'\n')

table2 = BeautifulTable()
print("Measure of Iris versicolor")
table2.column_headers = ["Species","Name", "Mean", "Min","Max", "Stdev"]
table2.append_row(["versicolor","Sepal_Length", meanfirstcol2, minfirstcol2,  maxfirstcol2,  devfirstcol2])
table2.append_row(["versicolor","Sepal_Width", meansecondcol2, minsecondcol2, maxsecondcol2,devsecondcol2])
table2.append_row(["versicolor","Petal_Length", meanthirdcol2, minthirdcol2,  maxthirdcol2,  devthirdcol2])
table2.append_row(["versicolor","Petal_Width", meanfourthcol2, minfourthcol2, maxfourthcol2,devfourthcol2])
print('\n',table2,'\n')

table3 = BeautifulTable()
print("Measure of Iris virginica")
table3.column_headers = ["Species","Name", "Mean", "Min","Max", "Stdev"]
table3.append_row(["virginica ","Sepal_Length", meanfirstcol3, minfirstcol3,  maxfirstcol3, devfirstcol3])
table3.append_row(["virginica ","Sepal_Width", meansecondcol3, minsecondcol3, maxsecondcol3,devsecondcol3])
table3.append_row(["virginica ","Petal_Length", meanthirdcol3, minthirdcol3,  maxthirdcol3, devthirdcol3])
table3.append_row(["virginica ","Petal_Width", meanfourthcol3, minfourthcol3, maxfourthcol3,devfourthcol3])
print('\n',table3,'\n')

#I want to sent this data to a txt file output for later presentation in the Readme.md

with open('Output_of_SimpleMeasure_code.txt', 'w') as f:
   f.write(str(table)) #All Iris measures written to the Output file
   f.write(str(table1)) # setosa measures written to the Output file
   f.write(str(table2)) # versicolor measures written to the Output file
   f.write(str(table3)) # virginia measures written to the Output file