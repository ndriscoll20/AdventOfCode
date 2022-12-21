# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 13:54:25 2022

@author: Nick
"""

filename = 'CalorieList.txt'
with open(filename) as fIn:
    lines = fIn.read().split('\n')

elfCalories = []
elves = []
for line in lines:    
    if line == '': 
        elves.append(sum(elfCalories))
        elfCalories=[]
    else:
        elfCalories.append(int(line))
#append last elf:
elves.append(sum(elfCalories))
        
print('Elf with the most calories has: ', max(elves), 'Calories')

elves.sort(reverse=True)

print('Sum of top 3 Elves Calories: ', sum(elves[0:3]))
