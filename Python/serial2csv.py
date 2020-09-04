#!/usr/bin/env python
# encoding: utf-8

# SPDX-FileCopyrightText: © 2020 Bjoern Schilberg <bjoern.schilberg@angelaschule-osnabrueck.net>
# SPDX-License-Identifier: Apache-2.0

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
    header = ['time_decimal', 'wind_speed', 'wind_direction', 'temperature1', 'rel_humidity', 'air_pressure', 'radiation', 'precipitation', 'leaf_moistening', 'tensiometer', 'temperature2', 'temperature3', 'temperature4', 'special_input1', 'special_input2', 'date', 'time']
    write = csv.writer(file) 
    writer = csv.DictWriter(file, fieldnames = header) 
      
    # writing data row-wise into the csv file 
    writer.writeheader()     
    
    write.writerows(datalist) 
