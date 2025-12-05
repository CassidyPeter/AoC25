# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 11:18:54 2025

@author: cassidy
"""

def reader():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    return lines

def solver(part):
    def remove():
        viable_rolls = 0
        removed_rolls = 0
        possible_neighbours = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)] # the 8 surrounding neighbours
        for x in range(len(grid)):
            for y in range(0,len(grid[0])):
                if grid[x][y] == '@':
                    nearby = 0
                    for dx,dy in possible_neighbours:
                        nx = x + dx
                        ny = y + dy
                        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]): # if a neighbours index is negative or greater than the length, it's not a viable neighbour
                            if grid[nx][ny]=='@':
                                nearby += 1
                    
                    if nearby < 4:
                        viable_rolls += 1
                        if part==2:
                            grid[x][y] = '.'
        return viable_rolls
    
    grid = [list(row) for row in reader()] # Convert grid to list of lists so it's mutable (Python fuckery)
    viable_rolls = viable_rolls_temp = remove()
    if part==2:
        while viable_rolls_temp != 0:
            viable_rolls += (viable_rolls_temp := remove())
    print(viable_rolls)


solver(1)
solver(2)
