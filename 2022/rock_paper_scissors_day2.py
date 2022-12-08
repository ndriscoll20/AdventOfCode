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

def __init__(self, games):
    self.games = games
    
def shapeScore(shape):
    if shape == 'X':
        score = 1
    elif shape == 'Y':
        score = 2
    elif shape == 'Z':
        score = 3
    return score

def outcomeScore(game):
    if game == 'A X' or 'B Y' or 'C Z':
        outcome = 3
    elif game == 'A Y' or 'B Z' or 'C A':
        outcome = 0
    elif game == 'A Z' or 'C Y' or 'B X':
        outcome = 6
    return outcome

gameScores=[]
for game in games:
    out1 = shapeScore(game[1])
    out2 = outcomeScore(game)
    total = out1+out2
    gameScores.append(total)
    
