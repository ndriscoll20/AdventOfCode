# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 12:06:19 2022

@author: Nick
"""

filename = r'C:\Users\Nick\Documents\Python\AdventOfCode\2022\buffer.txt'
with open(filename) as fIn:
    buffer = fIn.read()
    
packet = []
marker = []
for i in range(0,len(buffer)):
    packet.append(buffer[i])
    if len(marker) < 4:
        marker.append(buffer[i])
    else:
        marker.append(buffer[i])
        marker.pop(0)
    unq = list(set(marker))
    if len(unq) == 4:
        packetStart = len(packet)
        break
    
print('First Start of packet marker: ', packetStart)

#Part 2
packet = []
marker = []
for i in range(0,len(buffer)):
    packet.append(buffer[i])
    if len(marker) < 14:
        marker.append(buffer[i])
    else:
        marker.append(buffer[i])
        marker.pop(0)
    unq = list(set(marker))
    if len(unq) == 14:
        messageStart = len(packet)
        break
    
print('First Start of packet marker: ', messageStart)