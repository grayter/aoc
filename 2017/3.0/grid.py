#!/usr/bin/python

import sys
import math

location = int(sys.argv[1])
gridsize = int(math.ceil(math.sqrt(location)))
if gridsize % 2 == 0:
    gridsize += 1

maxval   = gridsize*gridsize
coord = [int(gridsize/2), -int(gridsize/2)]

print "Gridsize ", gridsize
print "Maxval   ", maxval
print "Coord    ", coord

difference = maxval-location

print "Diff     ", difference

whole_chunks = difference//(gridsize-1)

print "WholeC   ", whole_chunks

effect = [[0,0,0,-1], [-1,0,1,1], [-1,1,0,1], [0,1,1,-1]]

coord[0] += effect[whole_chunks][0] * (gridsize-1)
coord[1] += effect[whole_chunks][1] * (gridsize-1)

print "Jumped   ", coord

coord[effect[whole_chunks][2]] += (difference-(whole_chunks*(gridsize-1))) * effect[whole_chunks][3]

print "Final    ", coord

print "Distance ", abs(coord[0]) + abs(coord[1])
