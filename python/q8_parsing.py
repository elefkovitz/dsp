#!/usr/bin/python
# -*- coding: utf-8 -*-
#The football.csv file contains the results from the English Premier League.
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import numpy as np
import csv

allInfo = []
headers = []
goalDifference = []

with open('football.csv','rb') as csvfile:
        lines = csv.reader(csvfile, delimiter=',', quotechar="|")
        for row in lines:
            allInfo.append(row)

headers = allInfo[0]
del allInfo[0]
#print headers

for i in range(len(allInfo)):
    goalDifference.append(abs(int(allInfo[i][5]) - int(allInfo[i][6])))

minGoalDiff = goalDifference.index(min(goalDifference))

print """The team with the smallest difference between goals scored and goals
allowed is %s, with a difference of %s.
"""  % (allInfo[minGoalDiff][0], goalDifference[minGoalDiff])
