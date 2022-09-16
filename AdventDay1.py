# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 14:34:05 2021

@author: Nick
"""
# Advent Calendar Day 1

import pandas as pd
import numpy as np


df_sonar = pd.read_csv(filepath_or_buffer="C:/Users/Nick/Documents/Python/AdventOfCode/SonarDepthMeasurements.csv")

np_sonar = df_sonar.to_numpy()

depth_increases = 0
window=3

for row in range(1,len(np_sonar)-(window-1)):
    if np.sum(np_sonar[row:row+window]) > np.sum(np_sonar[row-1:row-1+window]):
        depth_increases += 1 
    else:
        continue
    
print("Depth Increases:", depth_increases)


