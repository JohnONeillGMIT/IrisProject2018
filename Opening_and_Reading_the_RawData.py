#John O'Neill Iris formatting file 16/04/18

#version 1

import csv

with open("Data/Iris.csv", newline='') as f:
 for line in f:  #Python tutorial
   print('{:4}{:4}{:4}{:4}'.format(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3]))
#aligning the numbers in the columns with 1 space and added the splits
#code seems a bit rough but it works...


#Version 2 not using the line.split and .format
import csv

f= open("Data/Iris.csv",newline='') #aware this is not the optimum way to Open...but it works for me.
reader =csv.reader(f) #reader function to parse data from the file
#measures = 'P.Len' 'P.Wid''S.Len''S.Wid'
#print(measures)#insert headers
for row in reader:
  PetalLength = float(row[0])
  PetalWidth= float(row[1])
  SepalLength= float(row[2])
  SepalWidth= float(row[3])
  Description= str(row[4])
  print(row[0],row[1],row[2],row[3])

f.close


#Other Workings....

# https://www.youtube.com/watch?v=Xi52tx6phRU Referenced in relation to opening files in CSV and formatting "CSV Files in Python || Python Tutorial || Learn Python Programming"

 #for line in f:
  #line.split(',')
  #print(line)#need to convert thestring to alist

#list = int(line.split(','))
#for l in list:
 # print (list[0,1,2,4,5])
 #"with" opens and closes file when finished
#with open("Data/iris.csv.txt") as f:
  #  for line in f:
    #   print (line.split(',')([0])
        #line.split(',')
        

        #Line split breaks up a string and used the 
        #defined seaparator "," in this case placed between each variable
        #  http://www.pythonforbeginners.com/dictionary/python-split
   
        
        #output = '{0[:4.2f]}{1[:4.3f]}'
       # print(output)
    

#measures = ['PetalLength', 'PetalWidth','SepalLength','SepalWidth']
#output = '{0[1]}{0[2]}'.format(measures) 
#https://www.youtube.com/watch?v=vTX3IwquFkc (String Format Tutorial)
#print(output)

    
   # for x in openedfile[0,16]:
    #    print(repr(x).rjust(3), end='')
   # print(openedfile.read())
   # for line in openedfile:
    #    print(line.split(",")[0])
    #    '{}{}{}'.format('5''6''11')