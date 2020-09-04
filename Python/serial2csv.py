import os
import csv

datalist=[]
with open('telegramm.serial', 'r') as reader:
    for line in reader:
        if not line in ('\n', '\r\n'):
            datalist.append(line.split())

file = open('telegramm.csv', 'w+', newline ='') 
  
# writing the data into the file 
with file:     
    write = csv.writer(file) 
    write.writerows(datalist) 