#!usr/bin/python
#-*- coding: utf-8 -*-

#Opening the file and appending everything to a list, copied from
#football exercise

import re
import numpy as np
import csv

allInfo = []
headers = []

with open('faculty.csv','rb') as csvfile:
        lines = csv.reader(csvfile, delimiter=',', quotechar="|")
        for row in lines:
            allInfo.append(row)

headers = allInfo[0]
del allInfo[0]

#This sets up the regular expressions I will use to search for each type of
#degree. This feels like a really hacked solution, but I couldn't think of a
#better way to do it. Suggestions welcome!

#Also, did I screw up these Regex's? It's entirely possible! They are 100% new
#to me and were pretty complicated, so I did my best but it's totally possible I
#am grabbing some bad stuff in here or they're cumbersome or whatever else.
#I checked manually and I know the counts are right, but the syntax of these
#titles are pretty limited. Feedback appreciated!

degrees = [0,0,0,0,0,0,0,0]
degreeTypes = list(['phd', 'scd', 'mph', 'ma', 'ms', 'md', 'jd', 'bs'])

phd = re.compile('[^m]* *ph+ *.*(d+)\.*', re.IGNORECASE)
scd = re.compile('sc+ *.*(d+).*', re.IGNORECASE)
mph = re.compile('mph+', re.IGNORECASE)
ma = re.compile('ma+', re.IGNORECASE)
ms = re.compile('m+ *.*(s+).*', re.IGNORECASE)
md = re.compile('md+', re.IGNORECASE)
jd = re.compile('jd+', re.IGNORECASE)
bs = re.compile('b+ *.*(s+).*', re.IGNORECASE)

for item in allInfo:
    if re.search(phd, item[1]) is not None:
        degrees[0] = degrees[0] + 1
    if re.search(scd, item[1]) is not None:
        degrees[1] = degrees[1] + 1
    if re.search(mph, item[1]) is not None:
        degrees[2] = degrees[2] + 1
    if re.search(ma, item[1]) is not None:
        degrees[3] = degrees[3] + 1
    if re.search(ms, item[1]) is not None:
        degrees[4] = degrees[4] + 1
    if re.search(md, item[1]) is not None:
        degrees[5] = degrees[5] + 1
    if re.search(jd, item[1]) is not None:
        degrees[6] = degrees[6] + 1
    if re.search(bs, item[1]) is not None:
        degrees[7] = degrees[7] + 1
    print item[1], re.search(scd, item[1])
print degrees
print degreeTypes
#Find titles and counts of each
titleList = []
titleSet = set()

for item in allInfo:
    titleList.append(item[2])
    titleSet.add(item[2])
#print titleList
#print titleSet

#for x in titleSet:
    #print x, titleList.count(x)

#Find all emails, this is getting text-inefficient but for code clarity
#is okay for now!

emails = []
for item in allInfo:
    emails.append(item[3])
#print emails

#Finding different email domains and counts of each, copied from above with
#slightly more complicated search

domainList = []
domainSet = set()

for item in allInfo:
    domainList.append(item[3][item[3].find('@')+1:])
    #print item[3][item[3].find('@')+1:]
    domainSet.add(item[3][item[3].find('@')+1:])

#print titleList
#print titleSet

#for x in domainSet:
#    print x, domainList.count(x)
