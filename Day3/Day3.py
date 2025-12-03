# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 10:15:00 2025

@author: cassidy
"""

def reader():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    return lines



def part1():
    total_joltage = 0
    lines = reader()
    for bank in lines:
        digits = [int(c) for c in bank]
        maxL = max(digits[0:-1]) # max dec up to end -1
        idxL = digits.index(maxL) # index of max dec digit
        maxR = max(digits[idxL+1:]) # max single digit from index of max dec digit onwards
        total_joltage += maxL*10 + maxR

    print(total_joltage)


def part2():
    total_joltage = 0
    lines = reader()
    for bank in lines:
        highest_joltages = []
        for i in range(11,0,-1): # loop - first iteration excludes last 11, next last 10 etc
            highest_joltages.append(max(bank[:-i])) # add highest digit from bank excluding last i numbers of bank
            bank = bank[bank.index(highest_joltages[-1]) + 1 :] # index as to remove bank digits from in front of highest digit just found (shrink the bank)
        highest_joltages.append(max(bank)) # add remaining highest digit
        total_joltage += int("".join(highest_joltages))
    
    print(total_joltage)



part1()

part2()