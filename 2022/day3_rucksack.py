# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 08:39:54 2022

@author: Nick
"""
import string

#Scoring
letters = list(string.ascii_lowercase + string.ascii_uppercase)
scores = [x for x in range(1,53)]

scorecard = dict(zip(letters, scores))
with open(r'C:\Users\Nick\Documents\Python\AdventOfCode\2022\rucksack.txt') as fIn:
    lines = fIn.read().split('\n')

priority = []
for line in lines:
    half = int(len(line)/2)
    first = line[0:half]
    second = line[half:]
    for i in first:
        if i in second:
           priority.append(scorecard[i])
           break
           

    
print('Total value of all common items in rucksack: ', sum(priority))