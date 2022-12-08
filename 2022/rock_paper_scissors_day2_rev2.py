# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 22:30:19 2022

@author: Nick
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 21:43:04 2022

@author: Nick
"""

filename = r'C:\Users\Nick\Documents\Python\AdventOfCode\2022\rock_paper_scissors.txt'

with open(filename) as fIn:
    games = fIn.read().split('\n')
    
# Scoring
# Rock = X,A,1, Paper = Y,B,2, Scissors = Z,C,3
# Loss = 0, Draw = 3, Win = 6
total = []
for game in games:
    shape = game[2]
    if shape == 'X':
        score = 1
    elif shape == 'Y':
        score = 2
    elif shape == 'Z':
        score = 3

    if game == 'A X' or 'B Y' or 'C Z':
        outcome = 3
    elif game == 'A Y' or 'B Z' or 'C A':
        outcome = 0
    elif game == 'A Z' or 'C Y' or 'B X':
        outcome = 6
    total.append(score+outcome)

