# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 10:15:00 2025

@author: cassidy
"""

def reader():
    with open("input.txt") as f:
        ranges = f.read().strip()
    return ranges.split(",")



def part1():
    ranges = reader()
    starts = []
    ends = []
    invIDs = 0

    for r in ranges:
        a,b = r.split("-")
        starts.append(int(a))
        ends.append(int(b))


    for start,end in zip(starts,ends):
        for n in range(start, end+1):
            # checks firstly for even length as invalid IDs contain only a sequence of digits repeated twice (can't be odd)
            # checks secondly that the first half of the string matches the second half of the string
            sn = str(n)
            if len(sn)%2==0 and sn[:len(sn)//2] == sn[len(sn)//2:]:
                invIDs += n

    print(invIDs)


def part2():
    ranges = reader()
    starts = []
    ends = []
    invIDs = 0

    for r in ranges:
        a,b = r.split("-")
        starts.append(int(a))
        ends.append(int(b))

    for start,end in zip(starts, ends):
        for n in range(start, end+1):
            sn = str(n)
            for num in range(1, len(sn)//2 + 1): # loop through numbers from 1 to midpoint of number n (to check 1-n/2 substrings)
                # checks if string is made by repeating block of length num an integer number of times
                # 1. firstly if total length isn't divisible by num then can't be tiled 
                # 2. then takes the first num as a candidate pattern and repeats enough times to match full length and check if reconstruction matches original
                if len(sn)%num==0 and sn== sn[:num]*(len(sn)//num):
                    invIDs += n
                    break # break as n already added to sum

    print(invIDs)


part1()

part2()