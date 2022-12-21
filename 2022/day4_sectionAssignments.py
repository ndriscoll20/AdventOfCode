# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 07:52:03 2022

@author: Nick
"""

filename = r'C:\Users\Nick\Documents\Python\AdventOfCode\2022\sectionAssignments.txt'
with open(filename) as fIn:
    lines = fIn.read().split('\n')
    
count = 0
for line in lines: 
    pair = line.split(',')
    rng1 = pair[0].split('-')
    rng2 = pair[1].split('-')
    rnglst1 = [*range(int(rng1[0]),int(rng1[1])+1)]
    rnglst2 = [*range(int(rng2[0]),int(rng2[1])+1)]
    #Part 1, use all, Part 2 use any
    if any(x in rnglst1 for x in rnglst2):
        count += 1
    elif any(x in rnglst2 for x in rnglst1):
        count += 1
    else:
        continue
    
print('Total number of sections overlapping: ', count)