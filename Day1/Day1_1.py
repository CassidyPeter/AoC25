# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 9:45:34 2025

@author: cassidy
"""

with open("input.txt") as f:
    lines = f.read().splitlines()

pos = 50
res = 0

for line in lines:
    dist = int(line[1:])
    if line[0]=="L":
        pos = (pos - dist) % 100 # modulo ensures pos between 0 and 99, kinda simple
    else:
        pos = (pos + dist) % 100

    res += pos == 0

print(res)

