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
    header = ['time_decimal', 'sensor1', 'sensor2', 'sensor3', 'sensor4', 'sensor5', 'sensor6', 'sensor7', 'sensor8', 'sensor9', 'sensor10', 'sensor11', 'sensor12', 'sensor13', 'sensor14', 'date', 'time']
    write = csv.writer(file) 
    writer = csv.DictWriter(file, fieldnames = header) 
      
    # writing data row-wise into the csv file 
    writer.writeheader()     
    
    write.writerows(datalist) 
