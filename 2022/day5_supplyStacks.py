# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 08:47:40 2022

@author: Nick
"""

filename = r'C:\Users\Nick\Documents\Python\AdventOfCode\2022\supplyStacks.txt'
with open(filename) as fIn:
    lines = fIn.read().split('\n')
    
stacks = lines[0:8]
moves  = lines[10:]

vertstacks = []
for stack in stacks: 
    vertstacks.append( [stack[i:i+4] for i in range(0,len(stack),4)] )

crane9000 = {'1':[], '2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[],'9':[]}
crane9001 = {'1':[], '2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[],'9':[]}
for i, key in enumerate(crane9000):    # loop through columns
    for j in reversed(range(0,8)):             # loop through rows
        if vertstacks[j][i].strip('[ ]') == '':
            continue
        crane9000[key].append(vertstacks[j][i].strip('[ ]'))
        crane9001[key].append(vertstacks[j][i].strip('[ ]'))
    
for move in moves: 
    crane = move.split(' ')
    nummoves = int(crane[1])
    origin = str(crane[3])
    dest = str(crane[5])
    for i in range(nummoves):
        crane9000[dest].append(crane9000[origin].pop())
    crane9001[dest].extend(crane9001[origin][-nummoves:])
    crane9001[origin][-nummoves:] = []
    
part1 = []
part2 = []
for key in crane9000.keys():
    part1.append(crane9000[key][-1])
    part2.append(crane9001[key][-1])
   

print('Crane 9000: ', part1[:])
print('Crane 9001: ', part2[:])