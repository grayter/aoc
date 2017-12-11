#!/usr/bin/python

import sys

def move(pos, step):
    if step == "se":
        return [pos[0]+1, pos[1]]
    elif step == "nw":
        return [pos[0]-1, pos[1]]
    elif step == "sw":
        return [pos[0], pos[1]+1]
    elif step == "ne":
        return [pos[0], pos[1]-1]    
    elif step == "s":
        return [pos[0]+1, pos[1]+1]
    elif step == "n":
        return [pos[0]-1, pos[1]-1]

with open(sys.argv[1]) as f:
    steps = f.readlines()[0]
    steps = steps.strip()
    steps = steps.split(",")
    pos = [0,0]
    away = []

    
    for s in steps:
        pos = move(pos, s)
        away.append(max(map(abs,pos)))
        
    print pos
    print max(map(abs,pos))
    print max(away)
