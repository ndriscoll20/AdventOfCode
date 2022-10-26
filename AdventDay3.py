# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 16:57:04 2021

@author: Nick
"""

#Advent Day 3

import pandas as pd
import numpy as np
import statistics as st

filename = "C:/Users/Nick/Documents/Python/AdventOfCode/powerConsumption.txt"

with open(filename) as file:
    lines = file.readlines()
    
debug = []

for ln in lines:
    ln = ln.strip()
    tmp = [ln[i:i+1] for i in range(0,len(ln), 1)]
    debug.append(tmp)    
    
arr = np.array(debug)       #np array of strings
np_debug = np.array(debug, dtype = np.int32)    #np array of ints

gamma = np.zeros((1,12))
epsilon = np.zeros((1,12))
for ii in range(0,12):
    gamma[0,ii] = st.mode(arr[:,ii])
    
for ii in range(0,12):
    if gamma[0,ii] == 0:
        epsilon[0,ii] = 1
    elif gamma[0,ii] == 1:
        epsilon[0,ii] = 0
    
g = int(np.array2string(gamma).strip('[').strip(']').strip('.').replace('. ',''),2)
e = int(np.array2string(epsilon).strip('[').strip(']').strip('.').replace('. ',''),2)

power = g*e
# 2640986 is correct!

# values = [[0,0,1,0,0],
#         [1,1,1,1,0],
#         [1,0,1,1,0],
#         [1,0,1,1,1],
#         [1,0,1,0,1],
#         [0,1,1,1,1],
#         [0,0,1,1,1],
#         [1,1,1,0,0],
#         [1,0,0,0,0],
#         [1,1,0,0,1],
#         [0,0,0,1,0],
#         [0,1,0,1,0]]

# arr = np.array(values)

# Part 2
def find_mode(input_array, idx):        #finds the mode of the idx column
    primary_bit = st.mode(input_array[:,idx])
    return primary_bit

def find_index(mode_bit, input_arr,col):
    row_idx = input_arr[:,col] == mode_bit
    slice_arr = input_arr[row_idx,:]
    return slice_arr

def tiebreaker(o2orCo2):
    if o2orCo2 == 'o2':
        primary_bit = 1
    elif o2orCo2 == 'Co2':
        primary_bit = 0
    return primary_bit
        
# Test of find_mode function
slice_oxygen = np_debug
# slice_oxygen = arr
for ii in range(0, 12):
    prim = find_mode(slice_oxygen,ii)
    count = (slice_oxygen[:,ii] == prim).sum()
    if count == len(slice_oxygen)/2:
        prim = tiebreaker('o2')
    slice_oxygen = find_index(prim,slice_oxygen,ii)
    print(ii)
    if len(slice_oxygen)==1:
        break
    

slice_carbon = np_debug
# slice_carbon = arr
for ii in range(0, 12):
    prim = find_mode(slice_carbon,ii)
    if prim == 1:
        prim = 0
    elif prim == 0:
        prim = 1
    count = (slice_carbon[:,ii] == prim).sum()
    if count == len(slice_carbon)/2:
        tiebreaker('Co2')
    slice_carbon = find_index(prim,slice_carbon,ii)
    print(ii)
    if len(slice_carbon)==1:
        break

oxygenRate = int(np.array2string(slice_oxygen).strip('[').strip(']').replace(' ',''),2)

carbonRate = int(np.array2string(slice_carbon).strip('[').strip(']').replace(' ',''),2)    
lifeSupport = oxygenRate * carbonRate

#6822109 is correct!