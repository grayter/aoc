#!/usr/bin/python

import sys

pinpad = [[1,2,3],[4,5,6],[7,8,9]]

def getmove(direction):
    if direction == "U":
        return [-1,0]
    elif direction == "R":
        return [0,1]
    elif direction == "D":
        return [1,0]
    else:
        return [0,-1]

def endpoint(pos):
    if pos[0] < 0 or pos[0] > 2 or pos[1] < 0 or pos[1] > 2:
        return 1
    else:
        return 0

def code(pos):    
    return pinpad[pos[0]][pos[1]]
    
pos = [1,1]

with open(sys.argv[1]) as f:
    for line in list(f):
        line = line.strip()
        for dir in line:
            move = getmove(dir)
            newpos = [sum(pair) for pair in zip(pos, move)]
            if endpoint(newpos):    
                pass
            else:
                pos = newpos
        print code(pos)
