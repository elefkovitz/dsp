#!/usr/bin/python
#-*- coding: utf-8 -*-

import numpy as np
import csv

allInfo = []
headers = []
emails = []

with open('faculty.csv','rb') as csvfile:
        lines = csv.reader(csvfile, delimiter=',', quotechar="|")
        for row in lines:
            allInfo.append(row)

headers = allInfo[0]
del allInfo[0]

for x in allInfo:
    emails.append(x[3])

#for y in range(len(emails)):
#   emails[y] = "".join(emails[y])

with  open("emails.csv", 'wb') as resultFile:
    wr = csv.writer(resultFile, delimiter=',')
    for item in range(len(emails)):
        print emails[item]
        wr.writerow([emails[item]])
