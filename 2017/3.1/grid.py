#!/usr/bin/python

import sys
import math

val = int(sys.argv[1])
gridsize = int(math.ceil(math.sqrt(val)))
grid = [[0 for i in xrange(gridsize+1)] for j in xrange(gridsize+1)]
grid[0][0] = 1

def step(count):
    localgrid = int(math.ceil(math.sqrt(count)))
    if localgrid % 2 == 0:
        localgrid += 1        
    coord = [int(localgrid/2),-int(localgrid/2)]
    maxval = localgrid*localgrid
    difference = maxval-count
    whole_chunks = difference//(localgrid-1)
    effect = [[0,0,0,-1], [-1,0,1,1], [-1,1,0,1], [0,1,1,-1]]
    coord[0] += effect[whole_chunks][0] * (localgrid-1)
    coord[1] += effect[whole_chunks][1] * (localgrid-1)
    coord[effect[whole_chunks][2]] += (difference-(whole_chunks*(localgrid-1))) * effect[whole_chunks][3]
    return coord
    
def getval(pos):
    return grid[pos[0]+1][pos[1]+0] + \
        grid[pos[0]+1][pos[1]-1] + \
        grid[pos[0]+1][pos[1]+1] + \
        grid[pos[0]+0][pos[1]-1] + \
        grid[pos[0]+0][pos[1]+1] + \
        grid[pos[0]-1][pos[1]+0] + \
        grid[pos[0]-1][pos[1]-1] + \
        grid[pos[0]-1][pos[1]+1] 

islarger = False
loc = 2
while not islarger:
    pos = step(loc)
    grid[pos[0]][pos[1]] = getval(pos)
    islarger = grid[pos[0]][pos[1]] > val
    print loc, pos, grid[pos[0]][pos[1]]
    loc += 1



