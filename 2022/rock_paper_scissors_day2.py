# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 21:43:04 2022
@author: Nick
"""

filename = r'C:\Users\1109336\Documents\Python\AdventOfCode\2022\RockPaperScissorsStrategy.txt'

with open(filename) as fIn:
    games = fIn.read().split('\n')

# Scoring
# Rock = X,A,1, Paper = Y,B,2, Scissors = Z,C,3
# Loss = 0, Draw = 3, Win = 6

## Part 1
total = []
for game in games:
    shape = game[2]
    if shape == 'X':
        score = 1
    elif shape == 'Y':
        score = 2
    elif shape == 'Z':
        score = 3

    #Draw
    if game == 'A X' or game == 'B Y' or game == 'C Z':
        outcome = 3
    #Lose
    elif game == 'A Z' or game == 'B X' or game == 'C Y':
        outcome = 0
    #Win
    elif game == 'A Y' or game == 'B Z' or game == 'C X':
        outcome = 6
    total.append(score+outcome)

print('Total overall score: ', sum(total))

## Part 2
# X = Lose, Y = Draw, Z = Win
#A, B, C = Rock, Paper, Scissors
scoreboard = {'A Y': 4, 'B Y': 5, 'C Y': 6,
              'A X': 3, 'B X': 1, 'C X': 2,
              'A Z': 8, 'B Z': 9, 'C Z': 7}

newTotal = []
for game in games:
    newTotal.append(scoreboard.get(game))

print('New Strategy overall score: ', sum(newTotal))
