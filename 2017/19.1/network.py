#!/usr/bin/python

import sys

diagram = []
pos = [0,0]
direction = [1,0]

with open(sys.argv[1]) as f:
    diagram = f.readlines()

# Find start
for i in xrange(0, len(diagram[0])):
    if diagram[0][i] == '|':
        pos = [0,i]
        break

# Follow
trail = []
steps = 0
while True:
    print pos, direction, "@", diagram[pos[0]][pos[1]], "@"
    npos = [x+y for (x,y) in zip(pos, direction)]
    if npos[0] < len(diagram) and npos[1] < len(diagram[npos[0]]) and npos[0] >= 0 and npos[1] >= 0 and diagram[npos[0]][npos[1]] != ' ':    
        steps += 1
        if diagram[npos[0]][npos[1]] not in [' ', '+', '-', '|']:
            print "Special", diagram[npos[0]][npos[1]]
            trail.append(diagram[npos[0]][npos[1]])
        elif diagram[npos[0]][npos[1]] == '+':
            print "Dir changer"
            direction = [direction[1], direction[0]]
            tentative = [x+y for (x,y) in zip(direction, npos)]
            if (tentative[0] > len(diagram) or tentative[1] > len(diagram[tentative[0]])) or diagram[tentative[0]][tentative[1]] == ' ':
                print "Twist"
                direction = [-direction[0], -direction[1]]
    else:
        steps += 1
        print "Found exit", pos, "".join(trail), steps
        sys.exit(0)

    pos = npos
