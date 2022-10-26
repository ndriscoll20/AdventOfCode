# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 14:02:53 2021

@author: Nick
"""
import pandas as pd
import numpy as np

filename = "C:/Users/Nick/Documents/Python/AdventOfCode/commands.txt"

with open(filename) as file:
    lines = file.readlines()

commands = []
for ln in lines:
    ln = ln.split()
    commands.append(ln)

horizontal = 0
depth = 0


for cmd in range(0,len(commands)):
    if commands[cmd][0] == 'forward':
        horizontal = horizontal + int(commands[cmd][1])
    elif commands[cmd][0] == 'down':
        depth = depth + int(commands[cmd][1])
    elif commands[cmd][0] == 'up':
        depth = depth - int(commands[cmd][1])

final_position = horizontal * depth

print("Final horizontal: ", horizontal, "\n")
print("Final depth: ", depth, "\n")
print("Final position: ", horizontal*depth)

# Part 2

p2_horizontal = 0
p2_depth = 0
p2_aim = 0 

for cmd in range(0,len(commands)):
    if commands[cmd][0] == 'forward':
        p2_horizontal = p2_horizontal + int(commands[cmd][1])
        p2_depth = p2_depth + (p2_aim * int(commands[cmd][1]))
    elif commands[cmd][0] == 'down':
        p2_aim = p2_aim + int(commands[cmd][1])
    elif commands[cmd][0] == 'up':
        p2_aim = p2_aim - int(commands[cmd][1])

p2_final_position = p2_horizontal * p2_depth

print("Final horizontal: ", p2_horizontal, "\n")
print("Final depth: ", p2_depth, "\n")
print("Final aim", p2_aim, "\n")
print("Final position: ", p2_final_position)

# 1749524700 is the answer