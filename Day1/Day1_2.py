# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 10:06:04 2025

@author: cassidy
"""

with open("input.txt") as f:
    lines = f.read().splitlines()

pos = 50
res = 0

for line in lines:
    dist = int(line[1:])
    if line[0]=="L":
        if (pos - dist) <= 0:
            res += abs(pos-dist)//100 + (pos != 0) # Counts number of times passes 0 by checking jumps of 100 (plus extra at end of fence-posting)
        pos = (pos - dist) % 100
    else:
        if (pos + dist) > 99:
            res += (pos + dist)//100
        pos = (pos + dist) % 100


print(res)

