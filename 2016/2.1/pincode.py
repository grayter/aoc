#!/usr/bin/python

import sys

pinpad = [[0,0,1,0,0],[0,2,3,4,0],[5,6,7,8,9],[0,10,11,12,0],[0,0,13,0,0]]

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
    if pos[0] < 0 or pos[0] > 4 or pos[1] < 0 or pos[1] > 4 or pinpad[pos[0]][pos[1]] == 0:
        return 1
    else:
        return 0

def code(pos):    
    return hex(pinpad[pos[0]][pos[1]])
    
pos = [2,0]

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
