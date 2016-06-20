#!usr/bin/python
#-*- coding: utf-8 -*-

#Opening the file and appending everything to a list, copied from
#football exercise

import re
import numpy as np
import csv
from collections import OrderedDict

allInfo = []
headers = []
faculty_dict = {}

with open('faculty.csv','rb') as csvfile:
        lines = csv.reader(csvfile, delimiter=',', quotechar="|")
        for row in lines:
            allInfo.append(row)

headers = allInfo[0]
del allInfo[0]

for item in range(len(allInfo)):
    lastFinder = allInfo[item][0][::-1].find(' ')
    b = len(allInfo[item][0]) - lastFinder
    allInfo[item].append(allInfo[item][0][0:b-1])
    allInfo[item].append(allInfo[item][0][b:])
    faculty_dict.setdefault(allInfo[item][5], [])
    faculty_values = [allInfo[item][1],allInfo[item][2],allInfo[item][3]]
    faculty_dict[allInfo[item][5]].append(faculty_values)

professor_dict = {}
professor_keys = [(allInfo[x][4],allInfo[x][5]) for x in range(len(allInfo))]
professor_values = [[allInfo[x][1],allInfo[x][2],allInfo[x][3]] for x in range(len(allInfo))]
professor_dict = dict(zip(professor_keys,professor_values))

sorted_dict = OrderedDict(sorted(professor_dict.items(), key=lambda x: x[0][1]))

#print faculty_dict
#print professor_dict
#print sorted_dict
