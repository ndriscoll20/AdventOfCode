# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 10:50:19 2021

@author: Nick
"""

import pandas as pd
import numpy as np
import statistics as st

# filename = "C:/Users/Nick/Documents/Python/AdventOfCode/BingoNumbers.txt"

# with open(filename) as file:
#     lines = file.readlines()

# bingoNumbers = lines

# filename = "C:/Users/Nick/Documents/Python/AdventOfCode/BingoBoards.txt"

# with open(filename) as file:
#     lines = file.readlines()

# bingoBoards = lines

#load the boards into a list 
# bingoBoards = []
# for ln in lines:
#     if ln == '\n':
#         numBoards +=1
#         continue
#     else:
#         bingoBoards.append(ln.split())

with open('bingoBoardsTest.txt', 'r') as f:
    num_data, *board_data = f.read().split('\n\n')  # * operator unpacks lists
    f.close()
    
    

nums = list(map(int, num_data.split(',')))
sp_boards = [[[int(i) for i in x.split()] for x in r.split('\n') if x] for r in board_data]

#Count the number of boards
numBoards = len(board_data)

# find rows
for row in range(0,5):
    rows = sp_boards[0][row]
    for col in range(0,5):
        cols = sp_boards[0][row][col]

for board in numBoards:
    



    

def determineWinner(bingoBoard,called):
    #check rows
    
    #check columns
    
    
    
    for row in range(0,5):
        if called in bingoBoard[row]:
            winner = True
    for col in range(0,5):
        col = []
        for row in range(0,5):
            col.append(bingoBoard[row][col])
        
    return winner

called=[]
for num in range(0, len(bingoNumbers)):
    if len(called) >= 5:
        called.append(bingoNumbers[num])
        determineWinner(bingoBoards,called)
    else:
        continue
    
#Loop through boards: row+5*boardnum

